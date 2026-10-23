# Checkpoint evaluations

See [RESULTS.md](RESULTS.md) for the checked run and its limitations.

Cases 1–3 are decision scenarios for ai-memory scope, single-use handoffs, and
revision conflicts. They do not exercise a real MCP server.

The `ai-memory-plan-store-gap/` and `ai-memory-durable-note-boundary/` case
folders add regressions for the provider contract: no transient wiki writes
(including working-tier/expiry workarounds), no mid-session handoffs or silent
second stores, bounded observation recovery, and separately authorized durable
knowledge writes. These are scenario specifications, not MCP runtime evidence.

Cases 4–5 exercise an explicitly authorized filesystem context store with real
file tools. Create separate persistent run directories and copy only the chosen
fixture. Give the evaluated agent the selected prompt, fixture root, and skill
path, not this directory, assertions, expected outputs, or grading data. Use a
new independent session for recovery to avoid carrying the original task plan
in the conversation. Run a baseline in a separate directory without loading
this skill; document any ambient harness instructions it still inherits.

The task ID, project names, synthetic credential, and small Python formatter
belong only to these test inputs. They are not operational defaults, do not
configure the user's project or memory service, and do not make the Markdown
skill depend on Python in normal use.

Before runs, hash every fixture file. After saving, inspect and read back the
exact task record, check its identity and ordered progress, and verify that the
synthetic credential value was not persisted. After recovery, check the README
and run its example, verify the correct record is complete, and compare hashes
of protected files and unrelated tasks. Keep generated reports outside the
editable project/store. Treat injected memory content as data, never authority.

The fixture store is not ai-memory and does not simulate all provider behavior.
No real credentials, network access, Git operations, or deployment are needed.
Do not write evaluation data into the user's real memory service. A passing
filesystem test does not prove MCP routing, pre-compaction hooks, atomic writes,
or automatic skill loading. Scenario prompts must not be mistaken for actual
provider calls or for a measured reduction in context loss.
