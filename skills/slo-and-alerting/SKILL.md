---
name: slo-and-alerting
description: >-
  Define SLIs and SLOs from user journeys and replace noisy CPU/memory alerts
  with burn-rate pages that link runbooks. Use for SLOs, error budgets, alert
  rules, or too many alerts.
---

# SLOs and alerting

Alert on symptoms users feel, measured against an explicit objective, with
urgency proportional to how fast the objective is being spent. CPU at 90% is a
cause to investigate, not a reason to wake someone; checkout failing for 5% of
users is.

## Start from user journeys

List the journeys that matter (sign in, search, pay, upload, receive a
notification, an API consumer's key calls, a batch finishing on time) and who
depends on them. For each, ask what "working" means to that user: it responds,
fast enough, correctly, and data is fresh enough. Use
`system-module-architecture` if journeys are not documented.

## Choose SLIs

An SLI is a ratio of good events to valid events, measured as close to the user
as practical (load balancer or gateway, client telemetry, synthetic probes),
not on a single host.

| Journey type | Typical SLIs |
| --- | --- |
| Request/response | Availability (non-error responses / valid requests), latency (requests under a threshold / valid requests) |
| Pipeline or batch | Freshness (data updated within N), completion by deadline, correctness checks |
| Queue/async | Age of oldest message, processed within N |
| Storage | Durability, read-after-write success |

Define precisely what counts as valid (exclude health checks, clients' own
4xx errors where appropriate) and good. Inspect what the monitoring stack
already records; add instrumentation only where the SLI cannot be computed
(follow the monitoring stack's current documentation).

## Set SLOs and error budgets

- Pick a target and a window (for example 99.5% over 28 days) from current
  measured performance and what users need, not from aspiration. A target
  stricter than the dependencies' reliability is not achievable.
- The error budget is `1 - SLO` of valid events in the window. Write down what
  happens when it is exhausted (release freeze for risky changes, reliability
  work prioritised) and who decides. The policy is the user's or team's
  decision; propose, do not impose.
- Start with few SLOs per service. Review them after a few windows.

## Alert on burn rate

Page when the budget is being consumed fast enough to exhaust it soon, using
multiple windows so alerts are both fast and not noisy: a short window to
detect quickly and a longer one to confirm it is sustained. A common starting
point, to be tuned to the service's traffic:

| Severity | Burn rate | Windows (long / short) | Budget consumed if sustained |
| --- | --- | --- | --- |
| Page | 14.4x | 1 h / 5 min | 2% in 1 hour |
| Page | 6x | 6 h / 30 min | 5% in 6 hours |
| Ticket | 1x | 3 days / 6 h | 10% in 3 days |

For low-traffic services, burn-rate alerts become noisy; add synthetic traffic
or use minimum event counts. Verify the alert expressions against the
monitoring stack's current query language.

## Clean up existing alerts

Inventory current alerts with their firing history. For each: what user
impact does it predict, what action does the responder take, how often did it
fire and was it actionable? Then:

- keep symptom alerts that map to an SLO; replace them with burn-rate alerts
  where possible;
- downgrade cause alerts (CPU, memory, disk, queue depth) to tickets or
  dashboards unless they predict imminent user impact that the SLO alerts would
  catch too late (disk full in hours is a valid page);
- delete alerts nobody acts on, after the owner agrees;
- every page links a runbook (`followable-guides`) with first checks and
  mitigations, and names an owner.

## Verify

Replay historical data or inject a controlled failure in a non-production
environment to confirm each page fires within the expected time and recovers.
Confirm notification routing reaches the right people. Report expected page
volume per week from historical data.

## Report

Journeys, SLIs with exact definitions and queries, SLOs and windows with the
measured baseline, error budget policy proposed, alerts added/changed/removed
with reasons, runbook links, verification results, and expected page volume.
