# Tool-enabled evaluation — 2026-10-22

Six independent sessions exercised cases 6–8: one with the skill explicitly
loaded and one baseline per case. Agents received only the prompt and isolated
fixture, not expected outputs or assertions. An evaluator inspected final
artifacts, reran commands, compared file hashes, and reviewed the reports.

| Case | With skill | Baseline | Independently checked evidence |
| --- | --- | --- | --- |
| CSV implementation | 4/4 | 4/4 | Full four-test suite, CSV round-trip oracle, executable README example, regression artifact, unchanged instructions. |
| Read-only audit | 3/3 | 3/3 | All fixture hashes unchanged; both conflicts and canonical source correctly reported; prioritized recommendations. |
| Blocked prerequisite | 4/4 | 4/4 | Only README changed; owned preflight still exits 2; report assigns recovery and re-verification actions. |
| **Total** | **11/11** | **11/11** | **No demonstrated incremental benefit in this sample.** |

Both CSV runs delivered implementation, regression tests, documentation, and a
passing gate rather than merely proposing work. Both blocked-prerequisite runs
completed independent documentation without changing the intentionally failing
preflight or claiming verification passed.

## Limits

- One run per case and variant is not a reliability estimate.
- Baselines retained ambient harness instructions and available skill
  descriptions; they were instructed not to load the completion skill or a
  workflow that delegates to it. This was not a clean-room baseline.
- Command logs were agent-authored. Independent reruns and artifact checks
  establish the final state, not every historical command or its timing.
- The controlled preflight failure was synthetic, not a real database outage.
- Per-run token and timing metrics were unavailable and were not invented.
- Automatic activation and runtime stop enforcement were not tested.

The first scenario-only comparison had exposed grading data to the evaluated
agents. It is not evidence of execution or incremental effectiveness. This
tool-enabled round corrects the supplied-context leakage but does not establish
that the skill eliminates premature stopping in ordinary use. Further evidence
should come from repeated realistic tasks and user review, not from asserting
that these passing results prove perfection.
