# Confirmed decisions

## D-01 — Public identifiers in exports

Status: accepted
Context: external consumers should not depend on internal storage keys.
Decision: use public_id in exported column headers; keep column order stable.
Alternative: expose internal_id; rejected because it couples consumers to storage.
Consequence: compatibility changes require explicit contract review.
