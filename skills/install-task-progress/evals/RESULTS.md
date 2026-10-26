# Task-progress contract results

2026-10-26: three synthetic cases with one execution per condition using
`openai/gpt-6-luna` in independent OpenCode child sessions. Baselines were told
not to load the new skill but retained ambient harness instructions. A separate
Luna grader assessed the initial two cases from final artifacts and visible tool
traces; the parent reviewed the additional blocked case against its three
criteria. This is not a blinded or statistically conclusive benchmark.

| Case | With skill | Baseline |
| --- | ---: | ---: |
| Install / preserve / reapply | 3/3 | 1/3 |
| Resume / promote / exact cleanup | 3/3 | 3/3 |
| Retain unverified blocked task | 3/3 | 3/3 |
| **Total criteria** | **9/9** | **7/9** |

## Observed differences and mechanical checks

Both installation traces contain actual repeated applications and comparisons.
The with-skill AGENTS.md block includes identity/worktree separation, recovery,
retention, read-back before completed-file removal, and evidence preservation.
The baseline omits these closeout/ownership protections and the file portability
and automatic-hook limitations required by the rubric.

The baseline also added `.agent-tasks/  # local-only task progress` to
`.gitignore`. A real read-only ignore check using an existing Git directory with
the fixture as worktree confirmed the pattern does not ignore task files; the
with-skill pattern does. The grader's initial check without a Git directory could
not run; this parent mechanical check supplies the actual ignore evidence.
The final skill explicitly warns about inline comments and rooted ignore scope.

In both closeout conditions, SHA-256 comparisons confirmed the unrelated blocked
record, existing decision history, instructions, and check evidence stayed
byte-identical. Only the intended completed record disappeared and a durable
outcome remained. Visible traces show durable read-back before removal. In the
additional blocked scenario both conditions retained the live record and did
not fabricate a successful export. Creating a clearly partial durable note in
the baseline is not itself a failure.

## Limits

The cases exercise real local file writes/reads/deletion, not a real application,
provider, interruption, automatic compaction, symlink attack, failed disk write,
malformed-marker repair, cross-machine recovery, or true concurrent writers.
The installer deliberately installs no hooks and changes no global instructions.
No root application build/lint/unit suite exists for this Markdown collection;
skill/case schemas, reference links, whitespace, shell scaffolds, preservation
hashes, and installed-copy equality are checked separately.

Raw sandbox artifacts, visible traces, usage metadata, and the generated static
review are outside this public checkout. Execution and grading used the same
model family; parent review is not independent. No human review or reliable
automatic activation has been measured. Do not generalize a single-sample
15/15 versus 12/15 combined score to all future tasks.
