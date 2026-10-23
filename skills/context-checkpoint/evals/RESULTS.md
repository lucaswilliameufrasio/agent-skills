# Filesystem checkpoint evaluation — 2026-10-23

## Provider-contract supersession

The ai-memory adapter was subsequently corrected against the official 3.2.2
durable-page contract: transient active plans must not use `memory_write_page`
or mid-session handoffs. The results below remain historical filesystem-only
evidence from before that correction, not a rerun of the revised skill or
validation of its former wiki-write advice. Updated decision scenarios and new
provider-contract regression cases are specifications, not executed MCP tests.

Local checks after the correction passed: skill frontmatter, five legacy
scenario records, both new scenario folders and their grader schemas, local
Markdown links, and whitespace checks. The unchanged recovery fixture's
`python3 -m unittest discover -s tests -v` passed one test; a direct formatter
example returned `Hello, Ada!`. These are structural/fixture health checks, not
new model evaluations, end-to-end save/recovery runs, or MCP runtime evidence.

## Prior filesystem runs

Four independent sessions exercised saving a checkpoint and recovering work
after a context gap, with one with-skill and one baseline run per case. Evaluated
agents received only the prompt and isolated fixture, not grading expectations.

| Case | With skill | Baseline | Independently checked evidence |
| --- | --- | --- | --- |
| Scoped save | 4/4 | 4/4 | Only the authorized task record created; identity, plan, pending checks and next action preserved; synthetic credential excluded. |
| Cold recovery | 4/4 | 4/4 | Only README and correct task record updated; example runs, one-test suite passes; protected files and newer unrelated record unchanged. |
| **Total** | **8/8** | **8/8** | **No demonstrated incremental benefit in this sample.** |

Save responses reported the exact record pointer and full read-back. Independent
recovery sessions read existing context, completed the documentation task,
rejected instruction-like historical content, and updated/read-verified the
matching task without asking the user to restate its plan.

## Limits

- The store was an explicitly authorized filesystem fixture, not ai-memory MCP.
- Provider-specific scope, single-use handoff, and conflict cases are evaluation
  specifications; no real MCP write or handoff consumption was performed.
- Cold independent sessions approximate loss of conversational context; no real
  automatic compaction event, hook, crash recovery, or automatic loading was
  tested.
- Baselines retained ambient harness instructions and available skill metadata.
  They were instructed not to load this skill or workflows delegating to it.
- Logs were agent-authored; evaluator checks independently establish artifacts,
  hashes, current tests and examples, not every historical tool call.
- One run per variant/case is not a reliability estimate. Per-run timing/token
  data was unavailable and was not invented.

The tests establish correct behavior in these examples, not guaranteed context
retention across all harnesses or improved reliability relative to the baseline.

## Subsequent provider-contract regression checks

The ai-memory guidance was corrected after auditing the upstream durable-page
contract: transient plans must not default to `memory_write_page`, and an ending
handoff is not a mid-session checkpoint. The correction also distinguishes a
missing storage operation from missing harness automation; a selected remote
provider is not to be replaced automatically or repeatedly questioned.

An independent skill-loaded decision check covered unknown static-client scope
and an already-working remote store with missing automatic progress updates.
Both responses respected scope, retained the chosen provider, rejected improper
wiki/handoff workarounds, and did not claim actions had run. These were decision
checks, not provider writes or comparative effectiveness measurements.

## Native integration smoke checks

Separately from the filesystem fixtures, native integrations were exercised
with ai-memory CLI 3.2.2 and an existing server identifying as 2.4.0:

- OpenCode 2.1.4: the generated V2 plugin was active; a real isolated session was
  compacted and correctly recalled its pending action afterward. The server's
  raw observations confirmed the `pre-compact` lifecycle event.
- Claude Code 2.1.309: actual SessionStart, UserPromptSubmit, Stop and SessionEnd
  events were confirmed on the server. Explicit local routing aligned its
  project scope with the other client without moving historical records.
- A new OpenCode session automatically recovered the handoff produced by that
  Claude session and identified the prior verification without the fact being
  repeated in its prompt.
- The native doctor command succeeded after correcting the local client
  connection. No remote server upgrade was performed.
- Codex 0.162.1 registrations were installed, but all seven hooks remained
  untrusted pending the user's native `/hooks` review; execution was not claimed.
  Kiro was unavailable locally and was not tested.

These checks validate lifecycle delivery and limited continuity, not automatic
semantic tracking of every plan step, a synchronous pre-compaction persistence
barrier, or a new active-task storage API. No synthetic fixture context was
written to the real MCP wiki. Private endpoints, credentials, task identifiers
and raw diagnostic logs are deliberately excluded from this report.
