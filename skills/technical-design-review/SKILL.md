---
name: technical-design-review
description: >-
  Review an RFC, design doc, ADR, or architecture like a principal engineer:
  alternatives, failure modes, one-way doors, rollout, ranked concerns. Use when
  asked to review or stress-test a design.
---

# Technical design review

A design review is cheapest when it changes the plan before code exists. Its
job is to find what would hurt later: wrong problem, missing alternatives,
failure modes, irreversible choices, and operational cost. Be specific and
constructive, and end with a decision the author can act on.

## Read for context first

Read the document fully, then the code, systems, and decisions it touches:
existing architecture docs and ADRs (`document-decisions`), the current
implementation, traffic and data volumes, SLOs, and team constraints. Note who
the author is asking to decide and by when. Verify claims about the current
system against the code or metrics instead of trusting the document.

## Review questions

**Problem.** Is the problem stated with evidence (incidents, metrics, user
requests)? Are goals and non-goals explicit? Is success measurable? Would a
smaller change solve most of it?

**Alternatives.** Were real alternatives considered, including doing nothing,
buying or adopting an existing component, and extending what exists? Are
trade-offs compared on the same criteria? If the chosen option was decided
before the comparison, say so.

**Reversibility.** Which decisions are one-way doors (data models, public APIs
and wire formats, storage engines, vendor lock-in, identifiers) and which are
two-way? One-way doors deserve most of the review time; two-way doors should
not block on debate.

**Failure modes.** For each component and dependency: what happens when it is
slow, down, returns errors, or returns wrong data? Retries and idempotency
(`resilient-async-workflows`), overload (`backpressure-and-admission-control`),
partial failure, data consistency, concurrency, clock and ordering
assumptions, and blast radius. What is the worst plausible incident?

**Data.** Ownership, schema evolution and migrations
(`schema-migration-safety`), backfills, retention, privacy and access control,
backup and restore (`backup-restore-drills`).

**Security.** Trust boundaries, authentication and authorization, secrets,
untrusted input, multi-tenant isolation, audit needs.

**Operability.** How will on-call know it is broken (SLOs and alerts,
`slo-and-alerting`)? Dashboards, runbooks, deploy and rollback, configuration,
capacity and cost at expected and 10x scale. Who owns it after launch?

**Rollout.** Incremental delivery, feature flags, migration of existing users
and data, compatibility during transition, rollback plan, and a way to measure
the outcome against the goals.

**Complexity.** Is the complexity proportional to the problem? New
technologies, services, or abstractions add permanent cost; are they
justified? Does it fit the team's skills and existing systems?

## Write the review

1. **Recommendation first**: approve, approve with changes, or rework, in one
   or two sentences with the main reason.
2. **Ranked concerns**: blocking issues (must change before building),
   significant risks (should address or explicitly accept), and suggestions
   (optional). Each concern states the issue, why it matters with a concrete
   scenario, and a proposed change or question.
3. **Questions** the author must answer, phrased so the answer resolves the
   concern.
4. **What is good**, briefly, so it survives revisions.

Separate verified facts from assumptions. Do not demand a full rewrite for
taste, and do not pile up minor comments that bury the important ones. When a
decision is made, suggest recording it with `document-decisions`.

## Do not

Do not approve on behalf of others or post the review publicly without
authorization. Do not invent product decisions; ask the owner.
