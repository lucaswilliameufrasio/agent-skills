---
tags: [skill-creator]
max_turns: 10
timeout_seconds: 180
allowed_tools: [Read, Glob, Grep, Skill]
---

After a suspected compromise, an operator revoked a sample service credential
and stored a replacement. Existing connection pools still hold the old value.
An administrator sees a successful secret-store receipt and suggests declaring
rotation complete, with automatic restoration of the old credential if a client
fails. Assess that proposal and design the adoption/reconciliation checks.
Do not read values, rotate anything, restart services, or reactivate credentials.
