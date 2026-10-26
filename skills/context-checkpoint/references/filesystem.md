# Explicit filesystem task store

Use this only when the user or canonical project instructions selected files
for active task progress. Do not silently replace a chosen memory/task provider.

1. Discover the approved store from instructions. Inspect existing files and
   resolved paths; match task ID, owner, repository/worktree, and current scope.
   A title, branch name, recent timestamp, or symlink is not sufficient identity.
2. Read the full record before recovering or updating. Keep one canonical live
   file per task/worktree; isolate concurrent owners. Ordinary file edits provide
   no compare-and-swap/atomic multi-writer guarantee. Do not overwrite conflicts.
3. Persist the core skill's bounded recovery payload at material milestones and
   read it back. Use the repository's safe-write/locking helper when available.
   Name the exact path in available summaries, but make it discoverable through
   the instruction file so recovery does not depend solely on a chat pointer.
4. Separate active progress from durable knowledge. Keep verification proof and
   final outcomes in the repository's issue/delivery documentation; use the
   existing ADR/design convention for substantive decisions. Do not require ADRs
   for trivial tasks or mirror the live plan into ai-memory durable wiki pages.
5. If policy requires cleanup on completion, verify requested outcomes/checks,
   promote results/rationale/evidence pointers, read back the durable output,
   then remove only the exact completed owned record. Confirm durable files and
   evidence remain. Failed writes or outstanding required work block cleanup.
   Preserve blocked, partial, interrupted, and cancelled records unless the user
   explicitly authorizes a different disposition. Never clean the whole store.

Local-only/ignored records stay on that checkout: a new clone or worktree will
not contain them, and losing the disk loses unsynchronized progress. Versioned
records have different sharing/history implications; follow the selected policy.
Neither files nor AGENTS.md guarantee pre-compaction callbacks, cross-machine
recovery, or capture of unwritten work. Installing hooks, publishing records,
committing changes, or switching the provider requires separate authorization.
