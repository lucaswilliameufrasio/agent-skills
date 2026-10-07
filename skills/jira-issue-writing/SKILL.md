---
name: jira-issue-writing
description: >-
  Create or refine complete, actionable Jira issues. Use whenever asked to open,
  draft, split, or improve a Jira card, story, task, feature, or bug. Check the
  target project and board for duplicates, make cross-repository solutions
  explicit, and write verifiable acceptance criteria without inventing decisions.
---

# Jira issue writing

Write issues that represent user or operational outcomes and can be delivered
and verified. Adapt to the target Jira project's issue types, hierarchy, fields,
and team conventions instead of assuming every board is configured the same way.

## Workflow

1. Identify the Jira instance, project, board, and available issue types. Inspect
   project configuration or existing issues when needed; ask only for missing
   choices that affect where or how the work is filed.
2. Search the target project/board for duplicate work, related issues, and
   suitable parent items. Report likely matches. Do not create a duplicate while
   the overlap is unresolved.
3. Gather the requested outcome, existing product/technical decisions, affected
   users, repository conventions, and dependencies. Treat proposed designs as
   proposals until confirmed. Mark unknowns as open questions instead of
   inventing behavior, limits, ownership, or contracts.
4. Prefer one independently deliverable end-to-end slice per issue. Do not split
   work into backend-only, frontend-only, or test-only cards unless the user
   requests that decomposition or those deliverables are independently usable.
5. For cross-repository work, explain each affected repository's responsibility
   in the technical solution. Keep the issue focused on the shared outcome and
   name cross-repository dependencies explicitly.
6. Include context, outcome, scope and non-goals, proposed technical solution,
   testable acceptance criteria, dependencies, open questions, and required
   validation evidence.
7. Show the complete draft before creation unless the user explicitly asks to
   create the issue. Even with that authorization, resolve duplicate ambiguity,
   missing product decisions, and invalid hierarchy choices before creating.
8. After creation, return each issue key and link. Do not transition, assign,
   rank, link, or change parent/hierarchy unless the user requested it.

## Issue content

Use the issue type available in the target project. If the project uses localized
or custom issue type names, use the exact configured name. Do not assume an
`Epic`, `Feature`, or parent-child relationship exists; verify the hierarchy and
allowed fields first.

### Story

```md
### Context
Describe the problem or opportunity and who is affected.

### User story
As a [user/beneficiary], I want [capability], so that [outcome].

### Scope and non-goals
- In scope:
- Out of scope:

### Proposed technical solution
Describe end-to-end behavior, repository responsibilities, contracts,
authorization, compatibility, and failure handling. Mark proposed choices and
open questions clearly.

### Acceptance criteria
- [ ] Observable user or business behavior works.
- [ ] Validation, authorization, errors, and idempotency are covered where relevant.
- [ ] Automated tests cover success and important failure paths.
- [ ] Integration, end-to-end, or manual evidence is recorded where needed.
- [ ] Documentation and operations are updated where relevant.

### Dependencies and open questions
- Dependencies or blockers:
- Open questions:
```

### Task

```md
### Context and objective
State the concrete deliverable, why it is needed, and the resulting outcome.

### Scope and non-goals
- In scope:
- Out of scope:

### Proposed technical solution
Describe affected boundaries/contracts, repository responsibilities, security,
and failure behavior.

### Acceptance criteria
- [ ] The deliverable is present and behaves as specified.
- [ ] Relevant automated tests and failure paths are covered.
- [ ] Manual evidence is recorded when automation cannot verify the real system.
- [ ] Documentation and operations are updated where needed.

### Dependencies and open questions
- Dependencies or blockers:
- Open questions:
```

### Bug

Do not invent reproduction details. If the report lacks exact steps or
environment, ask for them before filing a Bug; use a Task or investigation issue
only when that better reflects the request.

```md
### Summary and impact
What is broken, who is affected, and what is the impact?

### Environment and prerequisites
- Environment/build/device/configuration:
- Preconditions or test data:

### How to reproduce
1. Exact action
2. Exact action
3. Exact action

### Actual result
Observed behavior and safe evidence.

### Expected result
Expected behavior.

### Proposed technical solution
State a suspected cause only when supported by evidence; otherwise describe the
investigation path.

### Acceptance criteria
- [ ] The reproduction no longer triggers the bug.
- [ ] A regression test fails before the fix and passes after it.
- [ ] Related success and failure paths remain correct.
- [ ] Documentation or monitoring is updated if behavior or operations change.

### Evidence and dependencies
- Evidence:
- Dependencies or open questions:
```

## Card quality and privacy

- Use concise, domain-specific titles and plain language.
- Make acceptance criteria observable and verifiable; avoid vague criteria such
  as “works correctly” without defining the behavior.
- Separate confirmed decisions from assumptions and proposals.
- Identify blockers without creating detached follow-up cards unnecessarily.
- Keep sensitive information out of issues: never include secrets, tokens,
  passwords, private customer data, or unrelated internal URLs. Use approved
  references or redacted evidence when detail is needed.
- For public skills, examples, or documentation, use synthetic names and values;
  do not copy private project identifiers, issue keys, board IDs, URLs, or
  repository details.
- Keep automated tests separate from manual infrastructure evidence when both
  are required.

## After creation

Report the issue key, link, type, and target project/board. State whether the
issue was linked to a parent or related issue only if that action was requested
and the tracker confirmed it. Never claim creation without a successful tracker
response.
