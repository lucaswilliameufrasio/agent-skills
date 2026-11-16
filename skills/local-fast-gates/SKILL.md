---
name: local-fast-gates
description: >-
  Add or tune fast local checks (pre-commit or pre-push hooks) that run format,
  lint, typecheck, and quick tests on changed files before code reaches CI.
  Use when CI keeps failing on format or lint, when agents or people skip
  documented checks, when the user asks for git hooks, or when a rule in
  AGENTS.md should become enforcement. Reuse the repository's existing hook
  manager and commands; keep the hook fast and never replace CI.
---

# Local fast gates

A hook catches what people and agents forget, at the moment it is cheapest to
fix. It is a convenience layer in front of CI, not a replacement: hooks can be
bypassed, and CI stays the gate.

## Inspect before installing

Read repository instructions, CI workflows, task runners, package scripts, and
any existing hook setup: a hook manager configuration, a committed hooks
directory with `core.hooksPath`, or framework-specific hooks. Find the exact
format, lint, typecheck, and test commands CI runs.

- If a hook manager exists, extend its configuration.
- If none exists, propose one that fits the stack and is already common in it,
  or a plain committed hooks directory wired through `core.hooksPath` with a
  documented setup command. Choosing a new dependency is the user's decision.
- Do not install global hooks or change global Git configuration.
- Do not overwrite hooks a developer created locally; detect and report them.

## Design for speed

Set a budget (seconds, typically under 10 for pre-push on a typical change) and
measure it.

- Run on **changed files** relative to the upstream or merge base, not the
  whole repository, for tools that work per file (format, lint).
- Typecheck incrementally when the tool supports it; otherwise only the
  affected packages.
- Run fast, focused tests only (unit tests for touched modules) if they fit the
  budget; the full suite belongs in CI.
- Run independent checks in parallel.
- Choose the stage: formatting and lint at pre-commit (or auto-fix and restage
  only if the team agrees), typecheck and quick tests at pre-push.
- Fail with an actionable message that names the command to fix it.

## Stay consistent with CI

Hooks must call the same commands and configuration CI uses (through the same
scripts or task runner), so local green predicts CI green. Hooks must not
require secrets, network services, or production configuration.

## Agents and bypass

Agents skip steps written as instructions; a hook runs regardless. Repository
instructions should say that hook failures must be fixed, not bypassed with
`--no-verify` or equivalent, unless the user explicitly asks. If a hook is too
slow or wrong, fix the hook. Keep the AGENTS.md entry to one line pointing at
the setup command, and remove rules the hook now enforces
(`agent-correction-tree`).

## Verify

Introduce a deliberate format error, lint violation, and type error in a
scratch change; confirm each is caught with a clear message and that a clean
change passes. Measure the time on a typical change and on a large one.
Confirm the setup works on a fresh clone with the documented command. Revert
the scratch changes.

Report the hook manager, stages and commands, measured time, the setup command
for contributors, and what remains CI-only.
