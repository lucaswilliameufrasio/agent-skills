---
name: dependency-risk-review
description: >-
  Assess a new library, action, or tool before adopting it: maintenance,
  security history, licence, transitive weight, and alternatives. Use when
  about to add a dependency, or when asked if a package is safe to use.
---

# Dependency risk review

Every dependency is code you run but did not write, maintained by people you
do not control. Before adding one, check that it is needed, maintained, safe,
licensed compatibly, and replaceable. Choosing its version is a separate step
(`dependency-freshness`).

## Is it needed?

Check whether the standard library, the framework, or a dependency already in
the project covers the need. For small functionality, compare the cost of a
few lines of owned code against a permanent dependency.

## Check the candidate (at task time, from primary sources)

- **Identity.** Canonical repository and registry entry; publisher matches the
  repository; watch for typosquats and similarly named forks.
- **Maintenance.** Recent releases and commits, responsiveness to issues and
  security reports, number of active maintainers (bus factor), deprecation or
  archive status, stated support policy.
- **Security.** Advisories in the ecosystem's database and the repository's
  security tab, how quickly past issues were fixed, install-time scripts or
  native code, requested permissions (for actions and plugins), signed
  releases or provenance where the ecosystem supports them.
- **Licence.** Licence of the package and of its transitive dependencies
  against the project's licence and distribution model; flag copyleft,
  non-commercial, or missing licences.
- **Weight.** Number of transitive dependencies, install and bundle size,
  native build requirements, platform support.
- **Fit and quality.** API stability, semver discipline, documentation, tests,
  compatibility with the project's runtime versions.
- **Exit.** How hard it would be to replace; whether it is wrapped behind the
  project's own interface.

Run the ecosystem's audit tool on the project with the candidate added, if
available. Do not install packages with install scripts into a shared
environment just to inspect them.

## Decide

Recommend adopt, adopt with conditions (pin, wrap behind an interface, vendor,
monitor advisories), choose an alternative, or write it in-house. Show the
evidence for each concern and the alternatives compared. Adding the dependency
follows the project's normal change process and the user's approval where
required.

## Report

Candidate and version considered, a short table of the checks above with
sources and lookup date, alternatives, recommendation, and conditions.
