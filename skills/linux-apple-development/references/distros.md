# Distribution and toolchain preflight

## Support map at the reviewed revision

| Host | Upstream evidence | What not to infer |
| --- | --- | --- |
| Arch/Omarchy | Main target; dated installs and device runs on specified toolchains | Every rolling-release state or CachyOS configuration is verified |
| CachyOS | Arch-compatible package route is a candidate | A local desktop QA pass validates this Apple toolchain |
| Ubuntu 24.04 x86_64 | Container records for setup and selected SDK-free linking steps | Complete macOS/iOS runtime, all overlays/plugins or every Ubuntu release |
| Ubuntu 24.04 aarch64 | Documented hardware run and unsigned Flutter IPA | Identical runtime, signing or debugger coverage on every arm64 host |
| Debian | No Debian-specific run record in the reviewed distro page | Ubuntu package list/tarball is automatically ABI-compatible with Debian |

List the user's exact Debian/Ubuntu version. For unsupported host/toolchain
combinations, prefer a supported isolated builder or an approved Mac build over
host library hacks. A supported Ubuntu builder container on Debian is **Ubuntu
builder coverage**, not native Debian validation. Review the Apple SDK terms for
the intended environment; never present containers as a licensing workaround.

## Read-only inventory

Use `/etc/os-release`, CPU architecture and package metadata on the selected
host. Discover commands before invoking them: `swift --version`, matching clang,
LLDB, `swift sdk list`, Python and pkg-config. Protect credentials: do not run
authentication commands or inspect auth stores as a diagnostic shortcut.

Check actual compiler paths behind mise/asdf shims. Swift's clang must match the
toolchain; a system clang of a different generation can break SDK modules. A
Swift archive needs its expected `usr/` hierarchy for SwiftPM discovery. Verify
dynamic dependencies, including the LLDB Python library, instead of assuming
`swift --version` proves debugger readiness.

Check persistent and scratch disk/inodes before multi-GB SDK/toolchain/IPSW or
Flutter downloads. `TMPDIR` may not move every tool's cache or hardcoded scratch
path. Do not delete shared caches to make room or put a source checkout in RAM.

## CachyOS / Arch candidates

Inspect the upstream pacman/AUR branch before approving it. It may call sudo and
an AUR helper with noninteractive confirmation. Package install approval must
cover these operations explicitly; inspect package build instructions and avoid
rolling-release partial upgrades. Prefer the already-managed compatible Swift
toolchain when available, without replacing its global version silently.

Upstream packages include build tools, libimobiledevice/OpenSSL headers and
resource conversion tools. The needed set depends on the selected mode/app.
Do not require USB tooling for a compile-only remote job unless the build itself
needs those libraries. Do not install an entire desktop environment.

## Ubuntu candidates

Use the current upstream `docs/DISTROS.md` and official Swift release platform
requirements. Resolve packages for the exact Ubuntu release; do not blindly
copy versioned GCC/Python package names from another release.

The recorded Ubuntu 24.04 path needed newer libimobiledevice APIs than its
distribution package supplied. Verify API/pkg-config compatibility rather than
assuming an installed package is sufficient. If a source prefix is required,
approve and pin each component; keep its includes/libs/pkg-config settings local
to the build. Do not overwrite `/usr` or edit global `ld.so` configuration merely
because an upstream example did so.

## Debian candidates

First seek a toolchain distribution supported for that exact host/architecture.
Compare glibc, libstdc++, libicu, ncurses, libxml2, OpenSSL and LLDB/Python library
requirements using official metadata and actual loader checks. Resolve Debian
package names from its own repositories, not Ubuntu repositories.

If no supported native route is established, propose an approved rootless builder
using an appropriate supported Ubuntu base, or a scoped Mac build. Do not install
Ubuntu packages into Debian or fake missing ABI versions with global symlinks.
Containers need their own preflight: host architecture, disk, daemon mode, pinned
image, project mounts and resource limits. Do not mount the user's Apple keys,
pairing records, SSH agent, host Docker socket or USB bus just to build an artifact.

Device testing over USB/network is a separate stage; a successful container
compile does not prove USB passthrough, trust, provisioning, runtime or debugger.

## Installer and repair safety

At the reviewed revision, non-pacman hosts skip Arch package steps rather than
automatically supplying a complete apt adapter. `--user-only` likewise expects
dependencies to exist. Both still perform user-level installation and SDK edits.
Select `--mode full` or `--mode no-xcode` explicitly instead of allowing a headless
run to pick a default. Review `--repair` before using it: SDK registration and
Python environments are state, not disposable diagnostics.
