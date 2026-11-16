---
name: capacity-planning
description: >-
  Forecast when a service, database, or quota will run out and what headroom
  and cost are needed. Use for "when does this break?", growth planning,
  right-sizing, provider quotas, or before a launch or traffic event.
---

# Capacity planning

Capacity planning answers: at expected demand, what runs out first, when, and
what does it cost to stay ahead? It combines measured current usage, a
measured ceiling, and a demand forecast. Without all three, it is a guess and
must be labelled as one.

## 1. Inventory the constraints

For the system in scope, list every resource that can run out: CPU, memory,
disk and IOPS, network, connection pools, database connections and storage,
queue depth, thread and worker counts, rate limits and quotas of providers
and APIs, license or plan limits, and budget. Include managed-service limits;
they are often the first wall.

## 2. Measure current usage

From existing metrics, take peak (not average) utilization per resource over
a representative window, with the time of peak and its driver (requests per
second, jobs, data size). Note seasonality and batch spikes.

## 3. Know the ceiling

Use a measured saturation point where one exists, or run a load test
(`performance-benchmarking-and-load-testing`) in a safe environment to find
where latency or errors break the SLO. Vendor limits come from current
documentation or the account's quota page, not memory. A ceiling from a
different machine or dataset size is an estimate; say so.

## 4. Forecast demand

Project the driver from historical growth, known launches, marketing events,
and customer onboarding. Give a range (expected and high), not a single line.
Translate demand into resource usage with the measured ratio from step 2, and
check whether scaling is linear; queues, locks, and caches often are not.

## 5. Plan headroom and actions

- Target headroom so peaks plus a failure (one node or zone lost) stay below
  the ceiling.
- For each resource, compute the date it crosses the threshold under the
  expected and high forecasts, and the lead time to add capacity (procurement,
  quota requests, migrations).
- Options in order of preference: remove waste
  (`performance-optimization`), scale horizontally, scale vertically, change
  architecture. Show monthly cost for each.
- Quota increases and paid plans are the user's decision.

## Report

A table per resource: current peak, ceiling and how it was measured, forecast
crossing dates (expected/high), lead time, proposed action, and monthly cost.
Then the first thing that will run out, the decision needed and by when, and
which numbers are measured versus estimated.
