---
name: explicit-code-style
description: >-
  Apply Lucas's cross-project readability rules when writing or reviewing code:
  use multiline braced conditionals, avoid callback-based forEach loops, and
  avoid null as an absence value in TypeScript/JavaScript. Use whenever editing,
  reviewing, or refactoring application code; respect stricter repository rules
  and language-specific constraints.
---

# Explicit code style

Prefer code whose control flow and absence semantics are visible at a glance.
Apply these conventions across projects, while treating the current repository's
`AGENTS.md`, language rules, public API contracts, and tool-enforced standards as
the final authority when they add constraints or define a necessary exception.

## Multiline conditionals

Write `if` statements with braces and a multiline body. Avoid single-line
conditionals, even when the body is short. This keeps future edits safe and makes
branches easy to scan.

```ts
if (!user) {
  return;
}
```

Avoid:

```ts
if (!user) return;
```

Apply the equivalent block form in languages with different syntax. Do not
rewrite a language construct into invalid or less safe syntax merely to imitate
the TypeScript example.

## Explicit iteration

Avoid callback-style `.forEach(...)` and iterator `.for_each(...)` for control
flow. Prefer an explicit `for`, `for...of`, or language-equivalent loop so that
`break`, `continue`, `return`, and error propagation have clear semantics.

```ts
for (const item of items) {
  process(item);
}
```

Use transformations such as `map`, `filter`, or `reduce` when they express a
value transformation clearly; this rule is about callback iteration, not a ban
on functional operations generally.

## Absence values in TypeScript and JavaScript

In TypeScript/JavaScript codebases using the no-`null` convention, represent an
absent optional value with `undefined` or an optional field rather than `null`.
Convert database `NULL` at the persistence boundary. Keep external API and
library contracts accurate: normalize `null` at the adapter boundary when
needed instead of lying about the wire format or silently changing semantics.

```ts
let timeout: ReturnType<typeof setTimeout> | undefined;
type Profile = { nickname?: string };
```

Do not apply JavaScript's `undefined` rule literally to other languages. Use
their explicit optional-value type or idiom (for example, `Option<T>` in Rust),
and follow the repository's declared policy for nullable values.

## Review checklist

- Are conditionals braced and multiline?
- Is callback-style `forEach` used where an explicit loop would clarify control
  flow?
- In a no-`null` TypeScript/JavaScript codebase, is absence represented with
  `undefined`/optional fields and normalized at boundaries?
- Did the change preserve language, API, and repository-specific contracts?
