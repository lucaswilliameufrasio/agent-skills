# Control Room components

Markup is plain HTML so it maps to any framework. Class names are examples;
keep the project's naming. All values come from `tokens.css`.

## Page header

```html
<header class="page-header">
  <div>
    <div class="eyebrow">Nginx / Control room</div>
    <h1>Targets</h1>
    <p class="muted">One sentence saying what this page is for.</p>
  </div>
  <div class="header-actions"><button type="button">Add a target</button></div>
</header>
```

```css
.page-header { display: flex; justify-content: space-between; align-items: end; gap: 24px; padding-bottom: 26px; border-bottom: 1px solid var(--line); }
.header-actions { display: flex; align-items: center; gap: 16px; }
@media (max-width: 650px) { .page-header { display: block; } .header-actions { margin-top: 20px; justify-content: space-between; flex-wrap: wrap; } }
```

## Panel with header and status

```html
<section class="panel" aria-labelledby="certs-heading">
  <div class="panel-header">
    <div><div class="eyebrow">Identity</div><h2 id="certs-heading">Certificates</h2><p>What this section controls.</p></div>
    <span class="status good">DNS-01 ready</span>
  </div>
  …
</section>
```

```css
.panel-header { display: flex; justify-content: space-between; align-items: baseline; gap: 16px; margin-bottom: 16px; }
.panel-header > .status { flex: 0 0 auto; white-space: nowrap; }
@media (max-width: 760px) { .panel-header { flex-wrap: wrap; } .panel-header > div:first-child { flex: 1 1 100%; min-width: 0; } }
```

Sections stacked on a page are separated by 28px. A nested card inside a panel
uses `--raised`, `1px solid var(--line)` and radius 11px, without the hard
shadow, so only top-level surfaces look "pressed out".

## Clickable card (inventory)

```css
.inventory { display: grid; grid-template-columns: repeat(auto-fit, minmax(270px, 1fr)); gap: 16px; padding-top: 28px; }
.card-link { display: block; padding: 22px; border: 2px solid var(--outline); border-radius: var(--radius-surface); background: var(--panel); box-shadow: 0 4px 0 var(--shadow-deep); color: var(--ink); transition: border-color .18s, transform .18s; }
.card-link:hover { border-color: var(--cyan); transform: translateY(-2px); }
.card-meta { display: flex; justify-content: space-between; gap: 12px; color: var(--muted); font-size: .82rem; }
```

## Buttons

- Primary (gold) for the one main action of a form or panel.
- `.secondary` (transparent, `--line-strong` border, no shadow) for neutral
  actions next to it: Cancel, Remove (before confirmation), Send test.
- `.danger` only inside a confirmation step for destructive actions.
- Busy state: disable, keep the width, replace the label with a short
  progress verb ("Sending…"). Never leave a button enabled during a request.
- Buttons in a row: `display: flex; flex-wrap: wrap; gap: 10px`; labels never
  wrap (`white-space: nowrap; flex: none`).

## Status dot and state chip

Use the **status dot** (`.status.good|warn|bad`) for section-level state in a
header ("Unlocked", "3 open alerts"). Use the **state chip**
(`.state-chip.state-good|warn|bad|neutral`) inside tables and lists. Both
always carry a word; pair a warning chip with a one-line explanation below it
(`.field-help`, muted, `.8rem`).

## Form card

```html
<form class="form-card">
  <label>Domains<input name="domains" placeholder="example.com, *.example.com" required></label>
  <label>Challenge<select name="challenge">…</select></label>
  <div class="form-actions"><button type="submit">Request certificate</button><span class="field-help">Short hint about consequences.</span></div>
</form>
```

```css
.form-card { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; align-items: end; margin-top: 16px; padding: 16px; border: 1px solid var(--line); border-radius: 7px; background: var(--raised); }
.form-actions { grid-column: 1 / -1; display: flex; gap: 12px; align-items: center; }
.form-actions button { flex: none; white-space: nowrap; }
.inline-check { display: flex; align-items: center; gap: 9px; color: var(--ink); font-size: .78rem; font-weight: 750; }
.field-help { color: var(--muted); font-size: .8rem; line-height: 1.45; }
@media (max-width: 900px) { .form-card { grid-template-columns: 1fr 1fr; } }
@media (max-width: 560px) { .form-card { grid-template-columns: 1fr; } }
```

