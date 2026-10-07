---
name: resilient-async-workflows
description: >-
  Design or improve asynchronous jobs, webhook processing, consumers, and
  downstream calls. Use when work needs retries, timeouts, cancellation,
  idempotency, durable acceptance, dead-letter handling, or protection from
  retry storms. Trace the full lifecycle and delivery guarantees before adding
  retries or choosing an in-memory queue.
---

# Resilient asynchronous workflows

Make asynchronous work bounded, recoverable, and observable. Reliability is an
end-to-end contract: accepting a job, retrying it, and reporting completion must
have explicit behavior across timeouts, duplicate delivery, and process failure.

## Define the lifecycle and guarantees

Map submission, validation, persistence, acknowledgement, scheduling, execution,
downstream effects, completion, retry, and terminal failure. Establish whether
the intended guarantee is best-effort, at-most-once, or at-least-once; do not
claim exactly-once effects without a concrete transactional/idempotent design.

If acceptance must survive a restart, persist the job or a durable event before
acknowledging it. For database-triggered work, evaluate an outbox/transactional
handoff. Use idempotency keys or idempotent handlers because webhook and broker
delivery can repeat. Bound consumer concurrency and any local buffering even
when a durable broker exists.

## Bound time and retries

- Give the whole operation a deadline and propagate its remaining budget through
  queue wait, each attempt, and downstream calls. A timeout of the local wait
  does not cancel remote work unless the client/protocol supports cancellation.
- Classify retryable errors. Do not retry validation failures, permanent errors,
  or work whose result is unknown without an idempotency strategy.
- Bound attempts and total retry time. Use exponential backoff with jitter and
  honor downstream retry guidance where appropriate.
- Avoid retries at multiple layers that multiply attempts. Consider a retry
  budget, circuit breaker, or load shedding when downstream health is degraded.
- Define terminal failure handling: surfaced status, durable dead-letter or
  retry queue, alerting, and safe operator reprocessing.

Retries can amplify load precisely when a dependency is failing. Include the
initial attempt in capacity reasoning and monitor retry rate, queue age/depth,
timeouts, failures, and downstream saturation. Do not add retries as a generic
fix for latency.

## Preserve correctness on every exit path

Make state transitions explicit and idempotent. Ensure reservations, leases,
tenant quotas, and in-flight counters are released exactly once after success,
failure, timeout, cancellation, and process shutdown. Avoid acknowledging a
message before durable completion unless the delivery contract and recovery path
allow it. Use leases/visibility timeouts carefully so work is not duplicated or
lost when a worker dies.

## Validate the failure modes

Test transient failure followed by success, exhausted retries, permanent error,
deadline expiration, cancellation propagation, duplicate delivery, worker crash,
and downstream outage. Assert attempts are bounded, final state is correct,
resources are released, and overload does not create a retry storm. Use a real
local broker/database when the project has one; fake only external systems at a
clear protocol boundary.

For admission and capacity limits, use `backpressure-and-admission-control`.
For shutdown while work is pending, use `graceful-shutdown-drain`. For load and
performance evidence, use `performance-benchmarking-and-load-testing`.
