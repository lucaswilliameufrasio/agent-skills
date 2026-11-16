---
name: flaky-test-diagnosis
description: >-
  Find and fix why a test passes and fails without code changes (order, shared
  state, time, async). Use when a test is intermittent or fails only in CI, or
  someone proposes retries, sleeps, or skipping it.
---

# Flaky test diagnosis

An intermittent failure is a real failure with a probability. Retries convert
it into hidden latency and hidden risk; sometimes the flake is the product's
race condition reaching users. Find the cause, then remove it.

## Do not hide it

Do not add retries, rerun-on-failure, longer timeouts, sleeps, skips, or
quarantine to make the signal go away. If the team needs CI unblocked while the
cause is investigated, quarantine is a visible, owned, time-boxed decision by
the user, with an issue linked from the test, and the test keeps running in a
non-blocking job so evidence keeps accumulating. Never lower an assertion to
make it pass.

## Gather evidence

1. Collect failing runs: the exact error, stack, seed, worker or shard, order,
   runner type, timing, and the commit. Compare with passing runs of the same
   commit. Look at CI history for the failure rate and when it started.
2. Note the test's dependencies: shared database or files, network, clock,
   randomness, concurrency, global or module-level state, environment
   variables, locale and time zone, external services, and ports.

## Reproduce

Try, in roughly this order, using the test runner's own options:

- run the test alone, many times in a loop, to estimate the rate;
- run the whole file and then the whole suite in **random order** with a fixed,
  recorded seed; replay the failing seed;
- run with the same parallelism and worker count as CI, and with more;
- run under CPU or I/O stress or a slower machine to widen timing windows;
- set the time zone, locale, and clock to CI's values, and to boundary times
  (midnight, month end, DST change, leap day);
- bisect the order: when a test fails only after others, halve the preceding
  set until the polluting test is found.

A reproduction rate, even 1 in 50, is enough to confirm a fix statistically
later. If it cannot be reproduced locally, add targeted diagnostics (state
dumps, timing, seed logging) to the test run, not to production code, and
collect more CI failures.

## Common causes and real fixes

| Cause | Fix |
| --- | --- |
| State leaking between tests (database rows, files, caches, module globals, mocks not restored) | Unique fixtures per test; reset state after every test or file; transaction rollback per test where the framework supports it |
| Order dependence (a test relies on another having run) | Make each test set up what it needs; run in random order permanently |
| Shared resources across parallel workers (same database, port, temp directory) | Isolate per worker: separate databases or schemas, ephemeral ports, unique temp dirs |
| Time: real clock, sleeps, time zones, boundary dates | Inject a clock; use fake timers; fix time zone in tests and assert in UTC |
| Waiting by sleeping instead of on a condition | Wait for the observable condition with a bounded deadline |
| Asynchronous work not awaited, unhandled promise or goroutine outliving the test | Await or join it; fail tests on unhandled async errors and leaked tasks |
| Randomness without a seed | Seed and log the seed; generate data deterministically |
| Unordered collections asserted in order | Sort or compare as sets |
| Network or external service | Fake at the protocol boundary (`testing-standard`) |
| Resource exhaustion (memory, file handles, connection pool) | Close resources; size pools; reduce concurrency to cores |
| A real race in the product | Fix the product code, add a regression test that reproduces the race deterministically when possible |

## Prove the fix

Run the previously failing reproduction enough times to make passing by chance
unlikely (state how many runs and the prior failure rate), run the full suite in
random order and in parallel, and run it repeatedly in CI if the flake only
appeared there. Keep random order and isolation checks on permanently so the
next leak fails fast. Record the cause in the commit, and remove any temporary
quarantine or diagnostics.

Report the failure rate before, the root cause with evidence, the fix, the
number of verification runs after, and any related tests with the same pattern.
