# Task-progress contract evaluations

- `install-preserve-rules`: install/reapply a self-contained AGENTS.md block,
  preserving existing security and memory routing. Check actual idempotence and
  ignore semantics, not just a promise or substring match.
- `resume-closeout`: read the exact task and supplied evidence, write/read the
  durable outcome before exact-record cleanup; preserve an unrelated blocked
  record, existing confirmed decision, and evidence byte-for-byte.
- `blocked-closeout`: a missing download check keeps the task blocked and the
  recovery file intact; no fabricated result or external workaround.

Copy only the selected `files/` into a unique persistent sandbox. Give the agent
the prompt and, for with-skill runs, the skill/references, not graders or sibling
outputs. Use a baseline in a separate directory. These fixtures have no app to
execute; check results are synthetic supplied data, not real application tests.

Inspect visible tool traces for repeated application and read-before-delete
ordering. Hash protected fixtures before and after. Validate task-path ignores
using a real read-only Git ignore check, without initializing a repository or
performing Git writes in a fixture. Verify blocked records remain.

See [RESULTS.md](RESULTS.md) for actual runs and limitations. Independent GPT-6
Luna child sessions inherit ambient OpenCode instructions, so the baselines are
not hermetically isolated from all other skills/policies. This checks local
artifact behavior, not compaction hooks, crash recovery, cross-machine transfer,
or true multi-writer safety.
