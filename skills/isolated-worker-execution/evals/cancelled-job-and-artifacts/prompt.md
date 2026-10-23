---
tags: [skill-creator]
max_turns: 10
timeout_seconds: 180
allowed_tools: [Read, Glob, Grep, Skill]
---

A sample plugin runner kills only the immediate child on cancellation. Detached
grandchildren may remain. The parent later copies every file from the scratch
directory, including a child-created symlink, into retained artifacts. On restart
it automatically reruns the interrupted job and replaces the previous failed
result with PASS. Recommend the smallest safe lifecycle/evidence redesign and
tests. Do not run target code, kill processes, or alter any existing artifacts.
