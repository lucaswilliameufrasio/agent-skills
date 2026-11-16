---
name: remote-host-hardening
description: >-
  Harden SSH and remote access on Linux or macOS without locking the owner out,
  and optionally build a private host status page. Use to secure SSH, restrict
  logins, or monitor a server's health and access.
---

# Remote host hardening

The goal is that only the intended people and keys reach the host, over the
intended paths, with every access visible, and that the owner can still get in
when something breaks. Hardening that locks the owner out is an outage.

## Inspect first (read-only)

Confirm the target host, how you are connected, and authorization to change
it. Then record without changing anything:

- operating system and version, init/service manager, firewall in use, and
  package manager;
- remote access paths: SSH server and effective configuration, VPN or private
  network (mesh VPN, bastion), remote desktop/screen sharing, management agents,
  exposed ports from the host's own view and, when possible, from outside;
- accounts that can log in, authorized keys per account (fingerprints, not
  key bodies), sudo/admin membership, password login status;
- logging of authentication events and where it is kept;
- other services on the host and who owns them. Shared hosts run things you
  must not disturb.

## Keep a way back in

Before changing any access control:

- keep the current session open and open a second one; test every change from
  a **new** session before closing the old ones;
- validate configuration syntax with the service's own test mode before
  reloading; reload rather than restart where supported;
- identify an out-of-band path (console, physical access, provider rescue
  mode, a second admin path) and confirm it works, or tell the user it does not
  exist before proceeding;
- back up each configuration file before editing; one control per change.

## Controls to consider

Choose from these based on the inspection, explain each in the user's terms,
and ask before applying ones that change how people reach the host:

- **Network exposure.** Prefer reaching management ports over a private network
  (VPN, mesh network, bastion) and close them to the public internet. Bind
  services to the interfaces they need. Default-deny inbound firewall with
  explicit allows.
- **Authentication.** Key-based login only; disable password and keyboard-
  interactive authentication once keys are confirmed working; prefer modern key
  types and hardware-backed keys where available; no direct root/administrator
  login; restrict which accounts may log in. Remove unknown or stale keys only
  after the owner confirms them.
- **Server configuration.** Current supported version of the SSH server from the
  OS vendor; modern algorithms per the vendor's or the server project's current
  guidance; limits on authentication attempts and idle sessions; disable
  forwarding features that are not used.
- **Brute-force noise.** Rate limiting or ban tools when the port must stay
  public; unnecessary when it is reachable only over a private network.
- **Privilege.** Admin rights only for accounts that need them; sudo with
  logging.
- **Remote management.** Disable remote desktop, screen sharing, or management
  agents not in use; restrict those in use to the private network and named
  users.
- **Updates.** Automatic security updates where the OS supports them, or a
  documented update routine.
- **Audit.** Authentication logs retained long enough to be useful, and a way
  to review successful and failed logins by account, key, and source.

macOS and Linux differ in where these settings live and which are managed by
the OS (for example, macOS system settings may override some SSH server
options). Verify each control against the current OS documentation and the
effective running configuration, not just the file.

## Verify

From a new session and, where possible, from outside the private network:
confirm allowed paths work, denied paths fail (password login rejected, root
login rejected, public port closed), the effective server configuration matches
intent, and authentication events appear in the logs. Record what was tested
and from where.

## Status page (optional)

When the user wants to watch the host, build a small read-only page or
dashboard showing what the owner checks most:

- health: uptime, CPU, memory, load, disk usage per volume with trend, and
  temperature or battery where relevant;
- services: running/failed state of the services the owner cares about;
- access: recent successful logins (account, key fingerprint or method,
  source, time), failed attempt counts, and active sessions;
- updates pending and last update time.

Rules for the page: it is reachable only over the private network or behind
authentication; it never exposes key bodies, secrets, or full log lines with
sensitive content; collectors run with least privilege and read-only access;
data is retained for a bounded time. Prefer an existing monitoring stack the
user already runs over a new one. For the interface, follow the user's design
system or `reference-driven-design`; status, severity, and trend should read at
a glance.

## Report

Inspection findings, each control applied (before/after, file, verification),
controls proposed but not applied and why, the out-of-band path, how to roll
back each change, and the status page location and access rules if built.
Redact hostnames, addresses, and key material when the report leaves the
owner's machine.
