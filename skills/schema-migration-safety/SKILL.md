---
name: schema-migration-safety
description: >-
  Create, review, or run database schema and data migrations safely. Use
  whenever a change adds, alters, renames, or drops tables, columns, indexes,
  constraints, or enums, backfills data, or touches migration files, ORMs, or
  migration tools, and whenever a deploy depends on a schema change or uses
  blue-green or rolling releases. Generate timestamped up/down migrations with
  the project's own CLI, keep old and new code compatible, and rehearse risky
  migrations on a restored copy before production.
---

# Schema migration safety

A migration is a deploy of the database. It runs against live data, often
while old and new application versions are both serving traffic, and it is the
hardest part of a release to roll back. Treat it with the same care as code.

## Discover the project's migration contract

Read repository instructions, the migration directory, tool configuration,
existing migrations, CI, and deploy scripts. Determine:

- the migration tool and its CLI (framework, ORM, or standalone tool) and the
  exact command used to create, apply, roll back, and show status;
- the naming and ordering scheme (timestamp or sequence), file layout, and
  whether up and down live in one file or two;
- how and when migrations run in deployment (pre-deploy hook, release step,
  application startup, manual) and whether old and new versions overlap;
- database engine and version, table sizes for touched tables, and replication
  or read replicas that the change could lag.

Do not invent a tool or a layout. If the repository has none and needs one, it
is a decision to make with the user (`document-decisions`).

## Create migrations with the CLI

- **Generate every migration file with the project's migration CLI**, never by
  hand-crafting the filename or copying an older file. The CLI assigns the
  timestamp or version, the ordering, the template, and any checksum or
  metadata the tool tracks. If the CLI is not installed, install the version
  the project pins, or ask; do not hand-write a substitute.
- **Use timestamped versions** when the tool supports them, so parallel
  branches do not collide. If the project uses sequential numbers, follow it,
  and resolve conflicts by regenerating rather than renumbering applied files.
- **Write both up and down.** The down migration reverses the up exactly, or
  explicitly states why it cannot (for example, destroyed data) and what the
  recovery path is instead. Test down, then up again, locally.
- **Never edit a migration that has been applied in a shared environment.**
  Write a new one. A changed checksum or silently diverged schema is worse than
  an extra file.
- After schema changes, regenerate derived artifacts (ORM models, typed query
  code, schema dumps) with their own generators and commit them together.

## Keep old and new code compatible (expand, migrate, contract)

During a rolling or blue-green deploy, the old version runs against the new
schema. Split breaking changes into releases:

1. **Expand**: add new tables, nullable columns, or columns with safe defaults;
   add new indexes without blocking writes. Old code keeps working.
2. **Migrate**: deploy code that writes both shapes (or the new shape with a
   compatibility read); backfill existing rows in bounded, resumable batches
   outside the schema migration when large.
3. **Contract**: once no running version uses the old shape, drop or rename it
   in a later release.

A rename is an add plus a backfill plus a drop, not one statement. Changing a
column type, adding `NOT NULL`, or adding a foreign key to a populated table
usually needs the same split, or a validate-later constraint where the engine
supports it.

## Assess locking and duration

For each statement, check from the engine's current documentation what lock it
takes and whether it rewrites the table. Common hazards: table rewrites on type
changes, index builds that block writes (use the engine's concurrent/online
option, which may not run inside a transaction), long transactions holding
locks behind which every query queues, and backfills that saturate I/O or
replication. Set a lock timeout and statement timeout for the migration session
where the engine supports it, so it fails fast instead of stalling traffic.

## Rehearse on a restored copy

For anything beyond a trivial additive change on small tables, rehearse before
production:

1. Restore a recent backup of the target database into a **separate, isolated
   instance** with comparable engine version and settings, following
   `backup-restore-drills` (approval for real data, no outbound effects,
   private destination).
2. Apply the up migration with timing; record lock waits, duration, table
   growth, and replication lag.
3. Run the application's critical reads against the migrated copy, then apply
   down and confirm the schema and data return to the previous state, then up
   again.
4. Destroy the rehearsal instance when done, unless retention was agreed.

When real data cannot be used, rehearse on a synthetic dataset sized like
production and say so in the report.

## Apply

- Take or confirm a recent recoverable backup immediately before a risky
  migration; know the restore time.
- Apply through the deploy path the project already uses. Do not run
  migrations against shared or production databases from a workstation unless
  that is the documented, approved path.
- Watch errors, lock waits, latency, and replication while it runs; know the
  abort condition in advance.
- Production migrations need explicit authorization; a merged PR is not that
  authorization unless the repository's deploy policy says so.

## Review checklist

- Generated by the CLI, timestamped/ordered per the tool, with up and down.
- Down tested locally; irreversible steps documented with a recovery path.
- Old code works with the new schema, and new code with the old during deploy.
- Locks, rewrites, and duration assessed; timeouts set; large backfills batched.
- Rehearsed on a restored copy when risky, with measured timings.
- Derived code regenerated; integration tests run against a real local database
  (`testing-standard`).

Report the migration files and commands used, compatibility plan, lock
assessment, rehearsal results or why skipped, backup status, and what still
needs approval to run.
