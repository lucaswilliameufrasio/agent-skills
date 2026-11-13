---
name: control-room-design
description: >-
  Opt-in visual style "Control Room": a dark, arcade-flavoured admin look with a
  navy canvas, warm brown panels, gold actions with chunky shadows, cyan links
  and focus, pixel-font eyebrows and dotted status chips. Use ONLY when the user
  explicitly asks for this style by name ("Control Room design", "control-room
  style", "the nginx-gateway-manager look", "the NGM design"). Never apply it by
  default, never pick it because a task involves UI, and never use it to restyle
  a project that already has its own design system.
---

# Control Room design

A complete, portable visual style for dashboards, admin panels and operator
tools. It comes from an Nginx control panel whose palette was carried over from
an arcade game: dark and calm for long sessions, with game-like, tactile
controls.

## Activation rule (read first)

This skill is **opt-in**. Apply it only when the user's current request names
it, as listed in the description. If you loaded it for any other reason, stop
and follow the project's own design instead. When a project already has a
design system or design document, ask before replacing it; do not mix the two.

Once it is requested, apply the whole system: tokens, type, components and the
checklist below. A partial adoption (only the colors) looks broken.

## Concept

- **Mood:** a night-shift control room. Deep navy room light, warm wooden
  consoles, brass/gold buttons you can press.
- **Arcade cues, used sparingly:** pixel-font eyebrows, hard offset shadows
  (`0 3px 0` / `0 4px 0`, no blur), 2px near-black outlines on raised
  surfaces, a hard text shadow on the page title. Everything else stays a
  plain, readable admin UI.
- **Colour has jobs:** gold = primary action and current place; cyan =
  navigation, links, focus and "healthy"; coral = danger and errors. Do not use
  them decoratively.
- **Dark only.** `color-scheme: dark`. There is no light theme.

## Tokens

The full stylesheet is in [references/tokens.css](references/tokens.css); copy
it, then adapt names to the project's conventions (CSS variables, Tailwind
theme, design-token JSON, Flutter `ThemeData`, terminal palette).

| Token | Value | Use |
| --- | --- | --- |
| `--canvas` | `#172338` | page background, input fill |
| canvas glow | `radial-gradient(ellipse at 50% -24%, #315582 0, transparent 58rem)` | top light over the canvas |
| `--panel` | `#241c19` | cards and sections |
| `--raised` | `#33251b` | nested cards, form cards, hovered rows |
| `--line` | `#594633` | dividers and decorative borders |
| `--line-strong` | `#8a7240` | borders that are the only cue (inputs, outlined buttons) |
| `--ink` | `#fff7e6` | primary text |
| `--muted` | `#d0c1ac` | secondary text, table headers |
| `--accent` | `#f2c230` | primary buttons, eyebrows, active nav edge, page title |
| `--accent-strong` | `#ffe08a` | hover of gold elements |
| `--cyan` | `#6fc3ff` | links, focus ring, code, healthy status |
| `--danger` | `#ff8b78` | errors, invalid fields, destructive outline |
| `--outline` | `#1b1410` | 2px outlines and hard shadows of raised surfaces |
| `--shadow-deep` | `#0b111b` | hard shadow under panels |
| state good / warn / bad / neutral | `#8fdfb5` / `#f0c978` / `#ffaaaa` / `#b5c1cf` | status chips |

Measured contrast (WCAG): ink on panel 15.7:1, muted on panel 9.5:1, muted on
canvas 8.9:1, gold on panel 10.0:1, cyan on panel 8.7:1, coral on panel
7.3:1, button text `#21180d` on gold 10.4:1, chip colours on panel 9.2–10.7:1.
`--line` on panel is only 1.9:1, so it may decorate but must not be the only
boundary of a control; use `--line-strong` (3.6:1) there.

## Type

- **Body:** `Inter, "Segoe UI", ui-sans-serif, system-ui, sans-serif`. Body
  copy line-height 1.5–1.55; secondary copy in `--muted`.
- **Pixel accent:** `"Press Start 2P", ui-monospace, "Courier New", monospace`
  only for eyebrows (section kickers) at `.62rem`, uppercase, `letter-spacing
  .08em`, gold. Self-host the font file; do not load it from a third-party CDN.
  The monospace fallback is acceptable.
