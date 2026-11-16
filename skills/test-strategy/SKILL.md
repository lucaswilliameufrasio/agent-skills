---
name: test-strategy
description: >-
  Deprecated alias kept for existing callers until 2027-02-16; prefer
  testing-standard. Loads that canonical policy and keeps no rules of its own.
---

# Test strategy compatibility

> **Deprecated.** Removal planned for 2027-02-16; see
> [deprecations](../../docs/deprecations.md). Use `testing-standard` directly.

Read and apply [`testing-standard`](../testing-standard/SKILL.md), using the
skill loader or the sibling file. Install it alongside this entry point. If it
is unavailable, report that limitation before claiming verification.

It owns real local integration dependencies, external protocol fakes, regression
coverage, safe isolation, coverage exclusions, and the full repository gate.
Follow actual repository names and configuration; do not rename dependencies
or modify unrelated services as a side effect of testing.

If an installed user-owned `references/local-conventions.md` exists, read it
for compatible naming conventions. Preserve it privately during updates; it
does not replace repository facts or the canonical testing policy.

## Migrate `local-conventions.md` before removal

If `references/local-conventions.md` exists next to this skill, tell the user
once per session, before relying on it, that this alias will be removed on
2027-02-16 and the canonical skills do not read that file. Offer to migrate it:
show its contents (redacting any secret), propose where each convention
belongs (the user's personal agent instructions or memory for personal
preferences, the repository's `AGENTS.md` for project rules), and write only
after the user approves. Then tell the user the alias can be uninstalled. Do
not delete or edit the file without approval, and do not repeat the offer in
the same session after the user declines.
