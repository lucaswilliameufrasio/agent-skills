# Eufrasio's Agent Skills

A curated collection of reusable agent skills maintained in public.

## Skills

| Skill | Description |
| --- | --- |
| [`pr-merge-sequence`](skills/pr-merge-sequence/SKILL.md) | Safely sequence normal GitHub PR merges while rebasing and revalidating remaining branches after each merge. |
| [`single-state-enum`](skills/single-state-enum/SKILL.md) | Model mutually-exclusive UI overlays and modes with one discriminated-union state. |
| [`explicit-code-style`](skills/explicit-code-style/SKILL.md) | Prefer multiline conditionals, explicit loops, and clear absence values. |
| [`conventional-commits`](skills/conventional-commits/SKILL.md) | Draft and review Conventional Commit messages without committing without authorization. |
| [`semantic-versioning`](skills/semantic-versioning/SKILL.md) | Choose and validate version changes against SemVer 2.0.0 and project release rules. |
| [`http-api-conventions`](skills/http-api-conventions/SKILL.md) | Standardize JSON contracts, error bodies/statuses, pagination, and safe API boundaries. |
| [`git-delivery`](skills/git-delivery/SKILL.md) | Coordinate branch, commit, PR, CI, and release handoff using each repository's rules. |
| [`document-decisions`](skills/document-decisions/SKILL.md) | Record durable decisions in the repository's existing documentation structure. |
| [`testing-quality-gate`](skills/testing-quality-gate/SKILL.md) | Choose real unit/integration test boundaries and verify the full project quality gate. |
| [`secrets-safety`](skills/secrets-safety/SKILL.md) | Protect credentials during development, infrastructure changes, and incident response. |
| [`system-module-architecture`](skills/system-module-architecture/SKILL.md) | Plan and build journey-first systems, backoffices, modules, screens, and integration boundaries. |
| [`vps-blue-green-prepare`](skills/vps-blue-green-prepare/SKILL.md) | Prepare project-specific blue-green VPS deployment scripts and runbooks without executing a deployment. |
| [`vps-deploy-executor`](skills/vps-deploy-executor/SKILL.md) | Safely execute an approved VPS deployment after inspecting shared-host services and protecting unrelated applications. |
| [`backpressure-and-admission-control`](skills/backpressure-and-admission-control/SKILL.md) | Bound accepted work and protect services with explicit overload, rate, concurrency, and fairness policies. |
| [`resilient-async-workflows`](skills/resilient-async-workflows/SKILL.md) | Make asynchronous work recoverable with deadlines, bounded retries, idempotency, and durable acceptance. |
| [`graceful-shutdown-drain`](skills/graceful-shutdown-drain/SKILL.md) | Stop intake and safely drain in-flight work during shutdown within an explicit deadline. |
| [`performance-optimization`](skills/performance-optimization/SKILL.md) | Find and remove measured bottlenecks, then verify gains and guardrails under comparable conditions. |
| [`performance-benchmarking-and-load-testing`](skills/performance-benchmarking-and-load-testing/SKILL.md) | Build repeatable benchmarks and load tests for performance, saturation, and capacity. |
| [`performance-profiling-ebpf`](skills/performance-profiling-ebpf/SKILL.md) | Profile measured bottlenecks with runtime tools and optional, safely scoped eBPF/perf diagnostics. |

Each first-party skill lives in its own directory and contains a `SKILL.md` with frontmatter. Install skills from this repository with the [Skills CLI](https://github.com/vercel-labs/skills):

```sh
npx skills add lucaswilliameufrasio/agent-skills \
  --skill pr-merge-sequence \
  --skill single-state-enum \
  --skill explicit-code-style \
  --skill conventional-commits \
  --skill semantic-versioning \
  --skill http-api-conventions \
  --skill git-delivery \
  --skill document-decisions \
  --skill testing-quality-gate \
  --skill secrets-safety \
  --skill system-module-architecture \
  --skill vps-blue-green-prepare \
  --skill vps-deploy-executor \
  --skill backpressure-and-admission-control \
  --skill resilient-async-workflows \
  --skill graceful-shutdown-drain \
  --skill performance-optimization \
  --skill performance-benchmarking-and-load-testing \
  --skill performance-profiling-ebpf
```

Add `-g` for a global installation, or install an individual skill with one `--skill <name>` option. Skills are installed into the agent directories selected by the CLI.

## Third-party skill recommendations

These are upstream skills discovered in the public Skills ecosystem. They are **not copied or republished here**; install directly from their maintainers with `npx skills`:

| Upstream | Recommended skills | Install |
| --- | --- | --- |
| [anthropics/skills](https://github.com/anthropics/skills) | `frontend-design` | `npx skills add anthropics/skills --skill frontend-design` |
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
| [Stripe's official skills](https://docs.stripe.com/skills) | Stripe integration guidance | `npx skills add https://docs.stripe.com` |

Use `npx skills add <owner/repo> --list` to check the upstream repository's current skill names before installing. Third-party skills remain maintained by their authors; review their content and permissions before use.

Only first-party skills reviewed for public reuse are stored in this repository. Project-specific skills and files from private repositories are not copied here.
