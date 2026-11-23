# Perceived performance

These techniques make an app feel fast by starting work before the user waits
for it, or by never making them stare at an empty screen. They do not replace
fixing a slow request: measure the slow path first, and report it even when a
technique hides it.

Option names below were checked against upstream docs in November 2026.
Confirm them in the version the project uses before relying on them.

## Prefetch on intent

Load the data or code of a likely next screen when the user shows intent to
open it, so it is ready when they arrive.

### Intent signals, from weakest to strongest

| Signal | Lead time | Typical use |
| --- | --- | --- |
| Item scrolls into view | seconds | next page of a list, the item most users open next |
| Pointer rests on the link (about 50–200 ms) | 100–300 ms | links and rows on pointer devices |
| Keyboard focus on the link | until Enter | keyboard users; treat like hover |
| Press starts (`pointerdown`, `touchstart`) | 50–150 ms before the click completes | touch devices and the safest default |
| Step N of a flow is open | the whole step | load step N+1 while the user fills step N |

A delay before acting on hover keeps a pointer passing over a list from
firing a request for every row. Cancel or ignore the prefetch when the intent
ends before the delay.

### Good candidates

- list → detail screens the user opens often;
- primary navigation targets;
- the next step of a flow, and the result screen after a submit;
- the route's code bundle when the data is already cached.

### Never prefetch

- anything with side effects: a GET that logs out, marks as read, counts a
  view, sends an email, reserves stock, or starts a job. A known pitfall is a
  logout link that runs on hover; turn preloading off for that link;
- requests that are expensive, rate-limited, or billed per call;
- personalized or permission-sensitive data that could be cached and shown to
  the wrong user or after the session changed;
- on metered or slow connections (Save-Data or reduced data usage set), unless
  the cost is tiny;
- targets few users open: prefetching every link wastes bandwidth and server
  capacity for nothing.

### Make it correct

- Put prefetched data in the same cache the screen reads, keyed the same way,
  so navigation uses it instead of fetching again.
- Give it a freshness time; on arrival, show the cached copy and revalidate if
  it is older than that.
- Deduplicate: a second hover on the same link does not start a second request.
- Make sure prefetch requests are identifiable in logs or analytics (for
  example a header or the browser's `Sec-Purpose: prefetch`), so they are not
  counted as views.
- Respect server limits: bound how many prefetches run at once.

### Framework and platform hooks (verify in the current docs)

- **Browser, multi-page sites:** the Speculation Rules API.
  `"eagerness": "moderate"` starts on a 200 ms hover or on `pointerdown`;
  `"conservative"` starts on pointer or touch down. Chrome limits these to two
  prefetches and two prerenders at a time. Prefer prefetch over prerender
  unless the page has no side effects on load.
- **TanStack Router:** `defaultPreload: 'intent'` on the router or `preload`
  per link; `defaultPreloadDelay` (50 ms by default) and
  `defaultPreloadStaleTime` (30 s by default).
- **React Router (framework mode):** the `prefetch` prop on `Link`, with values
  such as `intent`, `render`, `viewport`, and `none`.
- **SvelteKit:** `data-sveltekit-preload-data="hover"` (falls back to tap on
  mobile) or `"tap"`; data is not preloaded when the user asked for reduced
  data usage. Use `"off"` on links with side effects.
- **Next.js, Nuxt, Astro, Remix, and others:** each has its own link
  prefetch option. Read the current docs for the default (often viewport-based
  in production) and how to switch to hover or turn it off per link.
- **Data libraries (TanStack Query, SWR, Apollo, and similar):** call the
  library's prefetch function from the intent handler, with the same query key
  as the screen.
- **Native mobile and desktop:** start the fetch on press-down or when the row
  becomes visible, keep it in the same store the next screen reads, and cancel
  it when the user scrolls away.

### Prove it

In the network or request log, show that hover or focus fetches the target
once, that navigation then renders without a new request (or with a background
revalidation), that a quick pass over a list does not fire one request per row,
and that no link with side effects was prefetched. Compare the navigation time
with and without prefetching on a throttled connection.

## Other techniques

**Stale-while-revalidate.** Show the last known data immediately and refresh in
the background; say when it was last updated if staleness matters. Never show
stale data for balances, stock, or anything the user acts on irreversibly
without revalidating first.

**Keep previous data during transitions.** When a filter, sort, or page
changes, keep the old results visible with a quiet loading cue until the new
ones arrive. Do not blank the list.

**Skeletons that match the layout.** For a known layout that takes more than
about a second, show a skeleton with the real structure. A generic skeleton
that does not match the final layout causes a jump and feels slower.

**Reserve space.** Give images, embeds, and late content their final size up
front so nothing shifts under the user's pointer.

**Optimistic updates.** Apply cheap, reversible, almost-always-successful
actions immediately (like, reorder, mark as read), send the request, and roll
back visibly with a reason if it fails. Never for payments, irreversible
deletes, or actions with external effects.

**Progressive rendering.** Render the dominant content first; load secondary
panels, recommendations, and below-the-fold sections after it. Stream
server-rendered pages when the stack supports it.

**Preload code for the next route.** Split code per route and load the next
route's code on intent, even when its data cannot be prefetched.

**Debounce search, cancel stale requests.** Wait a short pause after typing
before searching, cancel the previous request when a new one starts, and never
let an older response overwrite a newer one.

**Background work with progress.** Move work over about 10 s to a background
job with visible progress and a notification on completion, so the user can
leave the screen.
