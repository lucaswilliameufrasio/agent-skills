# Eufrasio's Agent Skills

A curated collection of reusable agent skills maintained in public.

## Skills

Install all first-party skills globally:

```sh
npx skills add lucaswilliameufrasio/agent-skills --skill '*' --global
```

Each row also has the command to install just that skill globally.

| Skill | Description | Install individually |
| --- | --- | --- |
| [`context-checkpoint`](skills/context-checkpoint/SKILL.md) | Persist scoped plans in a user-approved active-task store; recover available context from providers such as ai-memory without treating durable wiki pages as transient checkpoints. | `npx skills add lucaswilliameufrasio/agent-skills --skill context-checkpoint --global` |
| [`task-completion`](skills/task-completion/SKILL.md) | Carry authorized work through execution, verification, and an honest complete/partial/blocked handoff with concrete next actions. | `npx skills add lucaswilliameufrasio/agent-skills --skill task-completion --global` |
| [`quality-gate`](skills/quality-gate/SKILL.md) | Compatibility entry point for the canonical `testing-standard` and `task-completion` policies. | `npx skills add lucaswilliameufrasio/agent-skills --skill quality-gate --global` |
| [`test-strategy`](skills/test-strategy/SKILL.md) | Compatibility entry point for test boundaries and coverage in `testing-standard`. | `npx skills add lucaswilliameufrasio/agent-skills --skill test-strategy --global` |
| [`git-workflow`](skills/git-workflow/SKILL.md) | Compatibility entry point for repository-aware `git-delivery` and `conventional-commits`. | `npx skills add lucaswilliameufrasio/agent-skills --skill git-workflow --global` |
| [`pr-merge-sequence`](skills/pr-merge-sequence/SKILL.md) | Safely sequence normal GitHub PR merges while rebasing and revalidating remaining branches after each merge. | `npx skills add lucaswilliameufrasio/agent-skills --skill pr-merge-sequence --global` |
| [`single-state-enum`](skills/single-state-enum/SKILL.md) | Model mutually-exclusive UI overlays and modes with one discriminated-union state. | `npx skills add lucaswilliameufrasio/agent-skills --skill single-state-enum --global` |
| [`explicit-code-style`](skills/explicit-code-style/SKILL.md) | Prefer multiline conditionals, explicit loops, and clear absence values. | `npx skills add lucaswilliameufrasio/agent-skills --skill explicit-code-style --global` |
| [`conventional-commits`](skills/conventional-commits/SKILL.md) | Draft and review Conventional Commit messages without committing without authorization. | `npx skills add lucaswilliameufrasio/agent-skills --skill conventional-commits --global` |
| [`semantic-versioning`](skills/semantic-versioning/SKILL.md) | Choose and validate version changes against SemVer 2.0.0 and project release rules. | `npx skills add lucaswilliameufrasio/agent-skills --skill semantic-versioning --global` |
| [`http-api-conventions`](skills/http-api-conventions/SKILL.md) | Standardize JSON contracts, error bodies/statuses, pagination, and safe API boundaries. | `npx skills add lucaswilliameufrasio/agent-skills --skill http-api-conventions --global` |
| [`opencode-session-inventory`](skills/opencode-session-inventory/SKILL.md) | Inventory active OpenCode processes and sessions, then map verified relationships to Herdr workspace and tab labels. | `npx skills add lucaswilliameufrasio/agent-skills --skill opencode-session-inventory --global` |
| [`git-delivery`](skills/git-delivery/SKILL.md) | Coordinate branch, commit, PR, CI, and release handoff using each repository's rules. | `npx skills add lucaswilliameufrasio/agent-skills --skill git-delivery --global` |
| [`persistent-worktrees`](skills/persistent-worktrees/SKILL.md) | Keep Git worktrees and agent workspaces on persistent storage; default to `~/git-worktrees`, never temporary or RAM-backed paths. | `npx skills add lucaswilliameufrasio/agent-skills --skill persistent-worktrees --global` |
| [`github-gitea-actions`](skills/github-gitea-actions/SKILL.md) | Create and audit GitHub/Gitea Actions workflows with freshly verified, current, and securely pinned action dependencies. | `npx skills add lucaswilliameufrasio/agent-skills --skill github-gitea-actions --global` |
| [`jira-issue-writing`](skills/jira-issue-writing/SKILL.md) | Create complete, privacy-safe Jira issues with duplicate checks, end-to-end scope, repository-specific technical solutions, and verifiable acceptance criteria. | `npx skills add lucaswilliameufrasio/agent-skills --skill jira-issue-writing --global` |
| [`document-decisions`](skills/document-decisions/SKILL.md) | Record durable decisions in the repository's existing documentation structure. | `npx skills add lucaswilliameufrasio/agent-skills --skill document-decisions --global` |
| [`testing-quality-gate`](skills/testing-quality-gate/SKILL.md) | Compatibility entry point that delegates testing policy to `testing-standard`. | `npx skills add lucaswilliameufrasio/agent-skills --skill testing-quality-gate --global` |
| [`testing-standard`](skills/testing-standard/SKILL.md) | Apply repository testing policy for unit, integration, regression, safe execution, coverage, and full quality-gate verification. | `npx skills add lucaswilliameufrasio/agent-skills --skill testing-standard --global` |
| [`cross-repo-standard-sync`](skills/cross-repo-standard-sync/SKILL.md) | Define canonical ownership and safely audit or sync shared standards while preserving repo-specific facts. | `npx skills add lucaswilliameufrasio/agent-skills --skill cross-repo-standard-sync --global` |
| [`privacy-safe-skill-extraction`](skills/privacy-safe-skill-extraction/SKILL.md) | Generalize internal workflows into reusable skills and screen all artifacts for private information before sharing. | `npx skills add lucaswilliameufrasio/agent-skills --skill privacy-safe-skill-extraction --global` |
| [`shell-docker-preflight`](skills/shell-docker-preflight/SKILL.md) | Verify the login and execution shells, detect Docker daemon mode, and prefer rootless access without silent escalation. | `npx skills add lucaswilliameufrasio/agent-skills --skill shell-docker-preflight --global` |
| [`secrets-safety`](skills/secrets-safety/SKILL.md) | Protect credentials during development, infrastructure changes, and incident response. | `npx skills add lucaswilliameufrasio/agent-skills --skill secrets-safety --global` |
| [`credential-lifecycle-and-rotation`](skills/credential-lifecycle-and-rotation/SKILL.md) | Design enrollment, secure custody, recoverable renewal, rotation, revocation, and actual consumer adoption. | `npx skills add lucaswilliameufrasio/agent-skills --skill credential-lifecycle-and-rotation --global` |
| [`runtime-configuration-and-policy`](skills/runtime-configuration-and-policy/SKILL.md) | Separate typed settings/policy authoring, versioned publication, runtime adoption, and operational activation. | `npx skills add lucaswilliameufrasio/agent-skills --skill runtime-configuration-and-policy --global` |
| [`migration-parity-audit`](skills/migration-parity-audit/SKILL.md) | Audit behavioral parity across APIs, workers, data, and clients; separate evidence-backed replacement from approved cutover. | `npx skills add lucaswilliameufrasio/agent-skills --skill migration-parity-audit --global` |
| [`backup-restore-drills`](skills/backup-restore-drills/SKILL.md) | Prove scoped recoverability with consistent recovery sets, isolated restores, integrity checks, and bounded failure drills. | `npx skills add lucaswilliameufrasio/agent-skills --skill backup-restore-drills --global` |
| [`isolated-worker-execution`](skills/isolated-worker-execution/SKILL.md) | Build enforceable execution boundaries, bounded process trees, safe cancellation, and privacy-preserving evidence promotion. | `npx skills add lucaswilliameufrasio/agent-skills --skill isolated-worker-execution --global` |
| [`system-module-architecture`](skills/system-module-architecture/SKILL.md) | Plan and build journey-first systems, backoffices, modules, screens, and integration boundaries. | `npx skills add lucaswilliameufrasio/agent-skills --skill system-module-architecture --global` |
| [`web-capability-architecture`](skills/web-capability-architecture/SKILL.md) | Structure web features, data sources, and validated API boundaries around domain capabilities. | `npx skills add lucaswilliameufrasio/agent-skills --skill web-capability-architecture --global` |
| [`vps-blue-green-prepare`](skills/vps-blue-green-prepare/SKILL.md) | Prepare project-specific blue-green VPS deployment scripts and runbooks without executing a deployment. | `npx skills add lucaswilliameufrasio/agent-skills --skill vps-blue-green-prepare --global` |
| [`vps-deploy-executor`](skills/vps-deploy-executor/SKILL.md) | Safely execute an approved VPS deployment after inspecting shared-host services and protecting unrelated applications. | `npx skills add lucaswilliameufrasio/agent-skills --skill vps-deploy-executor --global` |
| [`backpressure-and-admission-control`](skills/backpressure-and-admission-control/SKILL.md) | Bound accepted work and protect services with explicit overload, rate, concurrency, and fairness policies. | `npx skills add lucaswilliameufrasio/agent-skills --skill backpressure-and-admission-control --global` |
| [`resilient-async-workflows`](skills/resilient-async-workflows/SKILL.md) | Make asynchronous work recoverable with deadlines, bounded retries, idempotency, and durable acceptance. | `npx skills add lucaswilliameufrasio/agent-skills --skill resilient-async-workflows --global` |
| [`graceful-shutdown-drain`](skills/graceful-shutdown-drain/SKILL.md) | Stop intake and safely drain in-flight work during shutdown within an explicit deadline. | `npx skills add lucaswilliameufrasio/agent-skills --skill graceful-shutdown-drain --global` |
| [`performance-optimization`](skills/performance-optimization/SKILL.md) | Find and remove measured bottlenecks, then verify gains and guardrails under comparable conditions. | `npx skills add lucaswilliameufrasio/agent-skills --skill performance-optimization --global` |
| [`performance-benchmarking-and-load-testing`](skills/performance-benchmarking-and-load-testing/SKILL.md) | Build repeatable benchmarks and load tests for performance, saturation, and capacity. | `npx skills add lucaswilliameufrasio/agent-skills --skill performance-benchmarking-and-load-testing --global` |
| [`performance-profiling-ebpf`](skills/performance-profiling-ebpf/SKILL.md) | Profile measured bottlenecks with runtime tools and optional, safely scoped eBPF/perf diagnostics. | `npx skills add lucaswilliameufrasio/agent-skills --skill performance-profiling-ebpf --global` |
| [`rust-cross-platform-builds`](skills/rust-cross-platform-builds/SKILL.md) | Accelerate and validate Rust cross-platform release builds with Zig/cargo-zigbuild and controlled benchmarks. | `npx skills add lucaswilliameufrasio/agent-skills --skill rust-cross-platform-builds --global` |
| [`create-verification-skill`](skills/create-verification-skill/SKILL.md) | Create a project-local, harness-native skill to drive real app workflows and preserve observable verification evidence. | `npx skills add lucaswilliameufrasio/agent-skills --skill create-verification-skill --global` |

