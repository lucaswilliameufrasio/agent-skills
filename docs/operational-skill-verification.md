# Operational skill additions

## Selection and boundaries

Four independent workflows now have reusable skills: secret namespace ownership,
configuration-service bootstrap, local validation for billing-blocked CI, and
insert-only deployment imports. Examples are synthetic; no private service
names, incidents, hostnames, repository links, credentials, or environment
topology are included.

Shell detection and command lifetime extend `shell-docker-preflight`, rather
than duplicating it. Feature rebase sequencing and release distinctions extend
`pr-merge-sequence`, linked from `git-delivery`. Organization-specific exceptions
are not universal permissions: local substitution needs the target project's
approval, and release reconciliation follows its documented branching model.

## Behavioral review scenarios

These are review criteria, not records of executed model evaluations.

| Area | Scenario | Expected behavior |
| --- | --- | --- |
| Namespaces | Two services have different databases but both use `DATABASE_URL`. | Use separate owner namespaces. Matching names do not justify sharing. |
| Namespaces | Own key missing, same key exists in shared namespace. | Do not fall back unless sharing is explicitly intended; qualify cache/refresh too. |
| Bootstrap | Import resolves tokens but still requires DSN and bucket in deployment env. | Identify incomplete migration and trace all constructors and commands. |
| Bootstrap | Store unavailable; old env and local defaults are present. | Fail deployed Vault mode; preserve only explicitly supported local mode. |
| Bootstrap | New keys require an operator bulk import. | Generate per-environment templates using the actual importer schema; document purpose, filling instructions, synthetic example and optionality per key; protect credential files from Git. |
| Bootstrap | Provider has no comment field in its import format. | Put keyed instructions in a companion file; do not invent unsupported fields or copy another provider's schema. |
| Billing | Explicit spending-limit message prevents workflows starting. | Stop futile reruns; enumerate and run equivalent local checks, bound to SHA. |
| Billing | A required matrix platform is unavailable locally. | Mark it unverified, not passed; report remaining blocker. |
| Billing | Branch protection still requires remote CI. | Report merge blocked without fabricating statuses or implicit admin bypass. |
| Import | Destination contains a newer record with the same identity. | Conditional insertion preserves its data; verify by database readback. |
| Import | Import fails halfway then runs again. | Safe resumption, accurate counts, explicit atomicity limits. |
| Shell | Login Fish, tool executor Bash. | Use each context's syntax; do not change login configuration. |
| Shell | A prior call loaded a helper or changed directory. | Do not assume persistence unless the tool guarantees it. |
| Merge | Several feature PRs with a moving base. | Rebase and validate each against the latest base before its merge. |
| Release | Development-branch promotion with direct main commits. | Inspect policy and reconcile development first when required; no generic release rebase. |

## Verification limits

Structural/frontmatter, catalog links, whitespace, and source-identifier scans
can be checked locally. They are not evidence of behavioral effectiveness or a
with-skill versus baseline improvement. No remote Vault/import/deploy is needed
to author these skills. Privacy scans reduce risk but do not guarantee absence
of all sensitive material.
