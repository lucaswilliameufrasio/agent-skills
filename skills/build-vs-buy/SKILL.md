---
name: build-vs-buy
description: >-
  Decide whether to build a capability, buy a managed service, or adopt open
  source, comparing total cost, lock-in, risk, and exit. Use when choosing a
  vendor, a hosted service, a runner provider, or whether to write it yourself.
---

# Build vs buy

The question is not which option is cheapest this month, but which gives the
needed capability at acceptable total cost and risk, with a way out. Decide
from requirements and evidence, not from vendor pages or habit.

## Define the need

Write the requirements before looking at options: functional needs, scale and
performance, reliability, security and compliance (data location, access,
audit), integration points, team skills, and timeline. Mark which are hard
constraints. Note whether the capability is core to the product (a reason to
build) or commodity (a reason to buy or adopt).

## Generate options

Include at least: build in-house, one or more managed services, one or more
open-source options self-hosted, and extending something the team already
runs. Check each option's current documentation, pricing page, release
activity, and support status at task time; do not rely on remembered prices
or features. For open-source components, apply `dependency-risk-review`.

## Compare on the same criteria

| Criterion | What to estimate |
| --- | --- |
| Fit | Which hard requirements each option meets, partially meets, or misses |
| Total cost (12-36 months) | Licences or usage at expected and high volume, infrastructure, build effort, ongoing maintenance and on-call time |
| Time to value | Effort to first production use |
| Operational burden | Upgrades, scaling, backups, incidents, who is paged |
| Risk | Vendor viability, security record, single points of failure, compliance |
| Lock-in and exit | Data export, standard protocols, migration effort if the option fails or pricing changes |
| Control | Ability to customise, debug, and prioritise fixes |

Label estimates and their assumptions. Engineering time is a cost; price it.

## Recommend

Recommend one option with the deciding reasons and the accepted trade-offs,
define the exit plan (what triggers re-evaluation, how data leaves), and list
a small proof of concept or trial that would validate the riskiest assumption
before committing. Signing contracts, creating accounts, and paid plans are the
user's decision. Record the outcome with `document-decisions`.

## Report

Requirements, options considered, comparison table with sources and dates,
recommendation, exit plan, validation step, and open questions.
