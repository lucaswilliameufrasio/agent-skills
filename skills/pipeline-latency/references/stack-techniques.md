# Stack-specific candidates

Candidates to test against measurements, never defaults. Tools change fast:
check each one's current stable release, maintenance status, and compatibility
with the repository before proposing it, and compare side by side before any
switch. Load only the sections that match the project.

## JavaScript / TypeScript

- Cache the resolved dependency directory keyed on the lockfile when restoring
  it is faster than a clean install; keep a clean install on cache miss.
- Use the workspace tool's affected graph (if the repository already uses one)
  for PR selection; keep the full run in the gate.
- Faster linters, formatters, and type checkers exist (native-code
  implementations); verify rule coverage against the current config and list
  rules without an equivalent before switching.
- Test runners: run files in parallel up to the core count; module isolation
  per file costs time, and disabling it requires explicit state reset between
  files and a random-order run to flush leaks.
- Bundled deploy artifacts (for example a single bundled function) are smaller
  to upload and faster to cold start than shipping the dependency directory.

## Rust

- Cache the cargo registry and the target directory keyed on the lockfile and
  toolchain; consider a compiler cache when targets are rebuilt across jobs.
- Split `check`/`clippy` from `test`; use a faster test runner if the project
  already accepts it; build tests once and run shards from the archive.
- Cross-compile instead of emulating the target architecture; see
  `rust-cross-platform-builds`.
- Pin the toolchain in `rust-toolchain.toml` so cache keys are stable.

## Go

- Cache the module and build caches keyed on `go.sum` and the Go version.
- `go vet` and the linter can run in parallel with tests; the linter has its own
  cache directory.
- Run packages in parallel (`-p`) sized to cores; shard by package durations.

## Python

- Cache the resolver/installer cache and, where safe, the virtual environment
  keyed on the lockfile and interpreter version. Faster installers and resolvers
  exist; confirm lockfile compatibility first.
- Parallelize tests with the project's plugin if present; ensure fixtures do
  not share a database or files across workers.

## Containers

- Order Dockerfile layers from least to most frequently changed; use cache
  mounts for package managers; export/import build cache to a registry or the
  CI cache.
- Build once per commit, tag by content or commit, and promote the same image
  through environments.
- Build for the target architecture natively or by cross-compiling; avoid
  compiling under emulation.

## Serverless and infrastructure as code

- Measure the deploy tool's own phases: synthesis/packaging, upload, change-set
  creation, apply, and waiters. The apply and waiter phases are usually the
  floor.
- Skip unchanged functions or stacks by content hash of their inputs, with a
  fallback to deploy everything when detection is uncertain.
- Upload code artifacts directly when the infrastructure did not change, if
  the team accepts that path and it keeps versioning, aliases, and rollback
  intact; otherwise keep the change-set path.
- Deploy independent stacks in parallel when dependency order allows.
- Hot-swap modes bypass the provisioning engine and cause drift: development
  environments only, with approval.
- Keep waiters and post-deploy smoke checks; a deploy that returns before the
  function is updated and healthy is not faster, it is unverified.

## Mobile and desktop

- Cache dependency managers and derived data keyed on lockfiles and toolchain
  versions; separate signing/notarization (external wait) from build time.
- Run UI tests on the minimum device matrix for PRs and the full matrix in the
  gate before release.