Each first-party skill lives in its own directory and contains a `SKILL.md` with frontmatter. The [Skills CLI](https://github.com/vercel-labs/skills) installs selected skills into the agent directories it manages.

## Completion and testing policy

`task-completion` owns the portable execution and handoff workflow;
`testing-standard` is the canonical testing policy in this collection.
When persistent context is authorized, `context-checkpoint` owns saving and
recovering the working plan at material boundaries where the user's selected
store supports active-task records. It verifies writes and does not treat memory
as fresh authorization. ai-memory-specific guidance uses documented retrieval
and observations, not durable wiki pages or mid-session handoffs for transient
plans; unsupported persistence requires a user-approved suitable backend.
No automatic compaction hook is installed or promised.
`testing-quality-gate`, `quality-gate`, and `test-strategy` are compatibility
entry points, not independent testing policies. `git-workflow` delegates to
`git-delivery` and `conventional-commits`; process requirements never grant
delivery permissions. If installing entry points individually, also install the
skills they reference; the installer does not resolve these dependencies.
Repository-specific commands, mandatory checks, and approved exceptions remain
owned by each target repository.

Installing a skill makes it available to the selected harness; it does not
guarantee activation or enforce a runtime stop condition. This collection does
not require a global harness configuration or plugin.

Existing installations may contain older, separately maintained copies of the
compatibility names above. Before replacing them, back them up privately and
review local rules and intended exceptions. Resolve whether unrelated failures
may be repaired and which delivery actions require authorization. Keep private
or project-specific conventions in their owner's source, not in this public
collection. A backup preserves history; it does not make a retired policy active.
Do not automatically delete other installed skills.

`git-workflow` and `test-strategy` can read an optional, user-owned
`references/local-conventions.md` in their installed directories. This is a
private migration supplement, not a second permission or testing policy. Keep
it out of public packages and preserve it when reinstalling, since an installer
may replace the whole destination directory. Repository instructions and
explicit authorization still govern.

### Evaluating completion behavior

See [`skills/task-completion/evals/README.md`](skills/task-completion/evals/README.md)
for scenario checks and tool-enabled fixtures. Give evaluated agents only the
selected prompt and fixture, not expected outputs, assertions, or grading code.
Keep baseline and with-skill workspaces separate and grade artifacts as well as
the final report. Passing a handoff scenario is not evidence of actual execution
or automatic skill activation.

### Evaluating operational workflows

See [workflow skill evaluations](docs/workflow-skill-evaluations.md) for the five
operational skills' ownership boundaries, synthetic scenarios, paired design
checks, aggregate results, and privacy/validation limits. Raw evaluation outputs
and source-memory details stay outside this public repository.

## Third-party skill recommendations

These are upstream skills discovered in the public Skills ecosystem. They are **not copied or republished here**; install directly from their maintainers with `npx skills`:

| Upstream | Recommended skills | Install |
| --- | --- | --- |
| [anthropics/skills](https://github.com/anthropics/skills) | `frontend-design` | `npx skills add anthropics/skills --skill frontend-design` |
| [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) | `security-audit` — source-first security reviews with coverage tracking, independent finding verification, and evidence-based reporting. | `npx skills add cloudflare/security-audit-skill --skill security-audit` |
| [majidmanzarpour/threejs-game-skills](https://github.com/majidmanzarpour/threejs-game-skills) | `threejs-gameplay-systems` | `npx skills add https://github.com/majidmanzarpour/threejs-game-skills --skill threejs-gameplay-systems` |
| [mattpocock/skills](https://github.com/mattpocock/skills) | `code-review`, `diagnosing-bugs`, `grill-me`, `grill-with-docs`, `improve-codebase-architecture`, `tdd` | `npx skills add mattpocock/skills --skill <name>` |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | `web-design-guidelines` | `npx skills add vercel-labs/agent-skills --skill web-design-guidelines` |
| [vercel-labs/skills](https://github.com/vercel-labs/skills) | `find-skills` | `npx skills add vercel-labs/skills --skill find-skills` |
| [juliusbrussee/caveman](https://github.com/juliusbrussee/caveman) | `caveman` | `npx skills add juliusbrussee/caveman --skill caveman` |
| [dart-lang/skills](https://github.com/dart-lang/skills) | Dart language and tooling skills | `npx skills add dart-lang/skills --skill <name>` |
| [flutter/skills](https://github.com/flutter/skills) | Flutter development and testing skills | `npx skills add flutter/skills --skill <name>` |
| [flutter/agent-plugins](https://github.com/flutter/agent-plugins) | Additional Flutter workflow skills | `npx skills add flutter/agent-plugins --skill <name>` |
| [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | `golang-patterns` | `npx skills add affaan-m/everything-claude-code --skill golang-patterns` |
| [jeffallan/claude-skills](https://github.com/jeffallan/claude-skills) | `golang-pro` | `npx skills add jeffallan/claude-skills --skill golang-pro` |
| [apollographql/skills](https://github.com/apollographql/skills) | `rust-best-practices` | `npx skills add apollographql/skills --skill rust-best-practices` |
| [wshobson/agents](https://github.com/wshobson/agents) | `rust-async-patterns` | `npx skills add wshobson/agents --skill rust-async-patterns` |
| [sveltejs/ai-tools](https://github.com/sveltejs/ai-tools) | Svelte authoring and best-practice skills | `npx skills add sveltejs/ai-tools --skill <name>` |
| [huntabyte/shadcn-svelte](https://github.com/huntabyte/shadcn-svelte) | `shadcn-svelte` | `npx skills add huntabyte/shadcn-svelte --skill shadcn-svelte` |
| [onmax/nuxt-skills](https://github.com/onmax/nuxt-skills) | Vue, Nuxt, Vite, Vitest, VueUse, TresJS, and pnpm skills | `npx skills add onmax/nuxt-skills --skill <name>` |
| [github/awesome-copilot](https://github.com/github/awesome-copilot) | PostgreSQL and SQL review/optimization skills | `npx skills add github/awesome-copilot --skill <name>` |
| [`ui-ux-pro-max`](https://www.skills.sh/nextlevelbuilder/ui-ux-pro-max-skill/ui-ux-pro-max) ([upstream](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)) | `ui-ux-pro-max` | `npx skills add nextlevelbuilder/ui-ux-pro-max-skill --skill ui-ux-pro-max` |
| [heliocosta-dev/revenue-centric-design](https://github.com/heliocosta-dev/revenue-centric-design) | `revenue-centric-design` — SaaS product design for conversion, onboarding, pricing, retention, and monetization; not for gambling, betting, or casino products. | `npx skills add heliocosta-dev/revenue-centric-design` |
| [Stripe's official skills](https://docs.stripe.com/skills) | Stripe integration guidance | `npx skills add https://docs.stripe.com` |

Use `npx skills add <owner/repo> --list` to check the upstream repository's current skill names before installing. Third-party skills remain maintained by their authors; review their content and permissions before use.

Cloudflare's full `security-audit` workflow requires subagents and Node.js validators. Executing target-controlled code additionally requires the upstream's OS-enforced sandbox controls; without them, keep source-grounded leads as needing validation rather than running code or probing live services. Adding this recommendation does not install the skill or authorize an audit.

Only first-party skills reviewed for public reuse are stored in this repository. Project-specific skills and files from private repositories are not copied here.
