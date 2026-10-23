---
name: test-strategy
description: >-
  Compatibility entry point for testing-standard when selecting unit, integration,
  regression, mocking, or coverage boundaries. Read the canonical testing policy
  rather than maintaining a second set of rules.
---

# Test strategy compatibility

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
