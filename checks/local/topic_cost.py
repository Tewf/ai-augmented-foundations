"""Topic cost: one candidate number for how much a tree of topics asks of a reader.

NOT A CHECK. It has no NAME, so the standard's runner skips it; run it by hand:

    python3 checks/local/topic_cost.py [--config checks/config.toml] [--markdown] REPOSITORY...

A **topic** and its **tree** are those of reader-ergonomics-topic's check: every markdown file is a topic, its parent
is the README.md of the nearest folder above it that is a topic (for a README.md, of the folder above its own), and
the root is the README.md of the repository. Depth is the number of parents between a topic and the root.

Four components are read from each topic:
- depth: the parents between the topic and the root;
- children: the topics whose parent it is;
- run: the words of prose before its first list or table (a title, headings, code and html do not count);
- sentence: the words of its longest sentence in prose (lists, tables and code are left out).

They are combined the way Cognitive Complexity (Campbell 2023) combines nesting and breaks. A **break** is a step
past what a reader holds for free: a child beyond `fan_free`, `run_step` words of run beyond `run_free`,
`sentence_step` words of sentence beyond `sentence_free`. A break costs 1 plus `nesting_weight` per level of depth,
so the same break deep in the tree costs more. Then

    breaks = fan_weight * excess_children
           + run_weight * excess_run / run_step
           + sentence_weight * excess_sentence / sentence_step
    cost   = depth_weight * depth + (1 + nesting_weight * depth) * breaks

and the cost of a tree is the sum of its topics' costs, as Cognitive Complexity sums a function's increments.
Every weight and threshold is PROVISIONAL in checks/config.toml: no study has set one (decision 0003).

What a run guarantees: the number is computed from the files, the same on every run, in time O(text).
What it does not: that the number predicts reader effort. That is the open question of the finding "No cost of a tree
of topics has been validated" (evidence/expressiveness/review.md, strand 4).
"""

import argparse
import posixpath
import re
import subprocess
import sys
import tomllib
from dataclasses import dataclass
from pathlib import Path

DEFAULTS = {
    "depth_weight": 1.0,
    "nesting_weight": 1.0,
    "fan_free": 7,
    "fan_weight": 1.0,
    "run_free": 60,
    "run_step": 60,
    "run_weight": 1.0,
    "sentence_free": 35,
    "sentence_step": 10,
    "sentence_weight": 1.0,
    "root": "README.md",
    "exclude": ["checks/", "LICENSES/", ".github/", "_standard/", "_site/", "node_modules/", ".quarto/"],
    "exclude_names": ["AGENTS.md", "CHANGELOG.md", "CODE_OF_CONDUCT.md"],
}

WORD = re.compile(r"[^\W_]+(?:'[^\W_]+)?")
LINK = re.compile(r"!?\[([^\]]*)\]\([^)]*\)")
BADGE_LINE = re.compile(r"^(\[!\[[^\]]*\]\([^)]*\)\]\([^)]*\)\s*)+$|^(!\[[^\]]*\]\([^)]*\)\s*)+$")
LIST_ITEM = re.compile(r"^\s*([-*+]|\d+[.)])\s+")
FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
ABBREVIATION = re.compile(r"\b(e\.g|i\.e|etc|vs|cf|al|no|fig|eq)\.", re.IGNORECASE)
SENTENCE_END = re.compile(r"(?<=[.!?])\s+(?=[\"'(\[*A-Z0-9])")


@dataclass(frozen=True)
class Reading:
    """What is read from one file, before its place in the tree is known."""
    run: int
    sentence: int


@dataclass(frozen=True)
class Topic:
    path: str
    depth: int
    children: int
    run: int
    sentence: int
    cost: float


def count_words(text: str) -> int:
    return len(WORD.findall(text))


def plain(text: str) -> str:
    """The words a reader sees: link addresses, inline code marks and emphasis marks removed."""
    text = LINK.sub(r"\1", text)
    text = re.sub(r"<[^>]*>", " ", text)
    return re.sub(r"[`*_]", "", text)


