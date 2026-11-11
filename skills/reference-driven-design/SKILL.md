---
name: reference-driven-design
description: >-
  Build or restyle interfaces from visual references the user chose (screenshots,
  links, Mobbin/Dribbble/CollectUI/Unsection shots, component library examples)
  instead of the agent's own taste. Use whenever UI work starts without an
  approved project design system, when the user sends prints or references, says
  the result looks generic, "SaaS-like", or "AI slop", or wants the project to
  keep one consistent look. Asks for references before inventing a style,
  extracts measurable traits, records them as the project's design system, and
  proves the result with side-by-side comparison. Carries no palette, font, or
  style of its own.
---

# Reference-driven design

The agent's unaided visual defaults are the problem this skill exists to avoid:
they converge on the same generic product look (centered hero, gradient accent,
three icon cards, one sans-serif, rounded cards with soft shadows). Generic
"design skills" that prescribe a style only replace one default with another.

This skill contributes **no taste**. Taste comes from references the user picked.
The agent's job is to observe them precisely, turn what it sees into explicit
project rules, build against those rules, and show the result next to the
references until the gap is closed.

References alone are not enough: copying one well-made product only produces a
more polished generic. The result needs two layers — the **reference layer**
(structure, density, quality bar) and the **identity layer** (a few moves that
only this product could have, drawn from its name, domain, and voice).

Rule of traceability: **every visual decision in the output must trace to a
reference, to the product's identity, or to a token in the project's design
system.** A decision that traces to none of these is a default, and defaults are
removed or replaced.

## 1. Find what already governs the look

Read the repository's agent instructions and look for an existing design
document, token files (CSS variables, Tailwind/theme config, design tokens JSON,
platform theme files), and a component library already in use.

- **An approved design system exists:** follow it. New references may only
  extend it (a new component, a new screen type). If a reference contradicts it,
  ask whether the system should change; never mix both silently.
- **Nothing exists, or the owner rejected the current look:** continue. The
  outcome of this skill becomes the project's design system.

## 2. Get references before choosing anything

If the user has not provided references, ask for them before writing any styled
UI. Ask for 2–5, for the exact kind of screen being built, and name where to
find them:

| Source | Good for | Caveat |
| --- | --- | --- |
| Mobbin | real shipped app flows, web and mobile | best signal for usability; screens are production work |
| CollectUI, Unsection | a specific component or landing section by category | compare several before picking one |
| Dribbble | visual direction, mood, color, type | many shots are concepts never shipped; check they survive real content |
| 21st.dev and other component libraries | implementation of a single component | check license, dependencies, and accessibility before adopting |
| Products the user already likes | overall feel | take patterns, not their identity |

Accept anything concrete: screenshots, URLs, a Figma frame, an existing screen
of the user's own product. If the user asks the agent to find references, search
those sources, present 4–8 candidates with links and one line each on what they
offer, and let the user choose. Do not pick on their behalf. Prefer shipped
products over concept shots: concept galleries are where the generic look comes
from.

When the user names a product instead of sending images, get real images of it
before extracting anything: official product imagery on its site, app store
screenshots (they show the actual app at high resolution), or public docs.
Marketing renders may be blurred, cropped, or stylized; use only the sharp parts
and say which parts were unreadable. Never extract from memory of what the
product "usually looks like".

If the user explicitly wants to proceed without references, build structure
only (layout, hierarchy, states) with neutral, unstyled defaults and say the
visual layer is pending references. Do not invent a "temporary" style; it
becomes the permanent one.

For each reference, record its **role**: what to take from it. One reference is
rarely right for everything. Example: "A: density and table layout; B: color and
type; C: the empty state." Ask when the role is not obvious.

## 3. Extract measurable traits

Look at each reference at full resolution and write observations as values, not
adjectives. "Clean and modern" is not an observation; "body 14px/20px, 1px
#E4E4E7 dividers instead of card shadows, 8px base spacing" is. Use the
[extraction sheet](references/extraction-sheet.md) and cover:

- **Layout:** grid, columns, max content width, alignment, how sections are
  separated (space, rule, background change), density.
- **Spacing:** the base unit and rhythm; estimate pixels from known-size
  elements (text line height, a standard icon, the device width).
- **Typography:** family classification (and the name if identifiable), size
  steps and their ratio, weights in use, case, tracking, numeral style.
- **Color:** background and surface steps, text levels, the accent and where it
  is used, status colors, how much of the screen is colored. Sample real pixel
  values from image files with an available tool; label estimates as estimates.
- **Shape and depth:** radii per element type, borders vs. shadows vs. fills,
  elevation steps.
- **Components:** anatomy and states visible in the reference (buttons, inputs,
  rows, navigation, empty/loading/error if shown).
- **Iconography and imagery:** stroke vs. fill, size, weight; photo,
  illustration, or none.
- **Signature moves:** the 2–4 specific choices that make it look like itself
  and not like a template. These are what generic output lacks.
- **Do not take:** logos, illustrations, brand marks, copy, and the overall
  composition that identifies the source product.

