# UX checks and evidence

Select checks relevant to the requested journey; record omitted scope explicitly.

## Appearance and layout

- Hierarchy, typography, spacing rhythm, density, alignment, icon clarity and
  readable contrast across normal, selected, hovered, disabled and error states.
- No clipped labels/buttons, overlapping panels, unintended blank areas or
  unreadable text at supported minimum, normal and large window sizes.
- Resize panel splitters, long labels, wide/large result grids, scrollbars and
  keyboard focus visibility. Cover DPI and light/dark themes where supported.
- Keep baseline and candidate geometry, fonts, renderer and fixture state equal.
  Differences between drivers are a diagnostic clue, not a reason to bless diffs.

## Interaction and recovery

- Keyboard-only navigation: Tab/Shift+Tab, Enter/Escape, shortcuts, visible focus,
  no accidental submission and sensible focus restoration after dialogs.
- Correct text entry including Unicode and SQL punctuation, selection/copy/paste
  within approved test scope. Inspect contents before sending/executing.
- Clear empty/loading/error/success states, actionable validation and recovery.
- No lost work or hidden state when switching panels, connections or tabs.
- Disabled actions explain their prerequisites; icon-only controls have names.

## Suggested database-client journey (adapt to actual features)

1. Fresh isolated profile → empty connections state → new connection form.
2. Invalid input → visible validation → correct it without losing other values.
3. Connect only to a disposable approved database → visible connection/schema.
4. Enter a known safe read-only query → execute → verify headers and row values.
5. Inspect a wide result set, horizontal/vertical scrolling and resized panels.
6. Exercise a safe query error → actionable message → recover and run again.

Use fixtures for large grids and difficult error states, labelled as fixtures.
An in-process fixture cannot establish real connection or query execution.
Do not run a repository's database setup script until its host, ports, volumes,
cleanup and data ownership have been checked. Never use production as a shortcut.

## Per-run evidence record

```text
Request / acceptance check:
Checkout / revision / dirty state / binary:
Build and launch commands:
Display / owned workspace and PID / renderer and adapter:
Window size / DPI / theme / fonts / locale / fixture:
Before image (actually inspected):
Action and target:
Observed resulting state and assertions:
After image (actually inspected):
Logs / component and live-app test results:
Intentional visual differences / baseline approval status:
Unverified platforms, interactions or GPU/session checks:
Cleanup and preserved artifacts:
```

Do not put secrets, real query results or complete environment dumps in this
record. Before publishing evidence, review both images and text for private data.
Generated screenshots and a green diff are evidence inputs, not human sign-off.
