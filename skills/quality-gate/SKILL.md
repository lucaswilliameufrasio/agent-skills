---
name: quality-gate
description: >-
  Compatibility entry point for testing-standard when finishing an implementation,
  preparing a commit, or verifying that a repository is green. Load the canonical
  policy instead of applying a separate language-specific quality checklist.
---

# Quality gate compatibility

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
