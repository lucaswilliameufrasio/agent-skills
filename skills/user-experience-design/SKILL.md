---
name: user-experience-design
description: >-
  Shape how an app works for its users: one job per screen, clear flows, every
  screen state (empty, one, many, error), feedback, and perceived speed
  (prefetch on intent). Use when building or reviewing screens or flows.
---

# Design the user experience

Visual polish does not rescue a confusing product. This skill covers what the
user goes through: which screen does which job, how they move between them,
what every screen shows in every situation, how the app answers each action,
and how fast it feels. It works on web, mobile, desktop, and terminal apps.

It contributes no visual style. Colors, type, and components come from the
project's design system (see [which skill to use](#which-skill-to-use)).

The order is the method: **job → structure → states → interaction → speed →
proof**. Do not lay out a screen before its job and its states are known.

## 1. Start from the user's job

For each screen or flow in scope, write down from the code, the product docs,
or the request:

- who uses it, the one thing they came to do, and how they arrive (link, menu,
  notification, deep link, search);
- what they need to see to decide, and the one primary action;
- what "done" looks like, and where they go next;
- how often they do it, and what a mistake would cost them.

When the request covers a whole system or a new feature area, map actors and
journeys with `system-module-architecture` first, then return here for each
screen.

## 2. Structure: one job per screen

A screen that does everything is the most common failure of generated
interfaces. Signs:

- several unrelated primary actions, or more than one filled primary button;
- create, browse, edit, configure, and delete forms on the same page;
- tabs or accordions used to hide jobs that should be separate places;
- settings and destructive actions next to everyday tasks;
- a page that has to scroll through sections nobody needs at the same time;
- no URL, route, or back step for a place the user clearly went to.

Split when the intent, permission, risk, frequency, or lifecycle differs. Use
the lightest container that fits the job:

| Job | Container |
| --- | --- |
| Find and pick among many items | list or search screen; filters and sort stay on it |
| Look at one item and act on it | detail screen with its own URL or route |
| Short, interrupting task that returns to the same place (rename, confirm, quick add) | dialog, sheet, or inline edit |
| Long creation with dependent steps | dedicated page or a stepped flow with saved progress |
| Rare configuration | settings area, grouped by topic, out of the daily path |
| Destructive or irreversible action | its own confirmation step, apart from frequent actions |
| Watching many things at once | dashboard, only when monitoring is the job, with each tile leading to its detail |

Do not over-split either: steps the user always does together, with the same
data in view, belong on one screen. A wizard for a three-field form is worse
than the form.

Navigation rules:

- The user can always tell where they are, how they got there, and how to go
  back. Back returns to the previous place with its scroll, filters, and
  selection intact.
- State the user would share or come back to (filters, tab, selected item,
  page) lives in the URL or the platform's equivalent.
- Mutually exclusive overlays and modes are one state value, not several
  booleans (see `single-state-enum`).
- Top-level choices stay few; the rest is reached through the screens above.

When asked to build the "single screen for everything", explain the competing
jobs, propose the split, and build the smallest coherent set of screens. Ask
only when the split changes a product decision.

## 3. States: design every one, not just the full screen

A screen designed only with a comfortable amount of sample data is unfinished.
For every screen and shared component, fill the
[state matrix](references/screen-states.md) before building, and mark each row
**designed**, **not applicable** (with the reason), or **pending**. At minimum,
think through:

- **amount:** first use with nothing, nothing matching a search or filter,
  everything cleared, exactly one, a few, many with paging, and more than the
  layout was drawn for;
- **content:** long names, missing optional fields, missing images, other
  languages, large text settings;
- **time:** first load, reload over existing data, saving, slow, offline,
  stale data;
- **failure:** a recoverable error with retry, a fatal error, a validation
  error, partial success in a batch;
- **access:** no permission, read-only, signed out, expired session;
- **done:** the moment the job finishes is a calm, visible place, not a toast
  over the same form.

Each empty state says what is missing and offers the next useful action. The
first-use empty state, the "no results" state, and the "all done" state are
three different screens with different copy and actions.

A matrix row is not designed until it has been rendered with a fixture or real
data and looked at (step 6).

## 4. Interaction and feedback

- Acknowledge every action within about 100 ms (pressed state, focus, change
  of label). Show progress past about 400 ms. Past about 1 s on a known layout,
  show a skeleton of that layout instead of a spinner. Past about 10 s, show
  real progress and let the user cancel or leave and come back.
