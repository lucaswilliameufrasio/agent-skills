---
name: testing-quality-gate
description: >-
  Compatibility entry point for testing-standard. Use when adding or reviewing
  tests, fixing bugs, changing persistence or APIs, or finishing a code change.
  Load testing-standard for the canonical test boundaries, regression coverage,
  safe local infrastructure, and full repository quality gate.
---

# Testing strategy and quality gate

This entry point is retained for existing callers. The canonical policy is
[`testing-standard`](../testing-standard/SKILL.md); read and apply that skill
before planning tests or verifying a change. Use the harness's skill loader
when available, or read the sibling file directly. If neither is accessible,
report the missing policy instead of claiming that its gate was verified.

Do not keep a separate checklist or infer commands here. Repository-specific
instructions supply the actual checks, dependencies, and approved exceptions.
Report which checks passed, failed, or did not run, and never imply that a
partial test run proves the full change is complete.
