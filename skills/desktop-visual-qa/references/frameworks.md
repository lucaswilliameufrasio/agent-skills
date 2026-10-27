# Framework-specific verification

## egui / eframe

Inspect Cargo.toml **and** Cargo.lock, resolved features, app construction and
renderer selection. Match `egui_kittest` to the project's egui/eframe version;
do not upgrade the app or copy a hardcoded latest dependency to add tests.
Check the version-specific API and feature flags before writing code.

`egui_kittest` can drive AccessKit-based widget interactions in-process. Its
`wgpu` and `snapshot` features provide rendered snapshots; `eframe` adds App
integration. Headless semantic tests and GPU-backed snapshot rendering have
different requirements: no visible window does not mean no graphics dependency.

Extract only the smallest useful view seam with deterministic inputs when needed.
Do not fork production layout into a test-only replica. Cover empty, loading,
success and error states with synthetic models; test real integration separately.
Use accessible widget labels and stable identities rather than ordering guesses.
OS-level AT-SPI exposure depends on enabled app/backend accessibility support;
in-process AccessKit testing does not automatically provide a system AT-SPI tree.

A wgpu snapshot can complement a glow production app, but does not verify glow,
native dialogs, fonts supplied by the OS, clipboard or window integration. Keep a
real-app smoke path with its actual renderer. Review new/diff images before
accepting baselines; bulk snapshot updates are not regression verification.

Source: https://docs.rs/egui_kittest/ (select the resolved version, not `/latest`).

## Slint

Inspect the exact Slint release and built features first. Recent upstream code
offers a developer-only `mcp` feature and `SLINT_MCP_PORT` for an embedded HTTP
MCP server. Verify availability, endpoint, debug-info compilation requirements,
bind address and headless/backend configuration in **that version's** source/docs
before generating a command. Do not assume every installed Slint supports it.

The upstream Cargo feature documentation describes `cargo ... --features
slint/mcp`, but renamed dependencies/workspaces need their actual feature path.
Keep developer introspection/control out of release builds. Treat the endpoint
as privileged and potentially unauthenticated: verify loopback binding, use an
approved SSH tunnel for remote access, and stop it after the run. Do not launch
it until exposure is understood; do not silently open a firewall port.

Headless rendering, software renderers and system testing are distinct options.
Verify `SLINT_BACKEND=headless` and the selected renderer are supported by the
resolved build rather than prescribing them unconditionally. Render actual pixels
and inspect the result; backend startup or element introspection alone is not
visual evidence. Embedded automation does not test native window-manager behavior;
retain a windowed check when the requested change depends on it.

Sources (checked 2026-10-27; main/master may differ from installed releases):
- https://github.com/slint-ui/slint/blob/master/api/rs/slint/Cargo.toml
- https://docs.slint.dev/ — use the installed release's backend and testing docs.

## GPUI

Read the project's pinned GPUI revision: it often comes from a Git dependency
and has evolving APIs and platform requirements. Reuse its existing test context
for logic/entity interactions, but do not equate those tests to rendered frames.

Check the actual Linux graphics backend, Vulkan/EGL requirements as applicable,
driver availability and render-device access. Xvfb by itself does not provide a
Vulkan-capable adapter. Software rendering is acceptable only after a successful
real frame with a recorded adapter; it is not proof of target-GPU behavior.

Prefer a compatible approved virtual compositor or approved real GPU/session
when the private X11 path cannot render. Do not fall back to the real desktop,
run as root, change device permissions, or install drivers without approval.
Capture renderer initialization errors; separate infrastructure blockage from
application defects and report which layer remains unverified.

Source: https://github.com/zed-industries/zed/blob/main/docs/src/development/linux.md
is a Zed integration reference, not a universal contract for every GPUI revision.

## Other native frameworks

Follow the same separation: framework semantic harness, rendered fixture, live
app, target-session integration. Discover official version-matched test hooks and
reuse existing automation; do not force browser tools onto native widgets or
invent accessibility support.