Validation: mark the field `aria-invalid="true"`, add a `.field-error`
paragraph linked by `aria-describedby`, and clear it on input. Messages say
what to enter ("Enter the topic name: letters, digits, - or _"), never only
"invalid". Secrets use `type="password"`, `autocomplete="off"`, and the page
never shows a stored secret back; offer "Leave empty to keep the stored value".

## Tables and responsive cards

Tables live inside a panel. Under 760px, either scroll inside the panel
(`display: block; overflow-x: auto`) or turn rows into labelled cards:

```css
@media (max-width: 760px) {
  table.responsive-cards, table.responsive-cards tbody { display: block; width: 100%; }
  table.responsive-cards thead { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0, 0, 0, 0); }
  table.responsive-cards tbody tr { display: grid; margin: 0 0 12px; padding: 8px 12px; border: 1px solid var(--line); border-radius: 10px; background: var(--panel); }
  table.responsive-cards tbody td { display: grid; grid-template-columns: minmax(7rem, 38%) minmax(0, 1fr); gap: 10px; padding: 9px 0; border-bottom: 1px solid var(--line); overflow-wrap: anywhere; }
  table.responsive-cards tbody td:last-child { border-bottom: 0; }
  table.responsive-cards tbody td::before { content: attr(data-label); color: var(--muted); font-size: .7rem; font-weight: 800; letter-spacing: .06em; text-transform: uppercase; }
}
```

Each `td` carries `data-label` with its column name. Empty tables show a
`.table-empty` block: a bold sentence of what is missing and a muted sentence
of the next action.

## Side navigation (detail pages)

```css
.workspace { display: grid; grid-template-columns: 250px minmax(0, 1fr); gap: 22px; padding-top: 24px; align-items: start; }
.workspace nav { display: grid; gap: 16px; position: sticky; top: 20px; }
.workspace nav a { display: block; padding: 11px 12px; border: 1px solid var(--line); border-radius: 6px; color: var(--muted); background: var(--panel); }
.workspace nav a:hover, .workspace nav a.active { border-color: var(--cyan); color: var(--ink); background: var(--raised); }
.workspace nav a.active { border-left: 3px solid var(--accent); }
.nav-group-title { padding: 0 10px; color: var(--accent); font-size: .68rem; font-weight: 800; letter-spacing: .12em; text-transform: uppercase; }
@media (max-width: 760px) {
  .workspace { grid-template-columns: 1fr; gap: 14px; }
  .workspace nav { display: flex; gap: 8px; overflow-x: auto; position: static; }
  .workspace nav a { flex: 0 0 auto; min-width: 126px; }
}
```

Each link has a bold title and a muted one-line description.

## Next-step cards

Guide the user to the next task after an empty or partial state:

```css
.next-steps { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 10px; margin-top: 12px; }
.next-step { display: grid; gap: 7px; padding: 14px; border: 1px solid var(--line); border-left: 3px solid var(--accent); border-radius: 5px; background: var(--raised); color: var(--ink); }
.next-step span { color: var(--muted); font-size: .76rem; }
.next-step:hover { border-color: var(--accent); background: #26384a; }
```

## Notices

- Warning: `padding: 12px 14px; border: 1px solid var(--accent); border-radius: 10px; font-size: .84rem`.
- Error: same with `border-color: var(--danger); color: #f0c0b9`, `role="alert"`.
- Guidance: `border-left: 3px solid var(--cyan); background: var(--raised)`.

## Toast

Fixed top-right region (`aria-live="polite"`), width `min(430px, 100vw - 36px)`;
each toast `padding: 14px 16px; border: 1px solid var(--line); border-radius:
11px; background: var(--panel); box-shadow: 0 12px 40px #0009`. Success border
cyan, error border coral with `role="alert"`. Success disappears after ~4.5s,
errors after ~12s; diagnostics go in a `<pre>` below the message. After a
reload, carry a pending success message through `sessionStorage`.

## Confirmation dialog

Use a native `<dialog>` with `showModal()`, never `window.confirm`:
`width: min(460px, 100vw - 32px)`, panel surface with the 2px outline and hard
shadow, backdrop `#080b0acc` with a 3px blur. Title names the action ("Remove
channel"), the message names the object and the consequence, the confirm
button repeats the verb, Cancel is a dark secondary button
(`background: #18201c`, hover border cyan).

## Disclosure

`details > summary` styled as a primary button opens inline forms ("Add a
channel", "Edit channel"). Keep one primary action visible per panel; secondary
forms stay collapsed until asked for.
