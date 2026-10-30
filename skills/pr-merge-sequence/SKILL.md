---
name: pr-merge-sequence
description: Safely merge one or more GitHub pull requests while keeping dependent branches current. Use whenever the user asks to merge multiple PRs, rebase PR branches before or after a merge, sequence merges, or says to merge normally rather than squash/rebase.
---

# PR merge sequence

Use this workflow when several open pull requests must be merged without letting later PRs drift behind the base branch.

## Before changing branches

1. Confirm the repository, current branch, and `git status`. Preserve any unrelated local work; do not reset or discard it.
2. List the requested PRs and inspect their base/head branches, draft state, mergeability, latest commit, checks, reviews, inline threads, and unresolved findings.
3. Refresh the base branch from the remote. Read applicable repository instructions and the user's merge/rebase preferences.
4. Do not mark a draft ready or merge any PR until the user has authorized that state change.

## Rebase and merge loop

1. Immediately before each feature/bugfix merge, fetch its current remote base and rebase that PR branch onto it, unless already current. Rewriting published history requires authorization; use `--force-with-lease` with the expected remote SHA, never plain `--force`. If a rebase conflicts or would overwrite unexpected work, stop and reconcile rather than dropping commits. Run the complete applicable gate on the resulting head; an old SHA's checks do not validate it.
2. For the next PR in the user-specified order, verify its remote head matches the rebased commit, all required checks are green, and no unresolved valid review finding remains. Inspect new comments after each push/rebase; reply and resolve findings according to the user's established workflow. Do not dismiss a security finding merely to get a green review.
3. Merge with a normal merge commit (for GitHub CLI, `gh pr merge <number> --merge`). Never use squash or rebase merge when the user requires normal merge commits.
4. After each merge, fetch the new base and repeat the rebase/validation loop for the next requested feature/bugfix. Do not validate all branches against an old base and then merge the batch without refreshing it. Check for another base update before merging.
5. Repeat until the requested sequence is complete. Do not merge unrelated PRs just because they are open or green.

## Release branches are not feature branches

Discover the release workflow before applying the rebase loop. In a Gitflow
project that promotes `develop` through a release branch, do not rebase the
release onto `main` merely to satisfy a feature-branch freshness rule. Prepare
the release from the updated development branch under the project's policy.

If that policy requires reconciling direct commits on `main` by rebasing
`develop` onto `main`, do so before creating the release, not by patching only
the release. Inspect divergence, exclusive release fixes, other worktrees and
collaborators first. Rewriting a shared development branch requires explicit
authorization, fresh validation, and a safe lease; do not recreate branches,
discard commits, or bypass protection automatically. This is a conditional
workflow, not a universal requirement for projects that use different release
or back-merge policies.

## Stop conditions

For explicitly confirmed billing-blocked Actions, use
`actions-billing-local-validation` to complete equivalent local checks under
the repository's approved substitution policy. Do not retry billing failures
in a loop or bypass protection; real failures still block.

Pause before merging if a required check fails or is still running, a new actionable finding is unresolved, the PR is not mergeable, the head changed unexpectedly, or the rebase has conflicts. Report the concrete blocker and next safe action. A false positive should be explained with evidence and resolved; a valid finding should be fixed, tested, pushed, and re-reviewed.

## Finish

Verify each requested PR's merged state and merge commit, confirm all surviving branches include the latest base, and report the final heads/checks. If the work included merges, preserve the sequence in the project progress record when the user requested that record be maintained.
