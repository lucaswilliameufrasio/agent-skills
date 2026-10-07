---
name: vps-deploy-executor
description: >-
  Safely execute or troubleshoot an authorized application deployment on a VPS,
  especially a blue-green release on a shared host. Use whenever a user asks to
  deploy, switch traffic, roll back, or run a release on a VPS. Inspect the host
  and deployment ownership before changes, protect unrelated applications, show
  the exact proposed actions and impact, and obtain explicit approval before any
  mutation. This skill is for execution; use vps-blue-green-prepare to create
  deployment scripts and documentation without deploying.
---

# Execute a VPS deployment safely

Assume every VPS may be shared with other applications. A deployment request
authorizes work only on the identified application and release; it does not
authorize stopping, reconfiguring, or cleaning up other services. Prefer
read-only discovery first. Never promise zero downtime.

## 1. Identify scope and inspect before changing anything

Confirm the target host/environment, application, intended version, and the
user's authority to deploy. Read the project's `DEPLOY.md`, deployment script,
service/proxy configuration, and rollback procedure. Do not run an unknown
script simply because it is named `deploy`.

Before any mutation, perform a bounded, read-only preflight using authorized
access. Establish only what is needed to protect the target and its neighbors:

- Running services and containers, relevant processes, listening ports, and
  resource/disk capacity.
- The target app's current release, service identity, health, traffic path, and
  ownership of relevant files and configuration.
- Shared reverse-proxy configuration and upstreams, without dumping unrelated
  application configuration or secret values.
- Whether the proposed inactive slot, ports, paths, service names, networks, or
  resources conflict with existing workloads.
- Whether the version requires database or shared-state changes, and whether
  old and new versions can coexist.

Use available SSH/host-management access only when the user asks to execute and
the target is clear. If access is absent, explain the safe read-only commands
the user can run and wait for their results. Do not infer that a host is
dedicated or that a service belongs to the target app from its name alone.

Do not read or print secret values from environment files, credentials, or
stores. Avoid broad dumps of process arguments, environment, proxy config, or
logs that could expose secrets. Redact diagnostic output before sharing it.

## 2. Present the plan and get explicit approval

Before the first write, restart, reload, traffic switch, migration, or cleanup,
show the user a concise plan containing:

1. The host/environment and exact target application/release.
2. What the preflight found about current and neighboring services relevant to
   the operation; note uncertainty or conflicts.
3. Exact files, units/containers, ports, and proxy resources that will change.
4. Ordered actions, expected user-visible impact, health checks, and timeout.
5. The rollback trigger and exact rollback path, including limits from database
   or shared-state changes.
6. Any backup/snapshot and cleanup action proposed.

Ask for explicit approval of this specific plan. General authorization to
"deploy" is not approval for an undisclosed migration, proxy rewrite, service
restart, destructive cleanup, or action affecting another workload. If the
scope changes materially during execution, pause and obtain approval again.

If target ownership, traffic routing, port availability, or service impact
cannot be established safely, stop and ask; do not improvise on a shared host.

## 3. Execute only the approved, scoped plan

After approval:

1. Capture the current active release and the minimum safe rollback metadata.
   Back up only files/configuration in scope; do not copy secret values into
   logs or chat.
2. Use the project's documented, reviewed deployment procedure. Prefer an
   immutable inactive release; do not overwrite the active release in place.
3. Start the inactive slot and wait for its bounded health/readiness check.
   Until it passes, do not move traffic or stop the active slot.
4. Validate any proxy change before applying it. Change only the approved target
   upstream/include; preserve unrelated virtual hosts and services. Use a
   graceful reload only when supported and confirmed by the host configuration.
5. Verify the new version via the real traffic path and check relevant service
   health. Report the observed evidence, not just a successful command exit.
6. If startup, switching, or verification fails, stop progression. If rollback
   was approved in the plan and remains safe, restore traffic to the previous
   healthy release and verify it. Otherwise pause and ask before taking a new
   action. Never hide a failed health check.
7. Keep the previous release available. Treat deletion, pruning, data cleanup,
   and removal of old service definitions as separate actions requiring their
   own explicit approval.

Do not perform an irreversible or incompatible database migration without
explicit approval of its data impact and recovery plan. An app rollback does
not undo a schema or data migration. Never stop or restart a neighboring app to
make room; report the conflict and ask for an operator decision.

## 4. Report completion accurately

Report the target and version, actions completed, health/traffic verification,
whether the previous release remains available, any rollback or migration,
redacted errors, and unresolved risks. Distinguish completed actions from
unverified assumptions. Do not claim success if the real traffic path was not
checked or if a failed step remains unresolved.

## Safety checklist

- Target host, app, version, and ownership are unambiguous.
- Shared-host inventory and conflict checks happened before mutation.
- The user approved the specific plan before writes or service/traffic changes.
- No unrelated service, proxy route, data, or secret was changed or exposed.
- The new slot passed health checks before traffic moved.
- Rollback remains possible and is verified when used.
- Destructive cleanup and incompatible data changes were not implicit.
