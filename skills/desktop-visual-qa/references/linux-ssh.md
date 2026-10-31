# Linux rendering and remote control

## Choose a route

0. Run `scripts/probe.sh` (read-only) to see what this machine already has.
1. Reuse a repository-owned native harness if it proves the needed behavior.
1a. On KDE machines, try the zero-install private KWin route below before
   asking to install anything.
2. For real-window QA over SSH, prefer an approved private desktop managed by
   `agent-workspace-linux` when installed and compatible.
3. Use `computer-use-linux` on an existing desktop only with explicit approval
   of that session/window scope. It may affect the user's focus and input.
4. Use a manually managed Xvfb/compositor only when tools and ownership checks
   are understood. Allocate a free display; do not hardcode or take over `:0`.

Xvfb supplies an X server, not a guaranteed OpenGL/Vulkan implementation. Mesa
software rendering may work for some apps; prove actual rendering. Virtual native
Wayland compositors may be alternatives depending on installed versions, render
nodes and permissions. Do not install a full desktop or grant GPU/input-device
access automatically. GPUI failure under Xvfb does not mean the UI is defective.

## Zero-install route: private KWin on Plasma

Plasma machines usually already ship `kwin_wayland` (`--virtual`), `spectacle`,
`dbus-run-session`, `kscreen-doctor`, `wl-copy` and `ksecretd`. `scripts/probe.sh`
lists what exists. `scripts/qa_session.py` uses them to run an app in a private
Wayland compositor and drive it, with no package installs and no contact with the
user's session (private runtime dir, private D-Bus, private HOME/XDG by default).
Input uses libei through KWin's EIS D-Bus endpoint, via `scripts/eitool.c`, which
`qa_session.py` compiles per run with `cc` (needs libei headers, e.g. `pkg-config
--exists libei-1.0`).

```sh
scripts/qa_session.py --out RUN_DIR --size 1920x1200 [--output-scale 1.5] [--keyring] \
  --steps steps.txt -- /path/to/NEW/binary
```

Step files are plain text (`click X Y`, `type`, `paste`, `key ctrl+a`, `shot NAME`,
`wait`, `sh`, ...; see the script header). Coordinates are compositor logical
pixels. Observe, act, then re-observe; do not reuse guessed coordinates.

Smoke-tested on 2026-10-30 on KWin 6.8.1 (Arch/CachyOS, NVIDIA + AMD) with four
Rust egui/glow apps and a Qt app:

- **Real GPU, not software.** An EGL probe inside the session reported the NVIDIA
  driver, and `nvidia-smi pmon` listed the app as a graphics client. Do not assume
  llvmpipe; probe the adapter in each environment. It still is one machine's GPU.
- **Click, type, Tab, ctrl+a, Enter, scroll and clipboard paste work.** ASCII typing
  is US-layout; use `paste` (private `wl-copy`) for accents. Pasted `São João ção`
  arrived intact in an egui field, a SQL editor and a Valkey console.
- **Real fractional DPI** needs `--output-scale N` (KDE output management through
  `kscreen-doctor`) applied **before** the app starts. KWin's own `--scale` only
  enlarges the framebuffer and is *not* a DPI test. Size the physical framebuffer as
  logical size x scale, or a 1.5x window overflows the screen.
- **Native dialogs are reachable.** A GTK file chooser (from `rfd`) and the KDE Wallet
  wizard appeared inside the private compositor and could be driven and captured.
- **Private keyring.** Without a Secret Service, apps using the `keyring` crate fail
  with a readable error. `--keyring` starts a private `ksecretd`; its first use opens
  a wallet wizard that must be completed (classic/Blowfish, throwaway password) by a
  `sh secret-tool store ...` step plus clicks *before* the app saves a password. The
  wallet lives in the private HOME; never point this at the real one.

Pitfalls that cost time:

- **Pick a framebuffer larger than the app's initial window plus decorations.** An app
  that opens 1360x860 does not fit a 1360x860 screen; its status bar was off-screen and
  looked like a missing feature.
- **KWin drops the EIS client when the D-Bus connection that requested it closes.** Keep
  that connection alive for the whole run (the script does).
- **egui repaints on events.** A frame captured after an async result may be stale until
  the pointer moves; add a `move` step before the capture and say so in the report.
- **Check ports before starting disposable services.** One default port was already in
  use by another local service; bind disposable containers on free loopback ports with
  unique names and remove only those.
- **Apps may not follow system theme.** Several force dark mode, so "light theme" was
  not testable; report that as not supported rather than as a gap in tooling.
- Not covered: macOS, other compositors, an on-screen IME, multi-monitor, and apps that
  need a portal (no `xdg-desktop-portal` runs in the private session).

For a Qt/KDE-less machine use the other routes below.

## agent-workspace-linux

Upstream documents a private X11 or native Wayland workspace, stdio MCP and a
bundled tool-driving skill. Prefer that skill for tool details rather than copying
its changing tool catalog. Read installed `--help` and run `doctor` first. The
documented CLI flow is below; verify against the installed version and perform
mutating steps only within approved scope:

```sh
agent-workspace-linux doctor
agent-workspace-linux workspace start --dry-run
agent-workspace-linux workspace start --ack-hidden-workspace --purpose "Desktop visual QA"
```

After identifying the run's workspace, use its launch/observe tools to start the
exact app binary and retrieve screenshots. Resolve the actual workspace selector,
working directory and output path from current help; do not launch into or stop
an existing workspace implicitly. Only stop the owned workspace at teardown.

