---
name: pipeline-latency
description: >-
  Make CI, CD, and other automation workflows (PR checks, deploys, releases,
  scheduled jobs) faster without letting them lie. Use whenever the user says CI
  or a deploy is slow, asks to reduce pipeline time or cost, wants faster PR
  feedback, mentions queue time, runners, caching, sharding, test selection, or
  a merge queue, on any CI platform, runner provider, or stack. Understand what
  each workflow guarantees, measure where time goes, estimate its floor, then
  remove overhead one measured change at a time.
---

# Pipeline latency

A pipeline is fast when it reaches a trustworthy result quickly. Speed that
comes from hiding failures, skipping guarantees, or turning a deploy green
before it finished is a regression, however good the chart looks.

This skill is platform-, provider-, and stack-agnostic. Never prescribe a runner
vendor, package manager, linter, or test runner before the project is
understood and measured. Stack-specific techniques live in
[references](references/stack-techniques.md) and are candidates, not defaults.

## Rules that outrank speed

1. **Never get faster by hiding failures.** No new retries, wider timeouts,
   skipped or quarantined tests, `continue-on-error`, or weaker assertions to
   save time. A check that needs a retry has a bug; find it
   (`flaky-test-diagnosis`).
2. **Keep the guarantee before main and before production.** Narrowing work on
   pull requests (affected-only, test selection) is acceptable only when the
   full required suite still runs before code reaches the protected branch or
   a deployment (merge queue, post-merge gate, or release gate). If no such
   gate exists, adding it comes before adding selection.
3. **A deploy is done when the target reports it is done.** Do not drop
   waiters, health checks, smoke tests, or rollback triggers. Hot-swap or
   drift-creating shortcuts are for disposable development environments only,
   and only when the user approves them.
4. **Do not cancel deploys in flight.** Cancel superseded PR checks freely, but
   serialize deploy and release workflows (queue them) so a half-applied change
   is never abandoned.

## 1. Understand each workflow first

Read the workflows, reusable/composite pieces, scripts they call, repository
instructions, branch protection or required checks, and deployment targets. For
each workflow in scope record:

- trigger, who waits on it, and what decision it gates (merge, deploy, release);
- what it proves (build, lint, types, tests, migrations, security, packaging)
  and which of those are required;
- the critical path: which jobs run in sequence and which already run in
  parallel; total duration is the critical path, not the sum of jobs;
- external steps whose duration the pipeline does not control (cloud
  deployment APIs, image registries, package registries, app stores).

Do not apply a uniform target across workflows. A deploy of one small function
and a deploy that updates several stacks have different floors.

## 2. Measure where time goes

Pull enough recent runs to see distributions (typically the last 50 to 150 per
workflow, fewer for rare workflows) through the platform's API or CLI. Split
every job into:

| Bucket | Meaning |
| --- | --- |
| Waiting | Trigger to job start: queue, runner provisioning, concurrency limits |
| Setup | Start to first useful command: checkout, toolchain, dependencies, caches, services |
| Running | The useful work: build, checks, tests, packaging, deploy calls |
| External wait | Time blocked on a remote system (deploy waiters, registry pushes) |

Report p50 and p95 per bucket and per step, and the critical path at p50 and
p95. Note cache hit rates and runner types. Fix the biggest bucket first; it is
rarely the tests themselves.

### Estimate the floor

For each workflow, estimate the irreducible time: the external waits plus the
minimum useful work on a warm, well-sized runner. The target is the floor plus
an agreed overhead margin, not a number copied from elsewhere. Show the gap:
"floor ~70 s, current p50 180 s, overhead 110 s: 45 s setup, 40 s rebuild, 25 s
queue". When the floor itself dominates, say so; further gains require changing
what is deployed or how, which is a design decision for the user.

## 3. Remove overhead by bucket

Generate candidates from the measurements, then rank by expected gain, risk,
and cost.

**Waiting.** Concurrency groups that cancel superseded PR runs; enough runner
capacity for peak pushes; avoid serial fan-in jobs that only wait. Treat the
runner as a decision across classes, not a vendor: platform-hosted, third-party
managed runners, self-hosted ephemeral, or self-hosted persistent. Compare on
measured queue and setup time, CPU/memory per price, cache locality, egress,
architecture support, and security. Self-hosted runners on public repositories
or untrusted PRs need isolation; persistent runners can leak state between
jobs. Moving providers needs an account and a bill: put it on the user's list.

**Setup.** Cache what is expensive to rebuild, keyed on lockfiles and toolchain
versions; seed caches from the default branch so PR runs hit; measure hit rates.
Cache resolved dependency directories or build outputs when restoring them is
safe and faster than reinstalling. Use partial clones or sparse checkout when
history or the full tree is unnecessary, and fetch depth that keeps the tools
that need history (versioning, affected detection) working. Preinstall stable
toolchains in runner images when the platform allows. Start service containers
in parallel with other setup.

**Running.** Split independent checks into parallel jobs; move unrelated work
off the slowest job; shard tests by measured duration, not file count; buy cores
before adding shards, and match test concurrency to cores. Build once and pass
the artifact to later jobs or stages instead of rebuilding. For tool swaps
(faster linter, formatter, type checker, package manager, bundler, test runner),
run old and new side by side on the same commit and list everything the new one
misses or reports differently before switching. The new tool must keep the
rules and guarantees the team relies on, or the gap must be approved.

**External wait and deploys.** Promote the artifact already built and tested by
CI instead of rebuilding it for deployment. Deploy only units whose inputs
changed, with a reliable change detection that falls back to deploying all.
Run independent stacks or functions in parallel where the tool supports it and
the dependency order allows. Skip work the target already has (unchanged
images, layers, assets) by content hash. Keep the waiters.

**Selection on PRs.** Use the build system's own affected/dependency graph when
it has one. Then prove it is safe: hide a real breaking change in a dependency
of an affected package and confirm the PR goes red, not green. Keep the full
suite in the gate before main.

## 4. Change one thing at a time

1. State the hypothesis and expected gain per bucket before editing.
2. Make the smallest change; one pull request per change.
3. Collect before/after numbers from real runs on comparable commits, enough
   runs to see past noise. Report p50 and p95, not the best run.
4. Confirm no guarantee was lost: same checks required, same failures caught.
   Deliberately break something the changed job should catch and see it fail.
5. Keep, revise, or revert based on evidence.

Use `performance-optimization` for the measurement discipline and
`github-gitea-actions` whenever a workflow's `uses:` references change.

## 5. Keep it fast

Record each workflow's budget per bucket next to the workflow or in the
repository's CI documentation. Prefer a trend report or alert on p95 drift over
failing jobs that exceed a budget, which turns noisy runners into flaky
failures. Keep job timeouts as protection against hangs, set generously above
p95. Offer fast local feedback through `local-fast-gates` so CI is not the first
place format and lint errors appear.

## Report

Per workflow: what it guarantees, floor estimate, before/after critical path at
p50/p95 by bucket, changes made (one per PR) with evidence, guarantees verified,
and remaining overhead. Then one list of actions that need the user: accounts,
secrets, paid runners, larger machines, or branch-protection changes, each with
expected time saved and expected monthly cost. End with total pipeline time and
cost before and after, labelled as measured or estimated.
