# 0006: Do not build the guide yet

**Decision:** The guide that proposes the next step is not built. The family writes one trace row per job instead, and reruns the replay when about thirty rows with the person's verdicts exist.

**Status:** accepted, 2026-11-03. **Shape:** [decision record](https://github.com/Tewf/reader-ergonomics/blob/2e5b6f0c3e67d2dc8195a63cf882d46170e79a5a/shapes/decision-record.md).

## Context

- The maintainer asked whether a guide, an AI or a program, could help the family reach the optimum, if the idea was good.
- The [design](../design/guide.md) models a project as a sequential decision problem under an unknown objective and maps the field's solutions onto it.
- The first test is [a replay](../design/replay.md) of [the family's trace](../design/trace.md): 36 jobs of two days, seven decision points.
- Three policies hit the kind of step the maintainer chose once in seven; chance hits 2.7; UCB1 hit three times by trying unrun kinds.
- The value-of-information stop fired at the second wave because the data could not tell the kinds apart.

## Decision

- **No repository for the guide yet.** The family's rule is one repository per problem; the problem is not yet shown to be solved.
- **Keep the trace.** [guide/trace.toml](../guide/trace.toml) and [guide/replay.py](../guide/replay.py) stay here, with their tests, as the instrument.
- **Write one row per job at its close:** kind, agents, tokens, and the outcomes moved and kept, filled by the person or by a rule the person wrote.
- **The bar for a spike, stated before the next run:** one policy hits at least 5 of the next 7 waves on both outcomes, with the menu generated from the state. Chance hits about 3.
- **If the bar is met,** the spike is one day: a proposal file written for one live wave, compared with the maintainer's choice. It then becomes its own repository.

## Consequences

- The trace costs the maintainer a few lines per job and gives the next replay real costs and the person's verdicts.
- **Bad:** the answer to the maintainer's question is "not yet", on one trace written by a model from a log. The result could change with a different outcome definition.
- **Bad:** the stop's ceiling and the meter conversion are crude and may mislead; the replay page says so.
- **Not chosen:** building the guide on one trace, which gives a policy that proposes a review at every wave.
- **Not chosen:** a guide that decides, which the objective's dependence on the person's judgment rules out.

## See also

[Decisions](README.md); [the design](../design/guide.md); [the replay](../design/replay.md); [0005](0005-the-project-as-optimisation-of-an-unknown-objective.md).
