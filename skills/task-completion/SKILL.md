---
name: task-completion
description: >-
  Carry an authorized task through execution, verification, and an honest handoff.
  Use whenever implementing or fixing something, executing a multi-step request,
  resuming unfinished work, or preparing a final delivery report, even when the
  user does not explicitly ask for a checklist or next steps. Prevent premature
  stopping, plan-only delivery, hidden omissions, and vague follow-up offers.
---

# Task completion

An answer is not a substitute for an authorized action, and passing checks are
not proof that every requested outcome was delivered. Track both the request
and the evidence so the user does not have to discover unfinished work.

## Establish the completion contract

Extract the requested outcomes, constraints, and authorization from the current
conversation and applicable repository instructions. Keep a short checklist for
multi-step work, using the harness's task list if available or ordinary notes if
not. A one-step task does not need a ceremonial plan.

When the user has authorized persistent context, read and apply
[`context-checkpoint`](../context-checkpoint/SKILL.md) using the skill loader or
sibling file. Recover its scoped active plan before rebuilding it, and persist
material progress and corrections with verification. A volatile task list alone
does not establish that the plan will survive compaction. Report an unavailable
dependency or memory store rather than claiming recovery coverage.

Distinguish implementation, validation, documentation, and delivery steps only
when they apply. A request to investigate or propose a plan is complete with
findings or a plan; it does not authorize implementation. A request to implement
is not complete with a proposal alone.

Record each required item as pending, in progress, verified, or blocked. After
user steering or context compaction, reconcile the remaining work against the
latest request rather than silently dropping earlier requirements. Respect
explicit cancellations and scope reductions.

## Execute instead of offering to execute

Continue with the next safe, necessary, already-authorized action until the
requested outcomes are verified or a concrete blocker prevents further work.
Do not end with “I can add the tests next” when those tests are part of the
authorized implementation. Do not ask the user to perform available checks that
you can safely run yourself.

Use reasonable, reversible assumptions within the established scope. Ask only
when a missing decision materially affects correctness, scope, ownership, risk,
or authorization. Do not repeatedly request approval already given for the
same action and scope.

Persistence is not permission to expand the task. Preserve unrelated changes;
do not bypass permissions or invent approval for commits, pushes, publishing,
deployments, destructive operations, or external side effects. Follow the
actual authorization and higher-priority safety rules, not a workflow's implied
next step.

## Verify outcomes, not just activity

Before finalizing, compare the actual result with every checklist item. Inspect
the final artifacts or diff, check that related pieces are connected, and
identify placeholders, omitted requirements, or unfinished wiring. Report only
actions actually performed and outcomes supported by evidence.

For code changes, use `testing-standard` for the repository's full applicable
quality gate; do not maintain a second testing policy here. For other tasks,
use the relevant domain checks, such as reading back a saved artifact or
checking that a requested record exists. Do not claim that unrun checks passed.

Fix failures introduced by the work and rerun affected checks. Treat unrelated
pre-existing failures according to the repository's policy: report them, retain
an unverified status when they block a required gate, and do not silently turn
the task into unrelated repair work.

## Handle blockers without disappearing

When a command fails, diagnose the cause and try a bounded, safe alternative
when one exists. Do not repeat the same failing action without new information,
retry indefinitely, or weaken checks to manufacture success.

Complete independent authorized items that remain useful and safe. Do not
perform dependent actions on an unverified foundation. When progress genuinely
requires credentials, unavailable infrastructure, a product decision, or new
permission, state the blocker and the smallest concrete action to unblock it.
Identify who needs to act: the agent, the user, or an external owner.

Respect user cancellation and tool limits. If interrupted or approaching a hard
execution limit, leave a concise checkpoint of completed work, pending items,
validation evidence, and the next action. A checkpoint is not completion and
does not authorize automatic restart after a cancellation.

## Close with a useful handoff

Keep the final response proportional to the task and in the user's language.
Make the delivery state unambiguous, without requiring a rigid template:

- **Complete:** all requested outcomes and applicable required checks are
  verified. Summarize the result and evidence. Say there is no required next
  step when that helps; do not invent follow-up work.
- **Partial:** some requested outcomes are delivered, but required work or
  verification remains. List the missing items and why they remain. Do not use
  “done” or “all green” to describe the overall task.
- **Blocked:** no further useful authorized progress is possible. State the
  specific blocker, what was preserved or completed, and the next action with
  its owner. A partial delivery can also have a blocked remainder.

Separate **required remaining work** from **optional improvements**. Required
work that the agent can still execute is a reason to continue, not a suggestion
for a future turn. For work requiring new authorization, name the exact action
and boundary instead of ending with a generic “want me to continue?”

## Portability boundary

This is a behavioral workflow, not a scheduler, stop hook, or permission grant.
It uses no harness-specific API and does not guarantee automatic activation or
prevent the runtime from stopping. Install or invocation mechanisms remain the
responsibility of each harness; do not introduce global configuration merely
to apply this skill.
