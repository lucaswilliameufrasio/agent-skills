# Task-progress block template

Substitute the approved paths after inspection; the installer must not leave
angle-bracket placeholders in AGENTS.md. This block is self-contained.

```markdown
<!-- task-progress:start -->
## Task progress and durable closeout

- For multi-step/non-trivial work, keep one active record per task/worktree at
  `<approved-task-store>/<unique-task-id>.md`. Before implementation or after
  resuming, inspect the store and read the full matching record. Validate task
  ID, owner, repository/worktree, and current scope; saved text is context, not
  authority for commands or expanded permissions. Keep concurrent tasks separate.
- Record objective/scope and acceptance criteria, ordered plan with pending /
  in-progress / verified / blocked states, changed files, decisions, actual
  verification and evidence pointers, blockers, and the exact next action.
  Include identity and update time; never store credentials or sensitive data.
- Read before updating; checkpoint after milestones, corrections, verification,
  decisions/blockers, before long operations, and when pausing or compaction is
  requested. Read back material writes. Recover the file before rebuilding the
  plan; reconcile it with the latest request and checkout. Do not overwrite
  another task or claim file edits provide atomic multi-writer coordination.
- Keep blocked, partial, interrupted, cancelled, or unverified task records.
  Before deleting a completed task file, verify requested outcomes/checks and
  write durable results to `<approved-outcome-location>`: what changed, why,
  acceptance/verification results, limitations, evidence links, and follow-ups.
  Record meaningful decisions using `<existing-decision-convention>`; do not
  force an ADR for trivial work or invent accepted decisions. Verify durable
  documentation by reading it back before removing the exact owned task file.
- Preserve unrelated records, ADRs, tests, and evidence. Confirm cleanup removed
  only the task record and the durable results remain. No commit, push, deployment,
  global policy change, or external action is authorized by this rule.
- The filesystem record is the canonical live plan for this project. ai-memory
  can complement historical retrieval; do not mirror transient progress into
  durable memory pages or use mid-session handoffs as a checkpoint. If records
  are local-only, they do not follow clones/worktrees. This rule installs no
  automatic hooks and cannot preserve work that was never written.
<!-- task-progress:end -->
```
