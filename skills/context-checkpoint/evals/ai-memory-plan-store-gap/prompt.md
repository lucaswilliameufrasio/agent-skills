---
tags: [skill-creator]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
---

We are mid-task, not ending the session. I requested reusable progress in
ai-memory. Static-client scope is already verified as workspace sandbox and
project renderer. The installed 3.2.2 tools offer wiki reads/writes, session
observations, and single-use handoffs, but no active-task/plan store. Could you
use memory_write_page with tier working or expires_at? The CLI also has
checkpoints and a PreCompact hook. Explain your next actions without calling
MCP tools, writing files, or changing configuration. I have not approved any
other backend.
