---
name: tech-debt-portfolio
description: >-
  Inventory technical debt with its measured cost, rank it by return, and turn
  the top items into scoped work. Use when asked what to refactor first, to
  justify debt work to stakeholders, or to plan a cleanup quarter.
---

# Tech debt portfolio

Debt is worth paying when its interest is high: it causes incidents, slows
frequent changes, or burns operator time. A list of things engineers dislike
is not a portfolio. Rank by measured cost against the effort to remove it.

## Inventory with evidence

Collect candidates from: incident and postmortem actions, code hotspots
(files changed most often combined with defect fixes, from git history),
slow or flaky CI steps, manual operational toil, outdated or unsupported
dependencies (`dependency-freshness`), modules with special cases or
coupling (`untangle-codebase`), and the team's own list. For each item record
where it lives and the evidence.

## Estimate interest and principal

For each item:

- **Interest** (ongoing cost): incidents or customer impact attributed to it,
  extra time per change in that area (from cycle time or the team's estimate),
  toil hours per month, risk exposure (security, end-of-life, single point of
  failure), and how often the area changes. Debt in code nobody touches costs
  little.
- **Principal** (cost to fix): effort range, risk of the fix, and whether it can
  be done incrementally.

Mark each number as measured or estimated. Use ranges, not false precision.

## Rank and shape

- Rank by interest relative to principal, with risk exposure as a tiebreaker;
  security and end-of-life items with real exposure go first regardless.
- Prefer items that can be paid incrementally alongside feature work in the
  same area.
- Turn the top items into scoped issues with a verifiable done criterion and
  the expected benefit (`jira-issue-writing` when the tracker is Jira).
- Note items deliberately accepted, and why.

Creating issues in a tracker requires the user's authorization.

## Report

A ranked table: item, evidence, interest (measured or estimated), principal,
incremental path, recommendation (fix now, fix with next feature work, accept).
Then the top three with expected benefit, and what data would improve the
estimates.
