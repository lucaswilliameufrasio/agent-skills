# Untangle-codebase evaluations

These synthetic scenarios check portable refactoring decisions, not mastery of
every ecosystem or successful execution in a real project. Give agents only the
prompt and the selected skill (for with-skill runs), not graders or expected
outcomes. No source checkout, package installation, live service, or credentials
are needed. Save paired baseline/with-skill outputs outside this repository.

Scenarios:

- `mixed-stack-contracts`: mixed-language audit with native and wire contracts;
- `dynamic-package-consumers`: a package that appears unused to an import scan;
- `bounded-refactor`: implementation planning with a failing baseline and no
  delegation or graph-analysis tools.

The prompts intentionally request analysis or next steps. Passing these checks
does not establish runtime behavioral parity, cross-platform support, automatic
activation, or measured improvement over a baseline. Real execution evaluations
need isolated project fixtures, contract tests, and artifact inspection.

See [initial results and limitations](RESULTS.md) for the paired scenario review.
