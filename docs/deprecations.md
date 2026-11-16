# Deprecations

## Compatibility entry points (removal planned for 2027-02-16)

| Deprecated skill | Use instead |
| --- | --- |
| `quality-gate` | [`testing-standard`](../skills/testing-standard/SKILL.md) and [`task-completion`](../skills/task-completion/SKILL.md) |
| `test-strategy` | [`testing-standard`](../skills/testing-standard/SKILL.md) |
| `testing-quality-gate` | [`testing-standard`](../skills/testing-standard/SKILL.md) |
| `git-workflow` | [`git-delivery`](../skills/git-delivery/SKILL.md), [`conventional-commits`](../skills/conventional-commits/SKILL.md), and [`pr-merge-sequence`](../skills/pr-merge-sequence/SKILL.md) |

**Why.** These entry points hold no policy of their own; each only redirects to
the canonical skill. Installed side by side, they compete with the canonical
skill for the same requests, so an agent may load the alias first and then
spend another step loading the real policy, or stop at the alias.

**What already moved.** Everything `git-workflow` states (refresh the local
base with `git pull --rebase`, rebase before every feature PR merge,
authorization boundaries) is owned by `git-delivery` and `pr-merge-sequence`.
Testing rules are owned by `testing-standard`.

**What does not move.** `git-workflow` and `test-strategy` read an optional,
user-owned `references/local-conventions.md`. The canonical skills will not
read it. Before removal, move those conventions to your personal agent
instructions or memory, or to each repository's `AGENTS.md` when they are
project rules. The two aliases offer this migration when they are loaded, and
`git-delivery` and `testing-standard` mention the file if they find it; all of
them write only with your approval.

### Timeline

1. **Now:** the four descriptions say "Deprecated" and name the replacement, so
   harnesses prefer the canonical skill. Behaviour is unchanged.
2. **Before 2027-02-16:** install the canonical skills, migrate any
   `local-conventions.md`, update instructions or scripts that name the old
   skills, then uninstall the aliases (`npx skills remove <name> --global`, or
   your installer's equivalent). Back up anything private first.
3. **On 2027-02-16:** the four directories, their README rows, and their evals
   are removed from this repository in one commit. Installed copies keep
   working until you remove them; they simply stop receiving updates.

If you still depend on one of them, open an issue before the removal date.
