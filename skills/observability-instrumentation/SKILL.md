---
name: observability-instrumentation
description: >-
  Add structured logs, metrics, and traces that answer real questions about a
  service, with bounded cardinality and no secrets. Use when instrumenting code,
  adding OpenTelemetry, or when an incident showed you could not see what broke.
---

# Observability instrumentation

Telemetry exists to answer questions during an incident or investigation: is
it broken, for whom, where, and since when. Instrument for those questions,
not for completeness. Every signal costs money, attention, and sometimes
privacy.

## Start from the questions

List the questions the team must answer quickly, usually from the service's
journeys and SLOs (`slo-and-alerting`) and from recent incidents
(`postmortem`): error rate and latency per endpoint or job, queue depth and
age, dependency health, and what a single failing request did. Then inspect
what the service already emits and which backend receives it. Reuse the
existing libraries, exporters, naming, and dashboards; do not add a second
stack.

## Choose the signal

| Need | Signal |
| --- | --- |
| Rates, ratios, latency distributions, saturation over time | Metrics (counters, histograms, gauges) |
| What happened in one request or job across services | Traces with spans and propagated context |
| Detail for a specific event or failure | Structured logs correlated with the trace id |

For request-serving code, cover RED (rate, errors, duration) per route or
operation; for resources and queues, USE (utilization, saturation, errors).
Use histograms for latency, not averages.

## Rules that keep telemetry useful

- **Cardinality.** Label metrics only with bounded values (route template,
  method, status class, dependency name). Never user ids, emails, full URLs,
  raw error messages, or request ids as metric labels; put those in logs or
  span attributes when needed.
- **Context propagation.** Propagate trace context across HTTP, messaging, and
  background jobs, including into async workers. Include the trace id in every
  log line.
- **Structured logs.** Key-value or JSON with a stable schema; levels that mean
  something (error = someone should look). No multi-line dumps.
- **No secrets or personal data.** Redact tokens, passwords, cookies,
  authorization headers, and personal fields at the source
  (`secrets-safety`). Check what libraries log by default.
- **Naming.** Follow the backend's or OpenTelemetry's semantic conventions and
  the repository's existing names; units in names or metadata.
- **Sampling and cost.** Decide trace sampling (head or tail) and log volume
  explicitly; estimate monthly volume before enabling in production.
- **Failure isolation.** Telemetry export must not block or crash request
  handling; use bounded buffers and non-blocking exporters.

Verify library and SDK versions against upstream before adding them
(`dependency-freshness`).

## Verify

Run the service locally with the exporter pointed at a local collector or
console, exercise the instrumented paths (success, error, timeout), and check
that each question from the first step can be answered from the output:
the metric exists with expected labels, the trace spans connect across
boundaries, logs carry the trace id, and no secret or personal value appears.
Add tests where the codebase supports asserting emitted telemetry.

## Report

Questions covered and the signals that answer them, new metrics with labels
and expected cardinality, trace propagation points, redaction applied, sampling
and volume estimate, and what remains invisible.