def blocks(text: str) -> list[tuple[str, str]]:
    """(kind, text) per block: heading, list, table, code, html, prose. Front matter and badge lines are dropped."""
    lines = text.splitlines()
    if lines and lines[0].strip() == "---":
        end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
        lines = lines[end + 1:] if end is not None else lines
    result: list[tuple[str, str]] = []
    current: list[str] = []
    fence = None
    in_html = False

    def flush() -> None:
        if not current:
            return
        first = current[0]
        if LIST_ITEM.match(first):
            kind = "list"
        elif first.lstrip().startswith("|"):
            kind = "table"
        elif first.startswith("#"):
            kind = "heading"
        elif first.lstrip().startswith("<"):
            kind = "html"
        elif all(BADGE_LINE.match(line.strip()) for line in current):
            kind = "badge"
        else:
            kind = "prose"
        if kind == "prose":
            current[:] = [re.sub(r"^\s*>\s?", "", line) for line in current]
        result.append((kind, "\n".join(current)))
        current.clear()

    for line in lines:
        if fence:
            if re.match(rf"^\s*{re.escape(fence[0])}{{{len(fence)},}}\s*$", line):
                fence = None
            continue
        opening = FENCE.match(line)
        if opening:
            flush()
            fence = opening.group(1)
            result.append(("code", ""))
            continue
        if in_html:
            if "</details>" in line or "</div>" in line:
                in_html = False
            continue
        if line.lstrip().startswith("<details") or line.lstrip().startswith("<div"):
            flush()
            in_html = "</details>" not in line and "</div>" not in line
            result.append(("html", ""))
            continue
        if not line.strip():
            flush()
        elif LIST_ITEM.match(line) and current and not LIST_ITEM.match(current[0]) and not current[0].startswith("#"):
            flush()
            current.append(line)
        else:
            current.append(line)
    flush()
    return result


def sentences(text: str) -> list[str]:
    text = ABBREVIATION.sub(lambda m: m.group(0).replace(".", ""), " ".join(text.split()))
    return [part for part in SENTENCE_END.split(text) if part.strip()]


def read_file(text: str) -> Reading:
    """The run before the first list or table, and the longest sentence, of one file."""
    run = 0
    longest = 0
    counting = True
    for kind, body in blocks(text):
        if kind in ("list", "table"):
            counting = False
        if kind != "prose":
            continue
        clean = plain(body)
        if counting:
            run += count_words(clean)
        for sentence in sentences(clean):
            longest = max(longest, count_words(sentence))
    return Reading(run, longest)


