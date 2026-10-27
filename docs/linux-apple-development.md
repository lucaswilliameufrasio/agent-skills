# Apple development from Linux with a Mac controller

## Decision

Add a portable `linux-apple-development` skill, not a fork of the upstream
`omarchy-apple-dev` toolchain. The upstream already contains distribution notes,
Ubuntu run records, user-only installation, pinned xtool fixes, SDK/resource
helpers and device/shipping tooling. A second implementation would duplicate
fast-moving SDK and authentication fixes without establishing new compatibility.

This skill coordinates discovery, host roles, distro/toolchain compatibility,
safe installation, build verification and separate runtime/release gates. The
upstream remains the owner of executable tooling; project-specific build commands
remain with the application. No upstream scripts are copied into this collection.

A separate tools repository is justified later only if there is an approved,
maintained requirement for executable distro adapters, reproducible builder
images or a remote Mac job service that upstream cannot accommodate. Prefer
upstream contributions before a fork. Merely needing CachyOS, Debian and Ubuntu
does not establish that requirement, and this change creates no remote repository
or Mac service.

## Three meanings of “using the Mac”

1. **Mac as terminal/controller:** SSH to Linux and run compatible jobs there.
   Ordinary server administration requires no Apple development toolchain.
2. **Linux builds Apple apps:** the upstream may build supported Swift-family or
   Flutter artifacts with a compatible SDK; those artifacts still need Apple
   runtime verification. It does not make Linux execute AppKit/SwiftUI applications.
3. **Mac native stage:** where cross-build compatibility is missing, a scoped Mac
   build or test/signing stage is available if the user approves it. This does
   not require publicly exposing the Mac or keeping it occupied by every job.

For a Rust/egui/Cargo app, `ship-mac.sh` is not a universal replacement for Cargo
bundling. Review Rust targets, linkers, native dependencies and the repository's
macOS packaging workflow. The Mac can remain the runtime verifier or bounded
fallback builder; do not promise a Linux-only Apple pipeline without that proof.

## Support evidence, not blanket promises

At reviewed upstream revision `2fb2486d7b1687a5ca8139df51da5ad932277cad`:

- Arch/Omarchy is the main target; CachyOS is an adaptation candidate, not a
  separately established Apple toolchain run in this delivery.
- Ubuntu 24.04 has upstream x86_64 and aarch64 run records with different, limited
  evidence. Those records are not equivalent to universal iOS/macOS runtime tests.
- Debian has no specific run record in the reviewed upstream distro guide. A
  compatible supported builder may be useful, but an Ubuntu container on Debian
  is not proof of native Debian compatibility.
- SDK-free mode is experimental and explicitly not the macOS-app route. Full
  SwiftUI/macOS needs a compatible full SDK path or a native Mac build.

Sources: [upstream repository](https://github.com/joshuaswarren/omarchy-apple-dev),
[distribution guide](https://github.com/joshuaswarren/omarchy-apple-dev/blob/2fb2486d7b1687a5ca8139df51da5ad932277cad/docs/DISTROS.md),
and the reviewed source links in the skill's references. Recheck current evidence
when executing; this documentation is not certification for future releases.

## Use

From this checkout, after reviewing the skill:

```sh
npx skills add . --skill linux-apple-development --global
```

Example request:

> Use linux-apple-development to plan this app's Apple build workflow. My Mac
> controls Linux hosts by SSH. Identify the app language and actual host versions,
> keep credentials on the designated signer, and separate Linux build evidence
> from Mac/device runtime tests. Do not install, enable inbound Mac access, export
> keys, notarize or upload without the corresponding approval.

Installing the skill does not install Swift, an SDK, xtool, Xcode or an SSH/MCP
service. Neither installing nor invoking it grants signing/publication permission.

## Verification scope

The initial evaluation uses two paired decision scenarios: native Debian versus
Ubuntu evidence and installer mutation; Rust versus SwiftPM with a Mac controller,
Apple runtime and signing/publication boundaries. These are procedural checks,
not actual host installs or Apple builds. The skill files, reference paths and
evaluation schemas receive structural validation. Exact results and limits are
maintained in the skill's `evals/README.md`; raw responses remain outside this
public checkout.

No Apple SDK, account, private key, device pairing, Mac, Debian or Ubuntu server
was accessed or configured while authoring this skill. No local Apple build,
device install, signing, notarization or publication is claimed.
