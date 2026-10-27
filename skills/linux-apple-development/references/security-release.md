# Credentials, devices and release boundaries

## Keep credentials out of the build fleet

Apple ID credentials, App Store Connect `.p8` files, Developer ID private keys,
provisioning data with private identifiers, device pairing records and auth
caches require scoped custody. Use reference paths or approved secret injection;
never print resolved secrets, commit them, copy a keychain or forward an SSH
agent globally. Prefer a designated signer instead of copying a signing key to
each server. Confirm the selected account/team and device before mutations.

Apple login/2FA, device Trust and GUI authorization may require the human. Do not
ask them to paste passwords or codes into chat or automate consent around them.
If the needed identity/account is absent, prove an unsigned build and state the
signing/deployment blocker; do not create account resources without approval.

## Device transport is not SSH transport

An iPhone plugged into the Mac is not attached to a Linux server. Use an approved
Mac stage or a separately approved device-access topology. Do not assume USB/IP
forwarding is safe or available. Do not invent an iPhone because the user owns a
Mac, and do not replace device tests with Linux screenshots.

The inspected upstream tailnet route has specific iOS/Python/TLS-PSK versions,
initial USB pairing, Wi-Fi/device-state constraints and a privileged TUN setup.
Its dated iOS 27 measurements are not a general promise for older/newer versions,
plain LAN or cellular-only connectivity. Read the actual chosen version's guide:
https://github.com/joshuaswarren/omarchy-apple-dev/blob/2fb2486d7b1687a5ca8139df51da5ad932277cad/docs/OVER-TAILNET.md

Pairing records contain private device-control keys. Copy only the named record
to named trusted hosts with explicit approval and restrictive permissions; never
bulk-sync all records. Tailnet membership does not replace pairing or grant all
hosts device access. Ask before scanning addresses/ports, creating tunnels or
using elevated TUN/device permissions. Close only tunnels started for this run.

Screenshots and device logs may include notifications, lock-screen details,
messages or other apps. Use an approved test window, verify the intended app and
keep evidence private. Respect retention instructions; do not publish captures
or delete the user's records as automatic cleanup.

## Independent release gates

1. **Compiled:** verify format, CPU, target SDK and bundle contents. Not runtime.
2. **Signed:** verify the actual identity/team, nested signatures, entitlements
   and provisioning for the target. An ad-hoc/TEST signature is not a distributable
   Developer ID or App Store identity.
3. **Ran:** prove launch and one user journey on the actual target. Test the exact
   transferred build, not a separately rebuilt app with the same name.
4. **Notarized/installed:** when requested, verify Apple's processing result and
   stapling/Gatekeeper behavior or physical-device installation independently.
5. **Uploaded/published:** TestFlight/App Store upload, processing, distribution
   to testers and review submission/approval are distinct external side effects.

Inspect all invoked shipping helpers for default network/account operations.
Installing a toolchain or asking for a build does not approve any later gate.
Do not create certificates/profiles, enable Remote Login, export signing keys,
notarize or upload merely because an upstream script offers a convenient flag.

The upstream macOS script may emit warnings and omit unsupported nibs or
entitlements. A zero exit can therefore conceal lost behavior. Inspect warnings,
resource completeness and the resulting native experience; do not weaken the
project's security entitlements to make launch/signing pass.
