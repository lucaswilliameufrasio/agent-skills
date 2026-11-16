---
name: quality-gate
description: >-
  Deprecated alias kept for existing callers until 2027-02-16; prefer
  testing-standard and task-completion. Loads that canonical policy and keeps no rules of its own.
---

# Quality gate compatibility

> **Deprecated.** Removal planned for 2027-02-16; see
> [deprecations](../../docs/deprecations.md). Use `testing-standard`, `task-completion` directly.

Read and apply [`testing-standard`](../testing-standard/SKILL.md), using the
skill loader or the sibling file. If unavailable, report the missing dependency;
do not claim the required checks passed. Install that skill alongside this one.

That policy owns test boundaries, safe local dependencies, fresh whole-repository
checks for every repository touched, and failure reporting. Use each repository's
verified commands rather than assuming Go or a particular database. Report
pre-existing failures without hiding them, waiving required checks, or silently
expanding the task to unrelated repairs.

Use [`task-completion`](../task-completion/SKILL.md) for the delivery state and
next action. Do not maintain another checklist here.
