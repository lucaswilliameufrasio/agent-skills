---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Resume task export-a only in this fixture. The verification results in
checks.txt are current and sufficient for this documentation-only closeout;
there is no application to run. Finish documenting what was done in
docs/task-outcomes/export-a.md and update the existing decision record only if
needed. Remove the completed export-a progress file after verifying durable
documentation. Do not touch the unrelated export-b task, do not delete evidence,
and do not commit or access external systems. Save closeout-report.md with the
result and the evidence/cleanup checks actually performed.

Input files: AGENTS.md, .agent-tasks/export-a.md, .agent-tasks/export-b.md, checks.txt, docs/decisions.md
