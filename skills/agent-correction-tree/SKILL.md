---
name: agent-correction-tree
description: >-
  Turn a mistake made by an AI agent into the cheapest durable check that stops
  it from happening again. Use whenever an agent produced a bug, a bad pattern,
  a wrong guess, or skipped a step, whenever the user says "don't do that
  again", "remember this", "add a rule", or asks to update AGENTS.md, CLAUDE.md,
  a skill, or memory after a correction. Prefer redesign, lint/type/test,
  hooks, and real-app verification before writing prose; a written rule is the
  fallback, not the default.
---

# Agent correction tree

Every correction should become a check, not another line of instructions.
Instructions are read inconsistently, compete with each other, and grow until
agents ignore them. A check fails loudly every time, for every agent and person.

Fix the mistake itself first (with a regression test, per `testing-standard`),
then decide how to stop the next one.

## 0. Confirm whose mistake it was

Before choosing a layer, establish what actually went wrong:

- Reproduce or quote the faulty output and the instruction that produced it.
- If the request, spec, or existing rule was ambiguous or contradictory, the
  correction belongs there: clarify the source, do not add a rule that papers
  over it.
- If the agent followed an existing rule that is wrong or stale, change or
  delete that rule.
- If the mistake depends on one person's preference, it is a preference, not a
  project invariant: record it where that person's preferences live, not in a
  repository every contributor reads.

State the mistake as an invariant that a machine or a reviewer could check, for
example "product code must not import the database client directly", not "be
careful with the database".

## Walk the tree from the cheapest layer

Stop at the first layer that can catch the mistake reliably. Cost grows down the
list; trust shrinks.

1. **Redesign: make it impossible.** Change an API, type, module boundary, or
   default so the wrong thing cannot be expressed: a constructor that validates,
   a discriminated union instead of flags, an internal module that is not
   exported, a wrapper that owns the dangerous call. Use `untangle-codebase`,
   `single-state-enum`, or the repository's architecture guidance.
2. **Static check: make it fail fast.** A lint rule, a type, a compiler setting,
   a test, a schema validation, a CI check. Prefer the repository's existing
   linter and its custom-rule mechanism; give the rule an error message that
   says what to do instead. Then remove the existing occurrences, or record a
   tracked baseline when cleanup is out of scope. A rule that only warns is
   usually ignored.
3. **Hook: make it run without being remembered.** A pre-commit or pre-push
   hook, a harness hook on tool calls, or a generator that owns the output.
   Use this when the check exists but agents skip it. See `local-fast-gates`.
4. **Verification: make the agent prove it.** Drive the real application and
   capture evidence (screenshots, responses, persisted state). Use
   `create-verification-skill` when the project lacks a repeatable path, and
   `acceptance-traceability` to tie proof to the request.
5. **Written rule: when only judgment can catch it.** One clear line in the
   right place (see below). Name the trigger and the required action; drop the
   backstory.
6. **Human review: the last resort.** Name what the reviewer must look for and
   why no earlier layer could catch it. Ask whether a later layer could be
   built so the review stops being the bottleneck.

Combining layers is normal: a lint rule plus one line explaining the exception
process, or a redesign plus a regression test.

## Authorization and cost

Layers 1 to 3 change code, tooling, or team workflow. Propose them with the
blast radius (files touched, existing violations, CI time, contributor impact)
and ask before implementing a redesign or a repository-wide rule unless the
user already asked for it. Do not silently install hooks or global harness
settings. If the cheapest reliable layer is not approved, say which layer was
chosen instead and what it will not catch.

## Writing a rule well (layer 5)

Choose the narrowest durable owner:

| Scope of the invariant | Where it belongs |
| --- | --- |
| One repository or directory | That repository's `AGENTS.md`/`CLAUDE.md`, nearest to the code it governs |
| A reusable workflow across projects | A skill (update the existing owner; do not create a parallel one) |
| One person's preference | That person's memory or personal instructions |
| A decision with trade-offs | `document-decisions`, linked from the rule |

Before adding text:

- Search the target for an existing rule on the same topic; edit or replace it
  instead of appending a near-duplicate. Resolve contradictions explicitly.
- Write the trigger, the action, and, only if not obvious, the reason in one or
  two lines. Avoid "always/never" unless it is truly absolute.
- When a rule replaces an older one, delete the older one in the same change.
- If the file is long, propose pruning rules that a later layer now enforces.

## Corrections to skills

When the mistake came from a skill (it triggered wrongly, missed a step, or gave
stale guidance), first add an eval that reproduces the failure, then change the
skill, then confirm the eval passes. More prose without a failing case tends to
make skills longer without making them better.

## Report

State the mistake as an invariant, the layer chosen and why earlier layers were
rejected, what was changed (rule, lint, hook, test, text), existing violations
fixed or baselined, how the check was proven to fail on the bad pattern, and
anything that still depends on review.
