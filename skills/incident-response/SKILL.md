---
name: incident-response
description: >-
  Guide the response while a production incident is happening: stabilize
  first, coordinate, communicate, and keep a timeline. Use whenever the user
  says production is down, broken, slow, losing data, under attack, or a deploy
  just went wrong, or asks "what do we do now". Prefer reversible mitigation
  (rollback, flag off, failover, shed load) over live debugging, never take
  destructive or outward-facing actions without explicit approval, and hand
  off to postmortem afterwards.
---

# Incident response

During an incident the goal is to stop user harm, not to find the root cause.
Mitigate with the smallest reversible action that restores service, then
investigate with the pressure off. Calm, explicit communication is part of the
fix.

## First minutes

1. **Assess impact.** What are users experiencing, how many, since when, and is
   it getting worse? Check SLO dashboards, error rates, recent alerts. Declare
   a severity using the team's scale if it has one.
2. **Find what changed.** Recent deploys, config or flag changes, migrations,
   infrastructure changes, dependency status pages, traffic shifts. Most
   incidents follow a change.
3. **Start the timeline.** Record timestamped observations and actions in one
   place (incident channel, document, ticket) from the start, in one time zone.
   The `postmortem` depends on it.
4. **Roles.** Even with two people, separate who coordinates and communicates
   from who operates. As an agent, act as operator or scribe as asked; the
   human incident lead decides.

## Mitigate before diagnosing

Prefer, in roughly this order, what is reversible and fast:

- roll back the most recent change (deploy, config, flag) when timing
  correlates, even without proof it is the cause;
- turn off a feature flag or degrade a non-critical feature;
- fail over to a healthy region, replica, or provider;
- shed or rate-limit load, block abusive traffic;
- scale out when saturation is confirmed.

State the expected effect of each action before taking it and check the effect
afterwards. Change one thing at a time so effects are attributable.

**Approval.** Production changes during an incident still need authorization.
Propose the exact command and its blast radius and wait for an explicit yes
unless the user or runbook has already authorized that specific action.
Destructive actions (data deletion, restores over live data, killing stateful
nodes, rotating credentials that break consumers) always need explicit
approval. A rollback that includes an irreversible migration is not a simple
rollback; check first (`schema-migration-safety`).

**Security incidents.** Preserve evidence (logs, snapshots) before changing
compromised systems; revoke exposed credentials (`secrets-safety`,
`credential-lifecycle-and-rotation`); involve the people responsible for
security and legal obligations.

## Communicate

- Post updates at a regular interval (for example every 30 minutes for a major
  incident) even if nothing changed: impact, current action, next update time.
- Internal updates can be technical; customer-facing updates state impact and
  workarounds in plain language and are sent only by or with approval of the
  owner (`comment-writing`).
- Do not speculate about cause publicly.

## Investigate safely

With service stable, narrow the cause using read-only access first: logs,
metrics, traces, recent diffs, then reproduce and test one hypothesis at a time. Avoid running
heavy queries against a struggling database or restarting things to "see what
happens".

## Close

Declare resolution when user-facing metrics have recovered and held for an
agreed time, not when the fix is merged. Note any temporary mitigations still
in place (flags off, extra capacity, blocked traffic) with owners to undo them.
Then hand off to `postmortem` with the timeline.

## Report during and after

Current impact and severity, actions taken with time and effect, actions
proposed awaiting approval, temporary mitigations to undo, open questions, and
the timeline location.
