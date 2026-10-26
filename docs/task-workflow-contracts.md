# Acceptance and task-progress contracts

## Purpose and decisions

Two separate capabilities complement the existing workflow:

1. `acceptance-traceability` maps the latest requested outcomes to implementation,
   actual verification, gaps, and evidence. It does not own test policy, execute
   all tests automatically, or grant product sign-off.
2. `install-task-progress` installs a self-contained project instruction rule for
   filesystem live plans and durable closeout. Installation of the skill alone
   does not change AGENTS.md in any repository. Applying the rule requires a
   named target and preserves its current rules and memory routing.

The selected contract keeps one live file per task/worktree at the approved
location (default proposal: `.agent-tasks/<unique-task-id>.md`). It is updated at
material milestones and read before recovery. The whole current plan is not
duplicated into ai-memory pages. ai-memory remains useful for historical lookup;
its observations and single-use end-of-session handoffs are not the canonical
current task state. This is an explicit choice of file storage, not a silent
fallback whenever memory retrieval is inconvenient.

Completed records are removed only after requested outcomes and checks are
verified, durable results/rationale/evidence pointers are written and read back,
and substantive decisions are preserved in the existing ADR/design convention.
Blocked, interrupted, partial, unverified, or cancelled tasks keep their recovery
state unless their disposition is separately authorized. Cleanup affects only
the exact owned file; it does not delete evidence, other tasks, or decision history.

Local-only transient files avoid committing noisy partial work, but do not move
between machines/clones/worktrees and cannot recover unwritten progress. Projects
may instead select versioned files with explicit sharing/history implications.
Neither option supplies automatic compaction callbacks or atomic multi-writer
coordination. A single global task file was rejected because simultaneous tasks
could overwrite one another. Mandatory ADRs for every task were rejected because
they dilute meaningful decision history. Installing the rule globally or
rewriting third-party memory policy is outside these skills' default scope.

This feature note records the policy boundaries; no existing ADR convention is
present in this collection, so an invented numbered ADR is not needed. A target
repository's actual architectural decisions still belong in its own convention.

## Ownership and integration

| Capability | Owner |
| --- | --- |
| Requirement → observable proof | `acceptance-traceability` |
| Running real app journeys | Project verifier authored with `create-verification-skill` |
| Execution and honest completion | `task-completion` |
| Test boundaries and repository quality gates | `testing-standard` |
| Checkpoint payload and recovery | `context-checkpoint` |
| Installing file-store lifecycle in AGENTS.md | `install-task-progress` |
| Substantive decision rationale | `document-decisions` |

`context-checkpoint` and `task-completion` now explicitly acknowledge a selected
transient-file lifecycle without making it mandatory in every project. The
installer embeds the minimum rule in AGENTS.md so future agents do not require
access to a particular skill installation to understand it.

## Validation and maintenance

Synthetic scenarios cover acceptance of incomplete work, scope changes,
idempotent rule installation, scoped completed-record removal with protected
blocked work, and refusal to remove an unverified task. See the evaluations and
results under both skills. Raw sandbox outputs, visible traces, and the HTML
review stay outside this public checkout; fixture content is synthetic.

Five paired GPT-6 Luna scenarios produced 15/15 criteria with skills versus
12/15 in baselines: acceptance 6/6 versus 5/6, progress 9/9 versus 7/9. These are
single samples with ambient harness policies, not proof of a statistically
reliable advantage. Separate model grading covered four cases; the blocked
case received parent review. Installed-copy and schema checks complement, not
replace, behavior checks. No human review is implied by generating the viewer.

No application code, production resources, real user data, automatic hooks,
third-party skill files, or other repositories' instructions are changed by
this delivery. There is no root app build/lint/unit runner in this collection;
quality checks validate skill YAML, Markdown reference paths, new case schemas,
shell scaffold syntax, fixture behavior, diffs, and installed-file equality.

Revisit the contract when a supported active-task provider is deliberately
chosen, cross-machine recovery is required, multi-writer ownership changes, or
the target repository's durable-documentation convention changes. Do not change
the live source of truth implicitly during a resumed task.

## Delivery record — 2026-10-26

| Requested outcome | Result and evidence |
| --- | --- |
| Reusable acceptance skill | Added skill and compact acceptance-map reference; two paired scenarios scored 6/6 with skill. |
| Installer for task progress and durable closeout | Added skill, self-contained AGENTS.md block and task template; three paired scenarios scored 9/9 with skill. |
| Avoid competing checkpoint/decision/completion policies | Added explicit filesystem guidance to context-checkpoint and a closeout bridge to task-completion; decision rationale remains owned by document-decisions. |
| Skills ready for local use | New skill bodies/references installed globally; compatible checkpoint/completion bodies synchronized only after verifying no local drift and privately backing up previous copies. Installed files compared equal. |
| Inspectable validation | Five case schemas and shell scaffolds validated; all 42 top-level skill frontmatter files checked; local skill/reference links, whitespace, privacy scan, and git diff checks passed. Static review generated outside the checkout. |

The only transient record for implementing these skills is removed after reading
back this delivery record and checking retained results. Evaluation fixtures and
protected blocked records are not cleanup targets. The documentation and test
artifacts remain available after the implementation note is gone. No required
skill-creation work remains; human review/trigger tuning and applying the rule
to a specific real repository are separate optional actions, not silently
performed installations. Commit and push are separate, explicitly authorized
delivery actions; installing these skills does not grant that authorization.
