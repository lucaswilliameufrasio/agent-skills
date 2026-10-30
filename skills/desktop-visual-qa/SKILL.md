---
name: desktop-visual-qa
description: >-
  Run evidence-based visual and interaction QA for native desktop applications,
  especially Rust egui/eframe, GPUI and Slint apps accessed over SSH or on headless
  Linux. Use when improving desktop UI/UX, testing resizing, keyboard navigation,
  themes or DPI, capturing real before/after screenshots, or setting up a remote
  GUI feedback loop. Distinguish component snapshots from the running application;
  compilation alone is not visual verification. Do not install tools or take over
  a user's graphical session without approval.
---

# Desktop visual QA

Close the loop: inspect → build → launch → observe → interact → improve → repeat.
SSH transports commands; it does not provide a graphical session, GPU, image
viewer, or permission to control the real desktop. A skill supplies the workflow,
not those capabilities.

## 1. Establish the target and acceptance

Read target repository instructions, manifests/lockfile, launch code, tests and
existing automation. Identify the exact checkout, binary, framework version,
renderer, enabled features, fixtures and supported platforms. Do not migrate UI
frameworks just to get screenshots or assume a dependency from a pasted example.

Choose one meaningful user journey and observable improvements before editing:
for example, open a connection form, correct an invalid field, connect to a test
database, run a safe query and inspect a wide result grid. Map each finding to
an acceptance check, not merely “looks modern.” Use the existing design language;
ask about consequential product choices rather than inventing new workflows.

For a database client, use synthetic local data and isolated application storage.
Do not unlock a real vault, reuse saved production connections, open a personal
keyring, or run arbitrary SQL to populate screenshots. Fixtures may cover UI
states, but a mocked connection does not prove the database integration.

## 2. Discover available capabilities

Read [Linux and SSH setup](references/linux-ssh.md) before choosing infrastructure.
Inspect capabilities without installing or changing configuration:

- Where do the agent, tools, source, build and GUI actually run?
- Is there a private virtual display, or only an existing desktop session?
- Are screenshot **capture and image inspection by this agent** both available?
  A PNG on a remote filesystem is not a viewed screenshot.
- Can input target the verified app/window? Are accessibility nodes exposed?
- What renderer/driver and display geometry can this environment support?

Run `scripts/probe.sh` first: it is read-only and lists the routes this machine
already supports (for example a private KWin session on Plasma, which needs no
installation and, with `scripts/qa_session.py`, supports click, type, paste, real
fractional DPI, a private keyring and native dialogs). Prefer a ready route over
proposing installs; probe the actual renderer instead of assuming software rendering.
Use installed tools and their current schemas/help; do not invent MCP tool names.
Run available read-only readiness diagnostics, then prove capture with an actual
frame. A successful doctor report or portal detection is not capture consent.
Record capture, inspection, targeting, input and rendering readiness separately.

Prefer an approved private desktop over taking over the user's mouse/focus.
If setup requires packages, MCP registration, a hidden workspace acknowledgement,
portal consent, services or host permissions, explain the exact change and obtain
approval. Never bypass consent, use `xhost +`, weaken device/socket permissions,
or silently select another person's session. When blocked, continue safe source
review/component tests if useful, but label visual acceptance unverified.

## 3. Select complementary verification layers

| Layer | Evidence | Does not establish |
| --- | --- | --- |
| Logic/component tests | State transitions, labels, deterministic widget interactions | Native window behavior or visual quality |
| Rendered component snapshots | Layout of selected fixture states under a recorded renderer | Real app launch, OS integration, database connectivity |
| Real app in private desktop | Actual window, input and before/after states | Equivalence to all GPUs, compositors or operating systems |
| Approved target session | Integration with that session's GPU, DPI, dialogs and input | Cross-platform coverage |

Read only the relevant framework section of
[framework guidance](references/frameworks.md). Use native accessibility selectors
when actually exposed, otherwise refreshed window-relative pixels from inspected
screenshots. Browser DOM/Playwright selectors cannot control a native egui canvas.

## 4. Establish a reproducible baseline

Build using repository commands and launch the **newly built** binary into the
owned display. Record revision plus dirty state, build command, binary path,
framework/renderer, driver where known, fonts, locale, theme, window size and DPI.
Fix seeds/time and disable nondeterministic animations only in a documented test
mode. Record changes to the test environment rather than disguising differences.

Use a unique app data directory/profile if the app supports it; verify the real
storage path instead of assuming an environment variable isolates keyrings or
single-instance IPC. A private display alone does not isolate data or credentials.
Confirm PID/window ownership and a visible ready state; process survival is not
readiness. Bound launch/wait time and capture startup logs on failure.

Save and actually inspect a baseline screenshot. Reject blank, stale, wrong-window
or loading frames. Keep evidence in a run-specific directory outside public
artifacts when it may contain private data. Preserve full frames and useful crops;
do not upload screenshots or logs without authorization.

## 5. Drive and evaluate the user experience

Observe → perform one action → observe its result. Refresh window identity,
accessibility handles and geometry after layout changes. Record screenshot pixel
size, preview scale, window origin/decorations and logical/physical coordinate
mapping before pixel input. Never reuse guessed coordinates across DPI changes.
Read entered text back before executing a query; a tool's “input sent” is not
proof that quotes, Unicode or keyboard-layout-dependent symbols arrived intact.

Select relevant checks from [the UX and evidence checklist](references/ux-evidence.md).
Cover navigation, focus, validation and recovery as well as appearance. Capture
the action and resulting state. Supplement screenshot review with semantic/state
assertions; image similarity alone cannot prove the workflow works.

Prioritize a few evidenced problems, make a coherent change, rebuild/relaunch,
and repeat the same journey and conditions. Compare full before/after frames and
relevant crops. Do not replace a baseline or raise diff tolerance just to get a
green result; inspect the change, explain intentional differences, and follow the
repository's approval process for accepting new baselines.

## 6. Close with evidence and limits

Run the repository's applicable quality gate as well as selected visual checks.
Do not report “visually verified” unless an image was actually inspected and the
requested interactions exercised. Distinguish agent assessment from human design
sign-off; do not claim target-GPU acceptance from software-rendered snapshots.

Report concisely:

- Journey and acceptance checks: passed, failed or blocked, with observed results.
- Before/after artifact paths, what was inspected, and environment/renderer.
- Component, live-app and target-session checks run; explicit coverage gaps.
- Owned resources cleaned up, retained evidence, and the exact unblock action.

Stop only processes/displays/test services created for this run and verified by
their recorded identity. Do not `pkill` by app name, stop a shared workspace, or
delete neighboring artifacts. Preserve evidence after teardown.

For a repeatable project-specific launch/drive recipe, use an existing verifier
or author one with `create-verification-skill` if available. This skill remains
the portable desktop QA workflow; the app's commands and selectors belong there.