- Keep the previous content visible while a filter, sort, or page loads;
  replacing a list with a spinner on every keystroke loses the user's place.
- Reserve space for content that loads late so the layout does not jump.
- Optimistic updates are for actions that almost always succeed and are cheap
  to undo (like, reorder, mark as read). Roll back visibly on failure and say
  why. Payments, irreversible deletes, and anything with external effects wait
  for the real answer.
- Prefer undo to a confirmation dialog when the action is reversible. Keep
  confirmation for what cannot be undone, and name what will be lost.
- A disabled control says why it is disabled and what enables it. Do not
  disable the submit button as the only form validation.
- Forms: ask only for what the job needs; validate a field when the user leaves
  it, not while typing the first character; put the error next to the field in
  words that say how to fix it; keep everything the user typed after a failed
  submit; protect unsaved changes when the user navigates away.
- Move focus on purpose: to the new screen's heading after navigation, into a
  dialog when it opens, back to the trigger when it closes, to the first error
  after a failed submit.
- Every action works by keyboard (and screen reader or switch on mobile);
  frequent users get shortcuts for frequent actions.

## 5. Perceived speed

Make the app feel fast by starting work before the user waits for it. Measure
first: know which navigation or action is slow and where the time goes
(`performance-optimization` owns finding real bottlenecks).

**Prefetch on intent** loads the data or code for a likely next screen when
the user shows intent (pointer resting on a link, focus on it, the press
starting, the item scrolling into view), so the screen is ready when they
arrive. Use it for navigation to read-only screens the user is likely to open,
such as list → detail or the next step of a flow. Do not use it for anything
with side effects, for costly or rate-limited requests, or on metered
connections. Details, signals, framework hooks, and limits are in
[perceived performance](references/perceived-performance.md).

Other techniques in that reference: stale-while-revalidate caching, skeletons
that match the real layout, optimistic updates, keeping previous data during
transitions, loading the code for the next route ahead of time, and rendering
the first screen before secondary panels.

A technique that hides slowness is not a fix for a slow backend; report the
slow call as well.

## 6. Prove it on the real app

- Drive each journey end to end on the running app, as the user would,
  including the back button and a reload in the middle.
- Render every matrix row with a fixture or real data and capture it at the
  sizes that matter. Look at each capture. Use the project's verification
  path; when there is none, create one with `create-verification-skill`.
  Native desktop apps follow `desktop-visual-qa`.
- Walk the main journey by keyboard only.
- For prefetching, show in the network or request log that hovering or focusing
  fetches the target once, that navigation then uses it, and that no request
  with side effects was prefetched.
- Report each screen with its matrix: designed and verified, not applicable
  (why), or pending. Do not call a screen done while rows are pending.

## Which skill to use

Not every agent or harness knows which skill fits which part of interface work.
Use this table, and name the skill you used in the report:

| Need | Skill |
| --- | --- |
| Actors, journeys, and modules for a new system or feature area | `system-module-architecture` |
| Web feature structure, data sources, validated API calls | `web-capability-architecture` |
| Visual style from references the user chose | `reference-driven-design` |
| A complete design system when there are no references | `design-system-definition` |
| Restyle every screen of an existing app | `interface-redesign` |
| One state value for overlays and modes | `single-state-enum` |
| Pagination, error bodies, and API shape behind a screen | `http-api-conventions` |
| A slow screen or endpoint, measured | `performance-optimization` |
| A repeatable way to drive the real app and capture evidence | `create-verification-skill` |
| Native desktop screenshots and interaction checks | `desktop-visual-qa` |
| Proving the delivery meets each request | `acceptance-traceability` |

The hierarchy and craft gates and the ethical limits on engagement in
[psychology and heuristics](../design-system-definition/references/psychology-and-heuristics.md)
apply to every screen; if that file is not installed, read it from the
agent-skills collection.

## Guardrails

- Never fill a screen with invented items, counts, people, or reviews to make
  it look complete. Use real data, fixtures clearly marked as fixtures in tests
  and demos, or an honest empty state.
- No dark patterns: no fake urgency, confirmshaming, hidden cancel or opt-out,
  pre-ticked consent, or endless feeds added to raise time spent.
- Never prefetch or optimistically apply a request that changes data, sends a
  message, charges money, or counts as a view the business reports.
- Preserve existing routes, deep links, and persisted state when restructuring;
  redirect old URLs instead of breaking them.
- A screen structure change that alters what users can do is a product
  decision; state it and get agreement before removing a path users rely on.
