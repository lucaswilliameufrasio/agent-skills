---
name: rfc-writing
description: >-
  Write a technical proposal (RFC or design doc) that states the problem,
  compares real alternatives, recommends one, and plans rollout. Use when asked
  to write an RFC, design doc, or proposal for a significant change.
---

# RFC writing

An RFC is a decision tool. Its readers need to understand the problem, trust
that alternatives were weighed fairly, see the risks, and know what they are
being asked to decide. Write for them, not to document the solution you
already like.

## Before writing

Gather evidence for the problem: incidents, metrics, user or team requests,
cost. Read the code and existing decisions (`document-decisions`) the change
touches, and talk to (or list) the owners of affected systems. If the problem
cannot be stated with evidence, say so to the user; the RFC may be premature.
Use the repository's or team's template if one exists.

## Structure

1. **Summary** — two or three sentences: problem, recommendation, the decision
   requested and by when.
2. **Problem and context** — what hurts today, with evidence; who is affected.
3. **Goals and non-goals** — measurable goals; explicit non-goals to keep
   scope honest.
4. **Options** — at least two real alternatives plus "do nothing" (and "buy
   or adopt" when relevant, see `build-vs-buy`). Compare them on the same
   criteria: fit to goals, complexity, cost, risk, reversibility, operability,
   time to deliver.
5. **Recommendation** — the chosen option and why, including which trade-offs
   are accepted.
6. **Design** — enough detail to evaluate: components, data and contracts,
   failure modes, security and privacy, observability, capacity.
7. **Rollout and rollback** — incremental steps, migration and compatibility
   (`schema-migration-safety`, `progressive-delivery`), how success is measured,
   how to back out.
8. **Risks and open questions** — each with an owner or a way to resolve it.

## Style

- Lead with the decision needed; readers may stop after the summary.
- Separate facts (with sources), estimates (labelled), and opinions.
- Mark one-way doors explicitly; they deserve the most detail.
- Prefer diagrams or tables where they replace paragraphs.
- Keep it as short as the decision allows.

Before sharing, review it as a critic would (`technical-design-review`) and fix
what that review finds. Do not publish, circulate, or request approval on the
user's behalf without authorization; once decided, record the outcome with
`document-decisions`.

## Report

The draft location, the decision it asks for, open questions that still need
the user or other owners, and any evidence gaps.
