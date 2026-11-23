# Screen state matrix

Fill one matrix per screen and per shared component that shows data. Every row
ends as **designed** (with the capture), **not applicable** (with the reason),
or **pending**. A row is designed only after it was rendered with a fixture or
real data and looked at. This matrix is shared by every design skill in this
collection.

```markdown
## <Screen or component> — state matrix

| Group | State | What the user sees | Primary action | Status | Evidence |
| --- | --- | --- | --- | --- | --- |
| Amount | First use, nothing yet | | | | |
| Amount | No results for search or filter | | | | |
| Amount | All done or all cleared | | | | |
| Amount | Exactly one item | | | | |
| Amount | A few items | | | | |
| Amount | Many items, paged or virtualized | | | | |
| Amount | More than the layout was drawn for | | | | |
| Content | Long text (names, titles, numbers) | | | | |
| Content | Optional fields missing | | | | |
| Content | Image or media missing | | | | |
| Content | Other languages, large text setting | | | | |
| Time | First load | | | | |
| Time | Reload or refresh over existing data | | | | |
| Time | Saving or submitting | | | | |
| Time | Slow (over a few seconds) | | | | |
| Time | Offline or connection lost | | | | |
| Time | Data changed elsewhere or stale | | | | |
| Failure | Recoverable error, with retry | | | | |
| Failure | Fatal or not-found error | | | | |
| Failure | Validation error | | | | |
| Failure | Partial success in a batch | | | | |
| Access | No permission | | | | |
| Access | Read-only | | | | |
| Access | Signed out or session expired | | | | |
| Done | Success or completion | | | | |
```

## What each group must answer

**Amount.** The layout drawn for "a comfortable number of items" usually breaks
at both ends.

- *First use* explains what this place is for and offers the action that fills
  it (create, import, connect). It is not a blank table with headers.
- *No results* repeats what was searched or filtered and offers to clear or
  change it. It never suggests creating data the user was only searching for.
- *All done* (inbox zero, all tasks finished) is a reward, not an error.
- *Exactly one* checks grammar ("1 item"), grids that look broken with one
  card, and bulk actions or "select all" that make no sense for one.
- *Many* decides paging, infinite scroll with an end, or virtualization;
  keeps headers and actions reachable; and states the total when it is known.
- *Overflow* checks the extra tab, chip, column, or badge count ("99+") that
  the layout did not plan for.

**Content.** Real data is longer, emptier, and stranger than sample data.
Decide truncation (with the full text available), wrapping, and what replaces
a missing field or image. Missing is not zero: show "not set", not "0".

**Time.** Each moment the user waits has its own look. First load can use a
skeleton of the real layout; a refresh keeps existing content and shows a quiet
indicator; saving keeps the form on screen and prevents double submission;
offline says what still works and queues or blocks writes explicitly; stale
data says when it was last updated.

**Failure.** Say what happened, what still holds (is the data saved?), and what
to do next, next to the cause. A recoverable error offers retry and keeps the
user's input. A fatal error offers a way out (back, home, support). In a batch,
say which items succeeded and which failed, and let the user retry only the
failed ones.

**Access.** Hide what the user can never do; explain what they cannot do yet
and how to get it. Read-only shows the data without dead controls. An expired
session keeps the user's unsaved work and returns them to the same place after
sign-in.

**Done.** The finished job has its own state: what was done, where the result
is, and the next useful action.

## Fixtures

Build one fixture per row (empty list, single item, long-text item, 500 items,
failing request, permission-denied user) in the project's test or story setup.
Mark fixtures as fixtures; never ship them as real content. Capture each row at
the sizes the project's design system names.

## Components

A component's matrix is smaller but has the same idea: default, hover, focus,
pressed, selected, disabled (with the reason shown), loading, empty, error,
read-only, and long or missing content inside it.
