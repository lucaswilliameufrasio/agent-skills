# Design system record (template)

Adapt headings and language to the repository. Keep it short enough that an
agent reads it fully before every interface task.

```markdown
# Design system

Source of truth for interface work. Every visual decision traces to a token
below or to a reference on the board. Anything else is a default and is removed.

## Reference board
| Ref | Source | Role | Consulted |
| --- | --- | --- | --- |
| A | <link or file> | <what we take from it> | YYYY-MM-DD |

Conflicts resolved: <trait> — followed <ref> because <role/decision>.

## Identity layer
Moves that come from the product, not from a reference.
| Move | Source in the product | Job | Where it may appear |
| --- | --- | --- | --- |
| <e.g. ink underline on current place> | <name / domain / voice> | <marks current place> | <nav, tabs; max one per region> |

## Tokens
Implemented in: <path to CSS variables / theme config>

| Token | Value | From | Notes |
| --- | --- | --- | --- |
| color.bg | | A | |
| color.identity | | identity | |
| color.text | | A | contrast vs bg: x:1 |
| space.unit | | B | |
| radius.control | | B | |
| font.body | | B | size/line-height/weight |

## Components
### <Component>
- Anatomy:
- Variants and sizes:
- States: default, hover, focus, pressed, disabled, loading, error, empty
- From: <ref>

## Rules
MUST
1. <signature move, stated so a reviewer can check it>

MUST NOT
1. <observed default or slop pattern that no reference shows>

## Surfaces
| Surface | Carries over | Adapts |
| --- | --- | --- |
| web app | | |
| back office | | |
| mobile | | |

## Accessibility deviations from references
- <what changed, why, by how much>

## Review checklist
- [ ] Every color, size, radius, and shadow comes from a token.
- [ ] Signature and identity moves are present, each doing its job.
- [ ] No MUST NOT pattern appears.
- [ ] Compared side by side with the relevant reference at the same viewport.
- [ ] Contrast, focus, labels, targets, and reduced motion checked.

## Change log
- YYYY-MM-DD: <change and reason>
```
