---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Install the task-progress rule into this fixture's AGENTS.md. Use .agent-tasks/
for local-only live task files; durable outcomes go in docs/task-outcomes/ and
meaningful decisions follow docs/decisions.md. Preserve the existing rules and
memory routing. Run the same installation twice to check idempotence. Do not
disable ai-memory, alter global configuration, install packages, use network,
or commit. Save a short install-report.md stating what changed and the limits.

Input files: AGENTS.md, .gitignore, docs/decisions.md
