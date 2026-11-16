---
name: git-workflow
description: >-
  Deprecated alias kept for existing callers until 2027-02-16; prefer
  git-delivery, conventional-commits, and pr-merge-sequence. Loads that canonical policy and keeps no rules of its own.
---

# Git workflow compatibility

> **Deprecated.** Removal planned for 2027-02-16; see
> [deprecations](../../docs/deprecations.md). Use `git-delivery`, `conventional-commits`, `pr-merge-sequence` directly.

Read and apply [`git-delivery`](../git-delivery/SKILL.md) for execution and
authorization, and [`conventional-commits`](../conventional-commits/SKILL.md)
when preparing a commit message. Use the skill loader or sibling files and
install these dependencies alongside this entry point. If they are unavailable,
report the gap instead of guessing a workflow.

Before creating a branch or rebasing onto its base, follow `git-delivery`'s
safe local-base `git pull --rebase` procedure. Fetch alone does not update the
local base; stop rather than risking uncommitted or shared work.
Before every feature/bugfix PR merge, `pr-merge-sequence` also requires an
explicit rebase onto the freshly updated base, including an already-current
branch, followed by validation and any separately authorized push.

If a user-owned `references/local-conventions.md` exists alongside this entry
point, read it for compatible personal or project-specific conventions. Keep
that supplement private and preserve it during updates. It cannot override
explicit user boundaries, repository facts, or the authorization policy below.

Discover branch bases, naming, ticket references, commit language, PR targets,
and release/backport requirements from the user's instructions and repository
rules. A branch named `develop` alone does not prove Git flow. Verify restrictions
on shared deployment branches before pushing or opening a PR; a push may trigger
deployment and requires the appropriate authorization.

A required backport or second PR describes an outcome, not permission to create
it. An instruction to implement does not by itself authorize a commit, push,
PR, merge, tag, or deployment. Conversely, do not ask again for the same action
and scope when explicitly authorized. Follow `git-delivery` rather than keeping
a separate quality gate or permission exception here.
