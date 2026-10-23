---
tags: [skill-creator]
max_turns: 10
timeout_seconds: 180
allowed_tools: [Read, Glob, Grep, Skill]
---

We are designing a settings editor for a sample subscription service. Product
owners have not chosen policy values yet. Two administrators can edit at once.
An operation may start before a policy publication and retry after it. The
current loader replaces an in-memory settings object, but existing client pools
keep their original options. What can we implement now, what needs decisions,
and how should we qualify completion? Give a concise design, not code. Do not
change configuration, contact services, or invent commercial values.
