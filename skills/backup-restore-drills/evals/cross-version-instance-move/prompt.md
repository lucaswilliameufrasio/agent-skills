---
tags: [skill-creator]
max_turns: 10
timeout_seconds: 180
allowed_tools: [Read, Glob, Grep, Skill]
---

We want to move our application database from an old instance to a new one
running the next major version of the same engine. The plan is to take last
night's snapshot, restore it on the new instance, and point the app at it.
What is missing from this plan? Give a plan only; do not connect to any
database, download backups, or create infrastructure.