When references disagree on a trait, name the conflict and resolve it by the
roles from step 2; ask the user when the roles do not settle it.

Then define the **identity layer**: 1–3 moves that come from the product itself,
not from any reference. Derive them from the product's name, the object or
ritual in its domain, and its voice (for example a ledger rule, a stamp, a
handwritten mark, a field-guide label). Rules for them:

- each one has a job (marks current place, confirms an action, labels a
  section), never pure decoration;
- they are used sparingly, so they stay recognizable; one per screen region is
  usually plenty;
- they must survive the platforms the system will reach (web, mobile, back
  office): prefer moves expressible as color, type, line, and shape over
  custom illustrations;
- if an existing project document contradicts the owner's current request for
  identity, the current request wins; record the change.

Before building, show the user the extracted traits, signature moves, and
identity moves in a short summary. Misreading a reference is cheaper to fix here
than in code. If the user already approved the direction and asked to proceed,
show the summary and continue without waiting.

## 4. Record it as the project's design system

Write the result where the repository keeps design or documentation (if nothing
exists, propose `docs/design-system.md`) using the
[design system record](references/design-system-record.md):

- a reference board: each reference with link or file, role, and date;
- tokens with values and the reference (or identity) each came from;
- component rules and states;
- the signature and identity moves as MUST rules, and the observed defaults to
  avoid as MUST NOT rules;
- how the system maps to the other surfaces it may reach (web app, back office,
  mobile): which tokens and moves carry over unchanged and which adapt;
- a short checklist for reviewing new screens.

Put tokens in the stack's native mechanism (CSS custom properties, theme config,
platform theme) so components cannot drift from the record. Point the agent
instructions file (for example `AGENTS.md`) to the record as the source of
truth for interface work, so later sessions follow the same patterns.

Store third-party screenshots only where the user approves; prefer links in
public repositories. The user's own screenshots and assets can live with the
project.

## 5. Build against the record

- Use the project's existing component library and restyle it through tokens; do
  not hand-tune values inside components.
- Start at the foundation: when screens already use shared tokens or theme
  names, re-point those names to the new values first, so every screen moves
  at once; keep legacy names as aliases until usages are migrated. Then fix the
  shell (navigation, top bar) and shared components, and only then individual
  screens.
- When adopting a component from a library such as 21st.dev, check license,
  dependencies, and accessibility first, then restyle it to the tokens.
- Use real or honestly empty content. Do not fill screens with invented metrics,
  testimonials, logos, or people to make them resemble a reference.
- Keep accessibility non-negotiable: text contrast at least 4.5:1 (3:1 for large
  text and essential UI boundaries), visible focus, labelled controls, usable
  target sizes, reduced-motion handling. If a reference fails one of these,
  adjust the value minimally and record the deviation.

## 6. Compare side by side and close the gap

Capture the implemented screen at the same viewport as the reference, using the
repository's tooling or an approved browser/screenshot tool. Put both next to
each other and review trait by trait from the extraction sheet:

1. list every visible difference that the reference's role covers;
2. fix them, or record why the difference is intentional;
3. recapture and repeat until no unintended difference remains, or report the
   remaining gaps honestly after a reasonable number of rounds.

Then look at every other screen the change touched, not only the one that
matches the reference. Token swaps create new pairs that nobody chose (a
selected label that was dark on a bright fill is now dark on a dark fill), and
mechanical replacements miss cases. Rerun the project's visual or accessibility
checks and compare their findings with the run before the change; a new finding
is a regression to fix, not noise.

Screens outside every reference's role (for example a login page when the
references only cover dashboards) receive the tokens only. Record them as
uncovered and ask for a reference before redesigning them further.

Then run the slop audit on the result. Each item below is acceptable only if a
reference shows it; otherwise remove it:

- gradient or purple/indigo accent with no source;
- centered hero with a pill badge above the heading and gradient text;
- a row of three cards with an icon in a rounded square;
- every container as a rounded card with a soft shadow;
- one sans-serif at uniform weights with no size contrast;
- emoji used as interface icons;
- glass or blur effects over content;
- micro-labels in letter-spaced CAPS above every group;
- summary cards tinted by meaning (a green card, a red card, a dark card) or a
  row of colored counters, where the reference uses neutral cards and a cue;
- a monospace font for money or metrics in a non-technical product;
- identical spacing everywhere, with no rhythm between groups;
- generic copy ("Get started", "Unlock the power of…") instead of product
  language;
- decorative color that marks nothing.

## Report

State which references were used and their roles, the identity moves and where
they appear, where the design system was recorded, what was compared (with the screenshots), remaining differences, and
any accessibility deviations from a reference. Do not describe the result as
matching a reference that was not visually compared.

## Guardrails

- Never apply a style from memory or from another skill when the user provided
  references; references win.
- Take patterns and measurements, not identity. Do not recreate a specific
  product's brand, artwork, or layout signature, even if asked to make it
  "identical"; explain the boundary and offer the pattern-level version.
- Do not install design tools or component libraries without approval.
- Preserve behavior, data, routes, and public contracts when restyling.
