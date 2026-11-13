# Psychology and heuristics for design decisions

Pick the principles that apply to the product; cite them in the design document
next to the decision they justify. Each engagement pattern needs an ethical
boundary written beside it.

Citing a principle is not applying it. A screen is done only when its rendered
capture passes the screen hierarchy gate and the craft gate below. This is the
check for every design skill in this collection. Do not wait for the owner to
ask.

## Perception and trust

| Principle | What it means for decisions |
| --- | --- |
| Aesthetic-usability effect | Polished, consistent interfaces are perceived as easier and more trustworthy. Consistency (one radius, one icon style, one accent) is the cheapest polish. |
| First impression (about 50 ms) | The first viewport decides credibility. It must show the product's real content and purpose, not a generic hero. |
| Visual hierarchy and contrast | One dominant element per view; size, weight, and color establish order. Several equally loud elements read as noise. |
| Gestalt grouping | Proximity and shared containers say "these belong together". Use spacing before borders. |
| Von Restorff (isolation) | The one thing that differs gets noticed: reserve the accent for the primary action and current state. |
| Serial position, peak-end rule | People remember the first, the last, and the best moment. Design the first view and the moment of success (saved, played, finished) carefully. |

## Effort and choice

| Principle | What it means for decisions |
| --- | --- |
| Jakob's law | Users spend most time in other products; follow established conventions for navigation, players, forms, and keyboard shortcuts. |
| Hick's law | Decision time grows with options. Few top-level choices, progressive disclosure for the rest. |
| Fitts's law | Frequent and important targets are large and close; destructive ones are not adjacent to frequent ones. |
| Miller / chunking | Group information into small, labeled sets rather than long undifferentiated lists. |
| Recognition over recall | Show state, history, and options instead of requiring memory. |
| Doherty threshold | Respond in under about 400 ms or show progress; skeletons over spinners for known layouts. |
| Tesler's law | Complexity moves to the system, not the user: sensible defaults, remembered preferences. |

## Motivation and return visits

| Pattern | Healthy use | Ethical boundary |
| --- | --- | --- |
| Hook model (trigger, action, variable reward, investment) | A real reason to return (new edition, new content the user asked for) | No artificial variable rewards, no streak pressure, no notifications without explicit consent |
| IKEA effect / investment | Favorites, notes, ratings, and collections the user builds and owns | Data is exportable and never held hostage; leaving is as easy as joining |
| Goal gradient / progress | Show real progress toward the user's own goal | No fake progress bars or inflated completion |
| Finite selection | A curated, complete set the user can finish | Do not convert to an endless feed to raise time-on-site |
| Social proof | Real, sourced signals only | Never invent counts, reviews, rankings, or "people are viewing" claims |
| Zeigarnik effect | Gentle "continue where you left off" | No guilt copy, no nagging reminders |

## Usability heuristics (Nielsen) as review questions

1. Is system status always visible (loading, saving, playing, offline)?
2. Does the language match the user's vocabulary, consistently?
3. Can the user undo, close, or go back from every state?
4. Is the same thing named, styled, and placed the same way everywhere?
5. Are errors prevented (confirmation for destructive actions, constraints on input)?
6. Are options visible rather than remembered?
7. Do frequent users have accelerators (keyboard, shortcuts, remembered filters)?
8. Is every element on screen earning its place?
9. Do error messages say what happened and what to do next, near the cause?
10. Is help available in context where it is needed?

## Screen hierarchy gate

Look at the capture, at the narrow size and the wide size. If it fails, fix
the screen and recapture. On a terminal, size becomes bold, dim, or reverse,
and a column becomes the next region. The same checks hold.

The dominant element is the user's own primary fact: the total, the work, the
status. It is never a manufactured goal, a sample, or a decorative hero.

1. **One dominant.** One element is the largest type. The task title is the
   next step down, then body, then captions. The page label, a section heading,
   and the primary fact do not share a size. When the primary fact is a number,
   name, or status, that fact is the dominant type. Its label is a caption in
   the same heading, so the accessible name still contains both.
2. **Quiet captions.** Brand metadata, hints, group labels, and the heading of
   a secondary region stay at caption size and a quieter color. A secondary
   region is not a second title.
3. **Groups by proximity.** Related facts sit together. Required inputs are one
   cluster. Optional or advanced inputs are a later cluster, with one label and
   one hint, separated by space before any rule. Do not repeat "optional" on
   every field. Do not add a sentence that restates the dominant fact or the
   task title.
4. **Neighbors stay neighbors.** On a wide layout the secondary region starts
   beside the task. The space beside the dominant element stays empty. A value
   stays next to its label. Do not stretch a row so a value crosses the gap and
   reads as part of the next region.
5. **One filled accent.** The primary action is the only filled accent. Current
   selection uses that accent as an outline or another non-fill mark, plus a
   cue that is not color. The dominant fact is not painted in the accent.
   Secondary and quiet actions do not share the primary control's fill, border,
   and weight.
6. **Required first.** The fields that unblock the job come first. The rest
   look later. Grouping is the disclosure. Collapse a group only when the owner
   asked for that extra step.
7. **Large primary, quiet reversal.** The primary control meets the platform
   target. In a form it is the full width of its group and sits at the end of
   that group. Undo, delete, and other reversals are quiet and are not next to
   it.
8. **Every element earns its place.** An empty state is one quiet sentence in
   the place that is empty. The first viewport on the narrow size shows the
   dominant fact, then the start of the task. The secondary region does not sit
   between them.

## Craft gate

A screen can pass the hierarchy gate and still look like a component kit.
Look at the same captures. If this gate fails, fix the screen and recapture.

1. **The subject is the figure.** The thing the product is about is the figure.
   Navigation, panels, and metrics are the ground. A wash, a blur, or a
   gradient that covers the subject fails. A missing image is an honest empty
   frame, not a decorative gradient standing in for the subject.
2. **Similarity means one kind.** One shape is one kind of thing. A page of
   identical cards that do different jobs fails. A second shape is for a second
   kind.
3. **Rhythm.** Inside a group the space is tight. Between groups there is a
   clear pause. The same gap between every block fails.
4. **One material.** One radius scale, one border weight, one elevation or
   none. Glass, blur, neon, and a new gradient on each panel are a second
   material. A gradient is allowed only where the design document gives it one
   job.
5. **The scan names the job.** In the first viewport a person can point to the
   object, the fact that decides, and the one action, without reading a
   paragraph. For a ticket those facts are the date, the place, and the price.
   For another product, name the deciding facts in the design document.
6. **The end is a place.** The moment the job finishes is its own calm state.
   A toast left on the same form is not that moment.

Do not add anchoring, decoys, artificial scarcity, countdowns, or invented
social proof to pass this gate. Those push a checkout. They do not make a
product clearer, and the engagement boundaries above already forbid the
dishonest forms.

## Accessibility as a quality floor

- Contrast: 4.5:1 for body text, 3:1 for large text and essential non-text UI.
- Targets: at least 44×44 points (iOS) / 48×48 dp (Android) / 24×24 CSS px
  minimum with comfortable spacing on the web; larger for primary actions.
- Focus is always visible; every control is reachable and operable by keyboard
  (or switch/screen reader on mobile) and has an accessible name.
- Motion respects reduced-motion settings; nothing flashes more than three times
  per second.
- Text scales with user settings without clipping or overlap.