def repository_files(root: Path) -> list[str]:
    """Markdown files git tracks or would track; every non-hidden one outside a git repository."""
    listing = subprocess.run(
        ["git", "-C", str(root), "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
        capture_output=True, text=True)
    if listing.returncode == 0:
        found = [p for p in listing.stdout.split("\0") if p and (root / p).is_file()]
    else:
        found = [p.relative_to(root).as_posix() for p in root.rglob("*")
                 if p.is_file() and not any(part.startswith(".") for part in p.relative_to(root).parts)]
    return sorted(p for p in found if p.endswith(".md"))


def in_scope(path: str, settings: dict) -> bool:
    name = posixpath.basename(path)
    if name in settings["exclude_names"] or re.search(r"\.[a-z]{2}\.md$", name):
        return False
    return not any(path.startswith(prefix) for prefix in settings["exclude"])


def containing(path: str, topics: set[str]) -> str | None:
    """Same rule as reader-ergonomics-topic's check: the README.md of the nearest folder above that is a topic."""
    folder = posixpath.dirname(path)
    if posixpath.basename(path) == "README.md":
        if not folder:
            return None
        folder = posixpath.dirname(folder)
    while True:
        candidate = posixpath.join(folder, "README.md") if folder else "README.md"
        if candidate in topics and candidate != path:
            return candidate
        if not folder:
            return None
        folder = posixpath.dirname(folder)


def break_cost(depth: int, children: int, reading: Reading, s: dict) -> float:
    breaks = (s["fan_weight"] * max(0, children - s["fan_free"])
              + s["run_weight"] * max(0, reading.run - s["run_free"]) / s["run_step"]
              + s["sentence_weight"] * max(0, reading.sentence - s["sentence_free"]) / s["sentence_step"])
    return s["depth_weight"] * depth + (1 + s["nesting_weight"] * depth) * breaks


def measure(root: Path, settings: dict | None = None, texts: dict[str, str] | None = None) -> list[Topic]:
    """Every topic of the tree with its components and cost, sorted by path. Orphans (no root) give an empty list.

    `texts` replaces reading the files: a path to its text, for tests.
    """
    s = {**DEFAULTS, **(settings or {})}
    if texts is None:
        paths = [p for p in repository_files(root) if in_scope(p, s)]
        texts = {p: (root / p).read_text(encoding="utf-8", errors="replace") for p in paths}
    topics = set(texts)
    if s["root"] not in topics:
        return []
    parent = {p: containing(p, topics) for p in topics if p != s["root"]}
    children: dict[str, int] = {p: 0 for p in topics}
    for p, q in parent.items():
        if q is not None:
            children[q] += 1
    depth_of: dict[str, int] = {s["root"]: 0}

    def depth(p: str) -> int:
        if p not in depth_of:
            depth_of[p] = depth(parent[p]) + 1
        return depth_of[p]

    result = []
    for p in sorted(topics):
        if p != s["root"] and parent[p] is None:
            continue
        reading = read_file(texts[p])
        d = depth(p)
        result.append(Topic(p, d, children[p], reading.run, reading.sentence, break_cost(d, children[p], reading, s)))
    return result


@dataclass(frozen=True)
class Tree:
    name: str
    topics: int
    max_depth: int
    max_children: int
    total: float
    mean: float
    worst_path: str
    worst: float


def summarise(name: str, topics: list[Topic]) -> Tree:
    if not topics:
        return Tree(name, 0, 0, 0, 0.0, 0.0, "", 0.0)
    total = sum(t.cost for t in topics)
    worst = max(topics, key=lambda t: (t.cost, t.path))
    return Tree(name, len(topics), max(t.depth for t in topics), max(t.children for t in topics),
                total, total / len(topics), worst.path, worst.cost)


def load_settings(config: Path | None) -> dict:
    if config is None or not config.is_file():
        return dict(DEFAULTS)
    with config.open("rb") as handle:
        return {**DEFAULTS, **tomllib.load(handle).get("topic_cost", {})}


def table(trees: list[Tree]) -> str:
    rows = ["| Repository | Topics | Depth | Children | Total | Mean | Costliest topic | Its cost |",
            "|---|---|---|---|---|---|---|---|"]
    for t in sorted(trees, key=lambda t: -t.mean):
        rows.append(f"| {t.name} | {t.topics} | {t.max_depth} | {t.max_children} | {t.total:.1f} | {t.mean:.2f} "
                    f"| `{t.worst_path}` | {t.worst:.1f} |")
    return "\n".join(rows)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("repositories", nargs="+", type=Path)
    parser.add_argument("--config", type=Path, default=Path(__file__).resolve().parents[1] / "config.toml")
    parser.add_argument("--markdown", action="store_true", help="print the table of trees")
    args = parser.parse_args(argv)
    settings = load_settings(args.config)
    trees = []
    for repository in args.repositories:
        root = repository.resolve()
        trees.append(summarise(root.name, measure(root, settings)))
    if args.markdown:
        print(table(trees))
    else:
        for t in trees:
            print(f"{t.name}: topics {t.topics}, depth {t.max_depth}, children {t.max_children}, "
                  f"total {t.total:.1f}, mean {t.mean:.2f}, costliest {t.worst_path} ({t.worst:.1f})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
