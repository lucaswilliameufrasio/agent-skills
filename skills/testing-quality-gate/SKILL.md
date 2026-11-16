---
name: testing-quality-gate
description: >-
  Deprecated alias kept for existing callers until 2027-02-16; prefer
  testing-standard. Loads that canonical policy and keeps no rules of its own.
---

# Testing strategy and quality gate

> **Deprecated.** Removal planned for 2027-02-16; see
> [deprecations](../../docs/deprecations.md). Use `testing-standard` directly.

This entry point is retained for existing callers. The canonical policy is
[`testing-standard`](../testing-standard/SKILL.md); read and apply that skill
before planning tests or verifying a change. Use the harness's skill loader
when available, or read the sibling file directly. If neither is accessible,
report the missing policy instead of claiming that its gate was verified.

Do not keep a separate checklist or infer commands here. Repository-specific
instructions supply the actual checks, dependencies, and approved exceptions.
Report which checks passed, failed, or did not run, and never imply that a
partial test run proves the full change is complete.
