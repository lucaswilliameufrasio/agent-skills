---
name: migration-parity-audit
description: >-
  Audit or plan a legacy replacement, framework rewrite, service extraction,
  or backend migration for behavioral parity and cutover readiness. Use when
  route counts, passing tests, merged PRs, or a migration status document are
  being treated as proof that the replacement is complete. Cover workers,
  consumers, data, permissions, failures, and deliberate contract changes too.
---

# Migration parity audit

Verify behavior at a known source revision. A replacement can build successfully
while required behavior is absent, delegated to the legacy system, or unsafe to
activate. This workflow produces an evidence-backed matrix and a safe next slice;
it does not authorize a production cutover.

## Establish the baseline

Read repository instructions, domain decisions, API specifications, route and
worker registration, persistence, tests, migration documents, and current issue
scope. Verify the checkout, worktree, branch, source refs, and dirty changes.
Do not continue feature work on a release branch implicitly or overwrite another
agent's work to match a stale status document.

Identify the old system as a behavioral reference, not unquestionable policy.
Distinguish behavior to preserve, known defects not to reproduce, approved
changes, and unresolved product decisions. Reconcile documentation and tracker
claims against actual registration and implementation at the reviewed refs.
Label stale evidence rather than silently replacing historical facts.

## Build a capability matrix

Inventory more than public HTTP paths. Include internal APIs, jobs, schedulers,
queue consumers, webhooks, projections, files/media, exports, authentication,
authorization, tenant scoping, and recovery/operational controls where present.
For each capability record:

- old entry point, actor, prerequisites, accepted input and durable effects;
- new owner and implementation/registration, including fallback paths;
- success, error, timeout, retry, cancellation, and concurrency semantics;
- data/schema dependencies and reader/writer compatibility during coexistence;
- authoritative contract and source/test evidence with reviewed revision;
- status, remaining gap, owner, and a concrete acceptance check.

Use explicit states such as unassessed, absent, legacy-fallback, implemented but
unqualified, parity-verified, approved-change, and out-of-scope. Define them in
the audit. A stub is absent behavior; a forwarding route is not native parity.
Approved-change requires a decision and its own tests, not a quieter label for
an unexplained difference. Route totals are an inventory check, not the verdict.

## Compare contracts and effects

Trace identity/permissions and durable effects through the whole journey. Match
response statuses, wire formats, pagination, ordering, error codes, privacy,
idempotency scope, conflict handling, and externally visible timing. A new
asynchronous acceptance response is not equivalent to synchronous completion:
qualify operation identity, authenticated status lookup, terminal results, client
pending states, and durable handoff separately.

Do not fix compatibility by silently restoring an insecure legacy control or by
inventing a new endpoint/business rule. Surface the choice and obtain approval
where behavior materially changes. Use named adapters for explicit compatibility
boundaries, not arbitrary request forwarding.

For background work, check who owns each trigger and effect before, during, and
after migration: start position, duplicate delivery, fencing, outbox/inbox,
retry/dead-letter behavior, lag, last success, and reconciliation. Two deployed
implementations must not both perform the same non-idempotent effect. Code for a
successor worker does not prove the old worker has been retired.

## Qualify locally, separate activation

Use synthetic fixtures and the repository's real local database/broker/services.
Exercise contract tests against both owned implementations when available.
Normalize irrelevant generated fields, but do not normalize away real semantic
differences. Do not call production systems or copy customer data just to fill
the matrix. Missing environmental evidence stays unverified.

Include permission/tenant denials, failures, duplicate requests, simultaneous
writes, restart recovery, partial effects, and representative client journeys.
Test additive schema changes and mixed-version readers/writers when coexistence
is intended. A green unit suite or local emulator is not evidence of external
provider behavior, production data compatibility, or live routing.

Specify cutover prerequisites separately: approved owner/traffic transition,
consumer/schedule fencing, data reconciliation, monitoring, backup/restore proof,
roll-forward/rollback limits, and an explicit activation decision. App rollback
does not undo destructive schema/data changes. Do not stop legacy services,
enable replacements, merge, deploy, or migrate shared data from an audit request.

## Deliver the audit

Return the source refs and scope, matrix summary, exact open gaps and decisions,
validation evidence/limits, and first safe vertical slice. Update the project's
established migration record only when authorized; do not create competing status
documents. Keep overall migration incomplete while required gaps remain, even
when a particular slice is delivered.

Use `web-capability-architecture` for prototype-to-real web slices,
`resilient-async-workflows` for durable effects, `backup-restore-drills` for recovery
proof, and `testing-standard` for the quality gate. These complement rather than
replace the parity matrix and separately approved cutover.
