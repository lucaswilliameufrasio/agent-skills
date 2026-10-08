---
name: shell-docker-preflight
description: >-
  Use before running shell commands, scripts, CLI tools, or Docker workloads.
  Identify the configured login shell and the shell that will actually execute
  commands; inspect Docker CLI/daemon availability and determine whether access
  is rootless or rootful. Prefer a verified rootless Docker context whenever it
  supports the task. Do not assume Bash, switch persistent contexts, escalate
  privileges, or reconfigure Docker silently.
---

# Shell and Docker preflight

Prevent shell-syntax mistakes and unnecessary rootful container access by
checking the command environment before running task commands. The user's login
shell and an agent's command-execution shell can differ; identify both instead
of treating them as interchangeable.

## Identify the shell before commands

Before the first shell command in a task:

1. Inspect the execution tool's documented/configured shell without running a
   task command.
2. Identify the user's configured login shell from available environment or
   account metadata. Do not assume `$SHELL`, the current process name, or a
   `.bashrc` is authoritative by itself.
3. As part of this same initial preflight, check whether Docker CLI, rootless
   helpers, and an accessible rootless or rootful daemon are installed/available,
   as described below. Keep this check read-only; do not start Docker merely to
   determine its mode.
4. Record the distinction between the login shell and the shell that will
   execute commands. If metadata is unavailable, use only a minimal,
   read-only probe whose syntax is safe for the known executor; do not run the
   requested work until the executor is known.
5. Use syntax and quoting appropriate to the actual executor. If the command
   must run under the user's login shell, invoke that shell explicitly using
   its supported arguments. Otherwise prefer portable syntax where practical.
6. Never source shell startup files just to identify the shell; they can have
   side effects or expose environment values.

Keep the preflight result for the current host, user, container, and execution
tool. Before each command, use that verified executor; repeat the preflight if
any of those contexts changes. Do not execute commands through a different
shell implicitly.

## Check Docker mode before Docker operations

As part of the initial task preflight, and again if the host/user/daemon
context changes, determine whether Docker is installed/available and whether
the accessible daemon is rootless or rootful:

1. Check whether the Docker CLI exists. A CLI binary alone does not mean a
   daemon is installed, running, or accessible.
2. Inspect configured context names without printing endpoint details. Check
   rootless helpers/services only when supported by the host OS; do not assume
   systemd or a particular installation layout.
3. Query only the selected daemon's minimal security metadata, such as Docker
   `SecurityOptions`, using a formatted/read-only query. A `name=rootless`
   security option confirms that the connected daemon is rootless. A context
   named `rootless` or a rootless helper binary alone is not proof that its
   daemon is active.
4. Distinguish and report: CLI missing; CLI present but no daemon available;
   rootless daemon installed but inactive/unreachable; verified rootless
   daemon; or verified/likely rootful daemon. If mode cannot be established,
   say it is unknown instead of guessing.
5. Do not dump full `docker info`, context endpoints, environment variables, or
   daemon configuration into output; these may disclose private paths or
   infrastructure details.

## Choose the least-privileged usable daemon

- Prefer a verified rootless daemon for Docker commands whenever it supports
  the requested operation.
- When both modes are available, target the rootless context explicitly for
  the command (for example, with Docker's per-invocation `--context` option).
  Do not change the user's persistent default context just to run one task.
- If rootless cannot support a necessary feature, explain the limitation and
  ask before using rootful access when the operation is consequential. Do not
  silently fall back to rootful because a command failed.
- Never prepend `sudo` to Docker commands or change groups, socket permissions,
  daemon configuration, or user services as an automatic workaround.
- Do not install, enable, start, stop, or reconfigure a Docker daemon unless
  explicitly requested. Running a daemon or container is a separate action
  from detecting its mode.
- Treat destructive operations (pruning, deleting volumes, removing images or
  containers, changing networks/volumes) as requiring explicit scope and
  approval, regardless of daemon mode.

## Report the preflight

For tasks that use the shell, briefly record the login shell and actual
executor. For Docker tasks, report whether the CLI and daemon are available,
the verified mode/context chosen, and any limitations. Redact endpoints,
private paths, and unrelated system details. If no Docker work is needed, do
not run Docker operations merely to demonstrate the check.
