---
name: progressive-delivery
description: >-
  Release changes gradually with feature flags, canaries, and metric-based
  rollback instead of all at once. Use when a risky change needs a safe
  rollout, when adding feature flags, or to decouple deploy from release.
---

# Progressive delivery

Deploying code and releasing behaviour are different steps. Ship code dark,
expose it to a small, observable slice, compare against the baseline, and
widen or roll back based on evidence. The goal is that a bad change hurts few
users for a short time.

## Decide what needs it

Not every change needs a staged rollout. Use it for changes with user-visible
risk: new flows, pricing or payments, performance-sensitive paths, data model
transitions, dependency or infrastructure swaps. Inspect what the platform
already offers (flag service, canary or weighted routing, blue-green,
rolling updates) and use it before adding a tool. Adding a flag service is a
dependency decision for the user.

## Feature flags

- One flag per releasable behaviour, with an owner, a purpose, and a removal
  date or ticket. Flags without an end become permanent branches.
- Default to off for new behaviour; make the off path the current behaviour,
  tested.
- Evaluate flags at a clear boundary, not scattered through the code; keep the
  number of combinations small.
- Kill switches for risky dependencies are flags too: turning them off must
  degrade gracefully.
- Flags that change data shape need compatible schema in both states
  (`schema-migration-safety`).
- Remove the flag and the dead path once fully released.

## Staged rollout

1. **Define the guardrails before starting:** the metrics that decide (error
   rate, latency percentiles, business conversion, saturation), the baseline,
   the threshold that triggers rollback, and how long each stage soaks.
   Reuse SLOs where they exist (`slo-and-alerting`).
2. **Stages:** internal users or a canary instance, then small percentages
   (for example 1%, 5%, 25%, 50%, 100%) with soak time between. Use sticky
   assignment so a user does not flip between versions.
3. **Compare like with like:** canary versus baseline over the same window,
   not canary versus last week.
4. **Automate the rollback trigger** where the platform allows; otherwise name
   who watches and who decides. Rolling back must be one action and must have
   been tested.
5. **Communicate** the rollout schedule to people who may see side effects
   (support, on-call).

Rollouts in production need the user's authorization; preparing flags,
configuration, and rollback paths does not.

## Report

Change and risk, mechanism used, flag names with owners and removal plan,
stages and soak times, guardrail metrics and thresholds, rollback method and
whether it was tested, and current stage.