**Not a sandbox:** apps run as the user and may access home, files, network,
SSH agents, keyrings and host settings. A separate display protects input focus,
not secrets. Use supported isolated app storage and synthetic data. Running
untrusted programs requires a separate, approved execution boundary.

## computer-use-linux

Use the installed doctor and window-discovery tools to identify the intended
session. Verify screenshot capture separately. AT-SPI is useful only where the
application exposes it; a container-only accessibility tree is not a widget map.
Setup commands can change desktop settings/extensions and input services, so
do not treat them as read-only diagnostics. Portals may require a human present;
never click through authorization prompts on the user's behalf.

An SSH process may lack the intended runtime directory, Wayland/X11 socket or
session D-Bus. Obtain these from a verified same-user session through an approved
launch mechanism. Do not scrape another process's complete environment, guess
`:0`, or copy authentication files. If no usable session exists, choose a private
one with approval rather than fabricating display environment variables.

## MCP transport is separate from display transport

If the harness already runs on the Linux host, launch the MCP binary there
directly. If the harness runs elsewhere, stdio MCP can be carried by SSH. This
is a **generic client example**, not universal harness configuration:

```json
{
  "mcpServers": {
    "desktop-qa": {
      "command": "ssh",
      "args": ["-T", "YOUR_HOST_ALIAS", "/ABSOLUTE/PATH/agent-workspace-linux", "mcp"]
    }
  }
}
```

Resolve placeholders on the actual host. Preserve existing MCP settings; use the
client's documented configuration format and scope. SSH must have verified host
keys and noninteractive authentication available; do not disable host-key checks.
Stdout must contain only MCP protocol output; do not source noisy login scripts.
Keep logs on stderr. Images must reach the agent as image content or through an
approved file-transfer/viewing path; a remote path alone is not inspectable.

Xpra is optional human viewing/control, not an MCP or visual-test assertion.
Connecting it to a different display will not show the MCP workspace. Establish
same-display ownership explicitly, secure transport, and authorization before
attaching. Do not expose unauthenticated MCP/VNC/X11 services publicly.

## Sources and freshness

Checked against upstream documentation on 2026-10-27 (not a local runtime pass):

- https://github.com/agent-sh/agent-workspace-linux — backends, CLI and trust model.
- https://github.com/agent-sh/agent-workspace-linux/tree/main/skills/agent-workspace-linux
- https://github.com/agent-sh/computer-use-linux — readiness, session and input limits.
- https://xpra.org/ — optional remote viewing; consult current connection docs.

Treat support tables as upstream claims until tested on the actual distro/session.
Package names, backend requirements and MCP schemas can change. Verify installed
versions and current upstream docs before proposing installation commands; request
approval for package installs, downloaded scripts and persistent configuration.

## Runtime lessons from a real SSH smoke check

These are observed failure modes, not universal setup requirements:

- **Choose backend-specific readiness.** In v0.6.0, `doctor` can report KWin ready
  while the generic `blockers` and recommendation still list missing X11 tools.
  Read the chosen backend's fields. Even a ready backend and successful dry run
  still need a real capture probe.
- **KWin capture compatibility.** A v0.6.0 capture probe against KWin 6.8.1 failed
  with `unsupported KWin screenshot layout ... format 16`. Do not diagnose this
  as an application failure or waive the capture check. Preserve versions/error;
  use a proven compatible release or an approved private X11 alternative.
- **Short runtime socket paths.** The tool uses Unix sockets with a 107-byte path
  limit. Deep artifact directories may be fine for PNGs but too long for
  `XDG_RUNTIME_DIR`. Use a short, private, same-user runtime directory and a short
  unique workspace ID. Do not reuse a shared runtime to avoid the limit.
- **Full `/tmp`.** Setting `TMPDIR` is not enough for an X server that writes
  `/tmp/.X*-lock` and `/tmp/.X11-unix`. Do not delete unrelated files or disable
  locking. An approved per-process mount namespace can bind a private disk-backed
  scratch directory over `/tmp` without changing the host. Use a consistent mount
  for the server, controller and app; verify device/proc setup and `/dev/null`
  access. A bind of `/` alone need not provide usable device nodes in a user
  namespace. This convenience mount is not a sandbox or permission grant.
- **Software graphics must select the right vendor.** On one mixed Mesa/NVIDIA
  setup, Xvfb crashed during NVIDIA EGL initialization even though software
  rendering was intended. Per-process Mesa EGL/GLX vendor selection and llvmpipe
  resolved that run. Verify the installed vendor JSON and driver before using
  `__EGL_VENDOR_LIBRARY_FILENAMES`, `__GLX_VENDOR_LIBRARY_NAME`,
  `LIBGL_ALWAYS_SOFTWARE` or `GALLIUM_DRIVER`. Do not edit global driver settings.
  Record the actual adapter with a context query; this does not test the target GPU.
- **Typing success is not fidelity.** X11 synthetic typing reported success but
  dropped accented characters. Pasting through the private workspace clipboard
  preserved them in the inspected frame. Prefer that route for complex nonsecret
  text when supported, and still verify the result. Never use the host clipboard
  or submit a query based solely on an input tool's success result.

Local-only dependency extraction is an option after approval, not an automatic
fallback: use official package metadata, verify checksums/signatures according
to the repository's policy, resolve dynamic libraries and scope `PATH`/library
settings to the test processes. Do not execute package installation hooks or
silently convert an isolated extraction into a system installation.
