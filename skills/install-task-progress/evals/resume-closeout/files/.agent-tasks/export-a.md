# Active task: CSV header correction

Task ID: export-a
Owner: fixture-owner-a
Repository/worktree: this fixture, checkout-a
Updated: 2026-10-26T10:00:00Z
State: active

## Scope and progress

- Verified: change CSV header from internal_id to public_id as approved.
- Verified: preserve column order and correctly escape quoted fields (checks.txt).
- Pending: durable outcome note, evidence read-back, then exact-file cleanup.

## Decisions

Existing confirmed decision D-01 in docs/decisions.md explains public identifiers.
No new substantive decision; do not duplicate it.

## Next action

Inspect checks.txt and D-01, write/read durable outcome, remove only export-a.md.
