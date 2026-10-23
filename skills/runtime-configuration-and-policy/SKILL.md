---
name: runtime-configuration-and-policy
description: >-
  Design, implement, or review typed runtime configuration, administrative
  settings, hot reload, and versioned business policies. Use when settings must
  change without a release, concurrent editors can overwrite each other, secret
  references need replacement, or an operation must retain its original policy.
  Distinguish authoring, publication, runtime adoption, and execution approval.
---

# Runtime configuration and policy

Make configuration a validated lifecycle, not an untyped key/value escape hatch.
Read the repository's domain decisions, configuration loader, consumers,
administrative permissions, secret-store contract, and testing policy first.
Reuse the existing control plane rather than creating another settings service.

## Classify settings and ownership

For each setting, identify its owner, type, validation, scope, sensitivity,
default policy, source precedence, reloadability, consumers, and failure behavior.
Keep these categories distinct:

- deployment/bootstrap settings needed to reach the configuration service;
- non-secret operational settings and references to protected secrets;
- business policies with draft, validation, publication, and revision semantics;
- activation flags, kill switches, and permissions that authorize effects.

An administrative form is not authorization to execute the configured effect.
Keep infrastructure/engineering privileges separate from business administration.
Authorize and audit reads, writes, publication, and activation independently.
Require the repository's identity/step-up controls for sensitive operations.

## Build capability without inventing policy

Unchosen commercial, legal, retention, or model values need not block building
the approved typed mechanism, validation, and UI. Do not invent those values,
reopen settled decisions, or advertise a mode that is only a stub. Separate:

1. implemented and locally qualified capability;
2. an authorized operator's valid published configuration;
3. consumer adoption of that revision; and
4. separately authorized operational activation.

Without required valid configuration, expose an explicit unavailable/disabled
state. Ask only for unresolved choices that affect correctness or safety; do not
turn a temporary safe fallback into the permanent product specification.

## Publish and edit safely

- Validate a complete candidate snapshot before replacing current configuration;
  do not expose mixed old/new fields during refresh.
- Use opaque revisions and conditional writes for concurrent editing. A stale
  edit must conflict, not silently overwrite. Define delete/recreate behavior so
  an old revision cannot match a new object accidentally (the ABA problem).
- Distinguish compare-and-swap from idempotency. CAS prevents stale replacement;
  it does not prove the outcome of a write whose response was lost.
- Retain a stable command identity and a supported reconciliation path for
  uncertain writes. Do not blindly retry, declare failure, or enable later writes
  while the earlier effect is unknown.
- Keep published policy revisions immutable where operations depend on them.
  Bind each operation to its policy snapshot before its first external effect;
  retries/restarts use that binding, not whatever is latest now.
- Do not retroactively change in-flight operations when publishing a revision.
  Any deliberate migration of them is a separate domain decision.

## Refresh consumers, not just a struct

Identify which settings can be read dynamically and which require replacement
of clients, connection pools, credentials, caches, or workers. Prepare and
validate replacements, switch atomically at the appropriate ownership boundary,
and drain/close old instances safely. Avoid overlapping schedulers or leaving
revoked credentials in active pools.

Choose refresh cadence, jitter, timeouts, version ordering, and observability
from the actual workload. Report **published revision** separately from
**revision adopted by each consumer**; a successful store write is not proof of
runtime adoption.

Resolve a documented decision table for missing values, transient outage,
invalid snapshots, explicit deletion, and revocation. Last-known-good may be
appropriate for a transient outage, but must not silently undo deliberate
revocation or bypass an invalid required policy. Do not silently fall back to a
different backend, provider, or environment value for every error. Keep bootstrap
access independent of the service it must bootstrap.

## Protect secrets and qualify the lifecycle

Expose secret metadata/references, not resolved values, in administrative reads,
browser bundles, audit events, command fingerprints, and error bodies. Provide
explicit keep/replace/remove behavior rather than echoing stored secrets into
forms. Use the established secret manager and reference mechanism; do not build
custom cryptography or copy deployment credentials into tests.

Test with synthetic data and real local persistence where available:

- validation and authorization, including read/write/publication separation;
- stale concurrent edits, delete/recreate revisions, and lost-response recovery;
- atomic refresh, out-of-order refresh, invalid candidates, outage, and revocation;
- actual client/pool adoption and safe retirement, not just loader unit tests;
- policy publication during retry/restart of an already-started operation;
- safe errors, audit metadata, and browser exposure boundaries.

For broader journey design use `system-module-architecture`; for credentials use
`credential-lifecycle-and-rotation`; for asynchronous effects use
`resilient-async-workflows`. Follow `testing-standard` for the repository gate.

## Report

State the setting/policy lifecycle, authority and source precedence, versioning
contract, adoption evidence, failure matrix, tests, and unresolved activation
gates. Do not mutate live configuration, activate effects, or deploy merely
because the local mechanism is complete.
