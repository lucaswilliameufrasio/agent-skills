---
name: postmortem
description: >-
  Write a blameless postmortem after an outage, failed deploy, or near miss,
  turning lessons into checks with owners. Use when asked for an incident
  report, RCA, or "what happened and how do we prevent it".
---

# Postmortem

A postmortem exists to make the next incident less likely or less harmful. It
is not a verdict on people. Systems that let a reasonable person make a costly
mistake are the thing to fix.

## Scope and audience

Confirm the incident, the audience (team, company, customers), and where the
document will live. Customer-facing summaries are a separate, shorter text
reviewed by the owner before publication (`comment-writing`). Do not publish or
send anything without authorization.

## Collect evidence before writing

Gather from logs, metrics, traces, alerts, deploy and change history, chat or
incident channel transcripts, tickets, and the people involved. Record each
source. Redact personal data, secrets, and customer identifiers in the
document; reference where restricted evidence lives instead of copying it.

## Write the document

Use the team's template if one exists. Otherwise:

1. **Summary.** Two or three sentences: what users experienced, for how long,
   and the current state.
2. **Impact.** Who and what was affected, measured: duration, error rate,
   requests or users affected, data lost or delayed, money, SLO budget used.
   Mark estimates as estimates.
3. **Timeline.** Timestamped in one stated time zone, from the first
   contributing change through detection, response, mitigation, and full
   recovery. Each entry cites evidence. Mark the key intervals: time to detect,
   to mitigate, to resolve.
4. **Root cause and contributing factors.** Trace why it happened and why it
   was not caught earlier, asking "why" until reaching conditions the team can
   change. Expect several contributing factors (a change, a missing check, a
   misleading alert, a runbook gap), not one person. Clearly separate confirmed
   facts from hypotheses still under investigation.
5. **Detection and response.** What alerted, what should have alerted sooner,
   what slowed mitigation (access, tooling, unclear ownership, missing
   rollback).
6. **What went well.** Practices worth keeping.
7. **Actions.** See below.

Use neutral language: describe actions and system states ("the deploy applied
the migration before the new version was healthy"), not people's failings.

## Turn lessons into checks

For each contributing factor, choose the cheapest layer that would have
prevented or caught it, using `agent-correction-tree`: redesign, automated
check, hook, verification, written runbook, and only last, "be more careful".
Common outputs: a regression test, an alert on the symptom users felt, a deploy
guard, a migration rule (`schema-migration-safety`), a restore drill
(`backup-restore-drills`), a runbook (`followable-guides`).

Every action has an owner, a priority, a due date or milestone, and a
verifiable completion criterion. File them in the team's tracker
(`jira-issue-writing` when the tracker is Jira) only with authorization, and
link them from the document. Prefer few, high-impact actions over a long list
nobody finishes.

## Review

Before sharing: every timeline entry has a source, impact numbers are measured
or labelled, no blame language, hypotheses are labelled, and each action is
specific and verifiable. Report open questions and what evidence would close
them.
