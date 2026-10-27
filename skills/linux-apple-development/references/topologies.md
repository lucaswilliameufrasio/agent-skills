# Host roles and upstream scope

## Three different jobs

| Job | Useful route | Boundary |
| --- | --- | --- |
| Use a Mac to administer Linux servers | SSH and existing administration tools | No Apple SDK or xtool needed |
| Build a compatible Apple app on Linux, using the Mac as controller | SSH into Linux plus approved upstream Apple build tooling | The artifact still runs on Apple hardware, not Linux |
| Use Linux development with native Apple build/test/signing stages | Scoped SSH/artifact transfer to an approved Mac | Mac availability, Xcode, signing, GUI consent and concurrency must be managed |

The upstream name includes Omarchy, but a desktop theme/window manager is not a
general prerequisite for its command-line toolchain. Do not install Omarchy or
replace KDE/GNOME to obtain Swift tooling on a server.

## What omarchy-apple-dev actually supplies

The inspected upstream describes patched xtool, Linux Swift/Darwin SDK setup,
resource compiler stand-ins, SwiftPM/Xcode project adapters, experimental
SDK-free build paths, Flutter iOS build helpers, device tooling and shipping
helpers. Prefer its pinned source/fix set over assembling unrelated latest
versions. Some tests cover installation or linking, others an actual device;
the evidence level matters.

Specific limits to carry into plans:

- `ship-mac.sh` inspects a SwiftPM package and currently constructs an arm64
  macOS target. It is not a universal Cargo bundler or proof of Intel/universal
  macOS builds. Inspect the chosen revision before naming supported targets.
- Its Xcode project adapter cannot prove every build phase, plugin, framework,
  entitlement or resource was translated faithfully. Test the actual project.
- The full route and SDK-free route have different feature sets. Upstream's
  README explicitly excludes macOS apps from the experimental no-Xcode route.
- Flutter evidence is qualified by host CPU, plugin implementation, mode and
  date; release device builds do not establish debug/hot reload or simulator use.
- Native Apple UI/runtimes are not emulated merely by having a Darwin SDK on Linux.

## Use the one Mac deliberately

Discover whether the user's Mac is Apple Silicon or Intel, its macOS/Xcode
versions, and whether the user even wants remote inbound access. Do not enable
Remote Login, install agents or alter power settings without approval.

If the agent runs on Linux and needs a Mac stage, use a named approved SSH alias
with normal host-key verification and least-privilege identity. Bound commands
and transfer only source/artifacts required for the job. Do not use `rsync
--delete` against a user workspace or copy whole home/config/keychain directories.
Use unique persistent workspaces and serialize shared GUI/signing resources.

If the agent already runs on the Mac controlling Linux, keep that direction;
there is no need to turn the Mac into a public service. The user can run an
approved local verification stage without exposing inbound SSH to the internet.
Private networking may help reach hosts, but is a separate infrastructure change.

## Sources and dated evidence

Reviewed on 2026-10-27 at upstream revision
`2fb2486d7b1687a5ca8139df51da5ad932277cad`:

- https://github.com/joshuaswarren/omarchy-apple-dev
- https://github.com/joshuaswarren/omarchy-apple-dev/blob/2fb2486d7b1687a5ca8139df51da5ad932277cad/docs/DISTROS.md
- https://github.com/joshuaswarren/omarchy-apple-dev/blob/2fb2486d7b1687a5ca8139df51da5ad932277cad/install-toolchain.sh
- https://github.com/joshuaswarren/omarchy-apple-dev/blob/2fb2486d7b1687a5ca8139df51da5ad932277cad/ship-mac.sh
- https://github.com/joshuaswarren/omarchy-apple-dev/blob/2fb2486d7b1687a5ca8139df51da5ad932277cad/docs/TEST-MATRIX.md
- https://www.swift.org/install/ — choose actual supported host and release.

These are upstream claims, not local Apple build or distribution certification.
Recheck compatibility, upstream fixes and current receipts when executing.
