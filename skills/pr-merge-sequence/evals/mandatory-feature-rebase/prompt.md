---
tags: [skill-creator]
max_turns: 12
timeout_seconds: 180
allowed_tools: [Read, Write]
---

Explain the steps before merging a feature PR into develop. The feature branch
appears current, the checkout is clean, and origin/develop is the base upstream.
Merge, rebase, and any necessary push are authorized. What if develop moves
again before the merge, or if the rebase encounters a conflict? Do not execute
commands or merge anything.
