# Linux rendering and remote control

## Choose a route

1. Reuse a repository-owned native harness if it proves the needed behavior.
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
