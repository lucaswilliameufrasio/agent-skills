---
name: dependency-freshness
description: >-
  Pick current stable versions of runtimes, toolchains, CLIs, libraries, and
  base images from upstream, not memory or global installs. Use when adding a
  dependency, creating a project, or updating versions.
---

# Dependency freshness

Agents tend to write the versions they remember from training data, or use
whatever version is installed globally on the machine, which may be years old.
Both silently start new work on stale, sometimes unsupported or vulnerable
versions. Check upstream every time a version is chosen.

## Choosing a version for anything new

For each runtime, toolchain, CLI, library, base image, or template being added:

1. Find the canonical upstream (official site, release page, or the package
   registry entry linked from the official repository). Beware similarly named
   packages and forks.
2. Read the current stable release and, for runtimes and frameworks, the
   support policy (LTS line, end-of-life dates). Prefer the newest stable
   release; for runtimes with LTS lines, prefer the active LTS unless the
   project needs a newer feature.
3. Check compatibility with what the project already pins (peer dependencies,
   minimum runtime, platform, architecture). If the newest release is
   incompatible, choose the newest compatible one and say why.
4. Record source and lookup date in the report. If upstream cannot be reached,
   say the version is unverified instead of presenting a remembered number as
   current.

Use the package manager's own add/install command so the lockfile is updated
by the tool, not by hand.

## Do not inherit the global install

The version installed on the machine is a fact about the machine, not a
project decision.

- Inspect the project's version pins first: tool-version files, toolchain
  files, engine fields in manifests, `go`/`toolchain` directives, container
  base images, CI setup steps. Pins win over globals.
- When a project has no pin, add one through the project's version manager or
  the language's native mechanism, set to the version chosen above, rather than
  using the global version implicitly.
- If the global install is older than what the project needs, run the project
  through its version manager or a per-project install. Updating the global
  install changes other projects on the machine: propose it with the current
  and target versions and do it only with approval.
- Do not generate a project with a scaffolding command from an old globally
  installed CLI; run the current version of the generator (or upgrade the CLI
  first, with approval) and verify the template versions it produced.

## Upgrading existing dependencies

1. Inventory what is outdated using the ecosystem's own commands, plus base
   images, toolchain pins, and CI setup versions. Note anything end-of-life or
   with security advisories first.
2. Group upgrades: patch and minor together where the ecosystem follows
   semantic versioning; each major separately.
3. For each major, read the upstream changelog and migration guide for every
   version crossed, list breaking changes that touch this codebase, and apply
   official codemods or migration tools when available.
4. Upgrade through the package manager, keep the lockfile consistent, and run
   the full quality gate (`testing-standard`). Do not upgrade the application's
   runtime as a side effect of a library upgrade without saying so.
5. One logical upgrade per commit or PR so failures are bisectable.

## Prevent drift

Recommend or configure the hosting platform's dependency update automation if
the repository does not have one, grouping minors and separating majors, with
human review of majors. A one-time update does not keep a project current.
For CI action references, follow `github-gitea-actions`; for container images,
pin by digest where the repository's policy prefers immutability, with a
comment naming the tag.

## Report

A table of what was chosen or upgraded:

| Component | Before | After | Latest stable checked | Source and date | Notes (breaking changes, compatibility) |
| --- | --- | --- | --- | --- | --- |

Then what was left behind and why, globals that are stale with a proposed
update, and checks run.
