# Evaluating task completion

`evals.json` contains prompts **and grading data**. Do not give that file to an
evaluated agent. Cases 1–5 test decisions and handoffs only; cases 6–8 use the
local fixtures below and require actual tools and artifact inspection.

See [RESULTS.md](RESULTS.md) for the latest checked run and its limitations.

## Run without answer leakage

1. Create an isolated persistent workspace for each case and variant. Copy only
   that case's fixture contents into it. Do not use the source fixture directly,
   share mutable files between variants, or put checkouts in temporary storage.
2. Extract only the selected `prompt` string for the evaluated agent. Keep
   `expected_output`, `assertions`, other runs, and grading tools out of its
   supplied context. Do not ask it to read this evaluation directory.
3. For `with_skill`, provide the `task-completion/SKILL.md` path explicitly.
   For `without_skill`, do not provide or load that skill or a workflow that
   delegates to it. Record any ambient harness instructions or skill metadata
   that cannot be removed; this is not a clean-room baseline in that case.
4. Launch independent sessions per case and variant. Keep tool transcripts,
   before/after file hashes, command results, and final responses outside the
   editable fixture. Never fabricate missing timing or transcript data.
5. Grade against the evaluator-only assertions and actual artifacts. For case 6,
   execute the fixture suite and independently check CSV round trips with commas,
   quotes, newlines, and empty input. Confirm a regression test and usage docs
   were added. For case 7, compare every fixture file before/after. For case 8,
   confirm the owned preflight file is unchanged, still fails with exit code 2,
   documentation was completed, and the final report does not claim a green gate.
6. Report baseline results alongside with-skill results. A tie does not establish
   an improvement. Repeated independent runs and user review are needed before
   stronger conclusions; these fixtures do not measure runtime stop enforcement
   or automatic skill activation.

## Fixtures

| Case | Directory | Purpose |
| --- | --- | --- |
| 6 | `fixtures/csv-export` | A deliberately incomplete CSV exporter, missing regression and usage documentation. |
| 7 | `fixtures/read-only-audit` | Conflicting synthetic policies; audit only, no edits. |
| 8 | `fixtures/blocked-check` | A controlled local preflight failure with independent documentation still possible. |

The failure in case 8 is a synthetic unavailable prerequisite, not a real
database integration test. Do not install infrastructure, contact external
services, or repair the intentionally failing preflight to make it pass.
Fixture code intentionally contains defects; it is test input, not a production
example. No Git initialization, commit, push, or deployment is needed.

## Collection checks

Validate all skill frontmatter, JSON files, Markdown links, and whitespace after
changes. Syntax-compile fixture Python without treating the intentional case 8
failure as a collection defect. Case 6's initial suite should pass, but its
CSV edge cases should fail until an evaluated agent fixes the implementation.
For new or changed entry points, also check that every referenced dependency
exists and delegates to a single policy rather than copying it.
