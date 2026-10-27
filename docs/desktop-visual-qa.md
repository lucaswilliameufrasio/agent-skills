# Remote native desktop QA

## Decision and scope

Use one portable `desktop-visual-qa` skill with Linux/SSH, framework and evidence
references. egui, Slint and GPUI share the same observe/act/verify loop; their
rendering and introspection differences belong in references rather than three
competing QA policies. A project's launch commands, fixtures and stable targets
belong in its own verifier, not in this public skill.

The skill supports improving native UI/UX while the developer connects over SSH.
It does not provide a display, install an MCP, grant desktop access, modify other
repositories, or automatically make a harness capable of inspecting image data.
No framework migration is necessary merely to create a feedback loop.

## Use

Install from a checkout containing this skill, after reviewing it:

```sh
npx skills add . --skill desktop-visual-qa --global
```

After publication, the README's repository installation command can be used.
Installation through the Skills CLI may fetch/execute tooling and is a separate
user action; no global installation is performed as part of authoring the skill.

Example request:

> Use desktop-visual-qa to inspect this Rust desktop app over SSH. First identify
> the renderer and available capture/input tools. Use a private test profile,
> capture and inspect before/after images, and verify keyboard navigation,
> resizing and the result grid. Ask before installing infrastructure or accessing
> my real graphical session. Do not use saved production connections.

For the first egui application, prefer a real-window private-desktop smoke path
plus version-matched `egui_kittest` component tests when appropriate. Do not treat
wgpu snapshots as acceptance of a glow application renderer. GPUI requires a
proven compatible graphics path; Slint embedded MCP needs version and exposure
checks before use.

## Supporting tools

- `agent-workspace-linux`: preferred candidate for a private Linux display and
  MCP input/capture, after local readiness and ownership checks. Its upstream
  bundled skill owns tool syntax. A private display is **not** a security sandbox.
- `computer-use-linux`: candidate for an explicitly approved real Linux session;
  screenshot consent and accurate targeting must be verified separately.
- Xpra: optional human viewing, not an automation or assertion replacement.
- Framework tests: deterministic component/state checks, not blanket acceptance
  of the actual native application or OS integration.

Upstream links and freshness limits are in the skill's references. Distro package
names, MCP registration formats and graphic backends must be checked at use time;
this collection does not pin third-party installation scripts as universal setup.

## Evaluation boundary

Three synthetic decision scenarios cover absent image inspection, GPUI graphics
failure/shared-session scope, and old Slint/public-MCP/native-dialog assumptions.
Each has three observable criteria under
`skills/desktop-visual-qa/evals/`. Paired responses with and without the skill
measure procedural behavior, not screenshot quality, usability, automatic skill
activation or real app rendering. No fixture pretends to provide a graphical
session or a real database. Raw responses and the review viewer stay outside the
public repository.

Initial response-only checks passed 9/9 criteria with the skill versus 5/9
without it. See the [evaluation notes](../skills/desktop-visual-qa/evals/README.md)
for grading details and limits. Skill frontmatter across the collection, the new
reference links, case/grader schemas and `git diff --check` were validated. The
initial authoring pass did not run a desktop application.

## Follow-up real runtime smoke check

An authorized SSH run subsequently built a real egui/eframe application with its
glow renderer, launched it in an exclusive Xvfb/Openbox workspace and inspected
ten actual window screenshots. It exercised the empty state, connection form,
required-field and URL validation, Tab navigation, ASCII entry, Unicode paste,
minimum-size scrolling, restored dimensions and cancellation. All data was
synthetic; app storage, runtime, session bus and clipboard were private. No
personal connection profiles or keyring were opened. The renderer query reported
Mesa llvmpipe, OpenGL 4.6: this is software-rendered Linux evidence, not target-GPU
or macOS acceptance.

This run found real UI issues (missing icon glyphs and inconsistent validation
status coloring) and automation issues (KWin capture format incompatibility,
runtime socket path length, full host temporary storage, NVIDIA EGL selection
and accented synthetic typing). The portable infrastructure lessons are recorded
in the skill's Linux reference. Downloads/dependencies were user-approved,
checksum-verified and confined to a private directory; no system installation,
global MCP registration or real-desktop control was performed.

The query result grid, connected GUI workflow, native dialogs, production GPU,
150% DPI and other frameworks remain outside this visual smoke check. A successful
component or database integration suite does not fill those visual coverage gaps.
Private run artifacts and exact local commands stay outside this public checkout.

The same target's debug build, formatting, warning-free Clippy and 27 ordinary
tests passed. Its three database integration tests also passed in three
consecutive executions against a script-owned disposable PostgreSQL 18 container
through a verified rootless Docker daemon. The owned GUI workspace was stopped
and evidence retained. Release/packaging and cross-platform CI were not run.
