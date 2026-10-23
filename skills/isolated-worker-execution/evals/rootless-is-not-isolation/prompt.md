---
tags: [skill-creator]
max_turns: 10
timeout_seconds: 180
allowed_tools: [Read, Glob, Grep, Skill]
---

We are designing a runner for less-trusted sample repository builds. It uses
rootless containers and a command timeout, but inherits the supervisor's full
environment, mounts its home directory, and retains external network access.
The submitted job can request additional capabilities. Is the execution boundary
ready? Propose enforcement and harmless qualification checks. Do not execute a
build, change host privileges, install a sandbox, or contact external services.
