---
name: system-module-architecture
description: >-
  Design or review modular architecture across web, mobile, API, and operations.
  Use before creating or refactoring modules, routes, screens, workflows, or
  service boundaries. Define capability ownership, contracts, state, permissions,
  and failure behavior instead of organizing a system only by framework files.
---

# System module architecture

Organize systems around coherent capabilities and user/operator journeys, not
only around pages, route folders, components, or service names. Respect existing
domain language and architecture decisions; this skill does not replace them.

## Module boundaries

A module owns a cohesive capability and should make its key responsibilities
discoverable:

- domain entities and lifecycle;
- commands and queries;
- states and transitions;
- authorization and ownership;
- dependencies and external contracts;
- failure modes, retries, and side effects.

A module may have multiple screens or endpoints when they serve the same
capability. Each route, screen, or operation should still have one primary
intent. Do not treat a folder or a large component as a domain boundary by
itself.

## Separate journeys by intent and risk

Use distinct flows when user intent, permission, risk, frequency, or completion
state differs. Typical examples include:

- overview/status versus search and collection management;
- read-only inspection versus creation/editing;
- routine operations versus configuration/policy changes;
- reversible actions versus destructive or irreversible actions;
- short interactions versus long-running work and progress;
- operational activity versus audit, diagnostics, and support.

Do not place destructive maintenance beside routine actions or bury important
configuration inside an unrelated operational screen. Do not solve a wrong
journey topology merely by extracting more components.

## Contracts and integrations

- Model APIs as named domain commands and queries, not generic forwarding
  proxies for arbitrary methods, paths, headers, or request bodies.
- Give each integration a named client and explicit operations, typed request
  and response models, validation, authorization, timeout, and safe error
  mapping.
- Parse external data at the boundary and map it into domain types before it
  enters business logic.
- Load configuration through named, typed contracts rather than arbitrary
  runtime key lookup.
- Validate long-running or destructive commands with authorization,
  idempotency where appropriate, explicit confirmation, and progress/final
  state.

## Review checklist

- Can each module be described as one coherent capability?
- Is ownership of state, permissions, and failure behavior clear?
- Does every route or screen have one primary intent?
- Are configuration, maintenance, and destructive actions separated from
  routine operation?
- Are integrations explicit and validated at their boundaries?
- Can a new contributor locate the contract and the source of truth for state?