- **Page title (h1):** `clamp(2rem, 5vw, 3.8rem)` (index pages up to `5rem`),
  `line-height .92–.95`, `letter-spacing -.07em`, gold with
  `text-shadow: 3px 3px 0 var(--outline)`.
- **Section title (h2):** `1.15–1.2rem`, ink. Headings use `text-wrap: balance`.
- **Labels:** `.78rem`, weight 750, ink. **Table headers:** `.68rem`,
  uppercase, `letter-spacing .12em`, muted.
- **Numbers and times:** `font-variant-numeric: tabular-nums`; times
  `white-space: nowrap`. Code and identifiers in cyan, `overflow-wrap: anywhere`.

## Layout

- Content width `min(1120px, calc(100% - 40px))`, centred; mobile
  `min(100% - 24px, 600px)`.
- Page header: eyebrow, h1, one muted sentence; actions on the right; a
  `1px --line` rule below.
- Detail pages: a 250px sticky side navigation of cards next to the content;
  under 760px it becomes a horizontal scroll strip.
- Panels: padding 22–23px (17px on mobile). Inventories use
  `grid-template-columns: repeat(auto-fit, minmax(270px, 1fr))`, gap 16px.
- Breakpoints: 760px (mobile layout, tables become cards), 900–1100px (tables
  scroll horizontally), 380px (stack header actions).

## Components

Recipes with markup and CSS are in
[references/components.md](references/components.md): raised panel, page
header, primary/secondary/danger buttons, status dot and state chip, form card
with field errors, tables with responsive cards, side navigation, next-step
cards, empty state, toast, confirmation dialog, disclosure (`details`).

The non-negotiable details:

- **Primary button:** gold fill, `#21180d` text, weight 850, `2px solid
  --outline`, radius 5px, `box-shadow: 0 3px 0 --outline`; hover
  `--accent-strong`; disabled `opacity .68` with `cursor: wait` while busy.
- **Raised surfaces** (panels, cards, dialogs): `2px solid --outline`, radius
  6px, `box-shadow: 0 4px 0 --shadow-deep`.
- **Focus:** every interactive element gets `outline: 3px solid --cyan;
  outline-offset: 3px` on `:focus-visible`. Never remove it.
- **Status:** a 6–7px dot in `currentColor` before the label; colour is never
  the only signal, the label always says the state.

## Motion

Short colour transitions only (`.14–.18s ease`), and a 2px lift on hoverable
cards. Honour `prefers-reduced-motion: reduce` by removing transitions and
transforms. No looping animation.

## Platforms other than the web

- **Mobile (Flutter, SwiftUI, Compose):** same palette and roles; 44–48pt touch
  targets; keep the hard shadow on primary buttons; pixel font only in
  eyebrows; follow the platform's navigation patterns instead of the web side
  navigation.
- **Terminal (TUI):** canvas as the terminal background where the user allows
  it, gold for the selected item and primary key hints, cyan for focus and
  links, coral for errors, muted for help text. No pixel font; use bold
  uppercase for eyebrows. Respect `NO_COLOR`.

## Checklist before handing over

- [ ] The user asked for this style by name in the current request.
- [ ] Tokens defined once and used everywhere; no stray hex values in
      components.
- [ ] Gold only on primary actions, eyebrows, current place and the page
      title; cyan only on links, focus, code and healthy states.
- [ ] Every control has a visible `:focus-visible` ring and a boundary of at
      least 3:1 (fill change or `--line-strong`).
- [ ] Status chips have a text label; errors name the field and the fix.
- [ ] Tables become labelled cards under 760px or scroll inside their panel;
      no page-level horizontal scroll at 390px wide.
- [ ] `prefers-reduced-motion` removes transitions and transforms.
- [ ] The pixel font is self-hosted or falls back to monospace; no external
      font CDN.
- [ ] Checked in a real browser or device at desktop and 390px widths, with
      screenshots, before calling the work done.
- [ ] The hierarchy gate and the craft gate in the design-system-definition
      skill pass. This style's recorded exceptions are the gold page title, the
      pixel eyebrows, and the hard shadow as its one material. Do not add a
      second material or paint anything else with the accent.
