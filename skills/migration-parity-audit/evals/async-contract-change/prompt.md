---
tags: [skill-creator]
max_turns: 10
timeout_seconds: 180
allowed_tools: [Read, Glob, Grep, Skill]
---

We are rewriting a sample document-processing API. The legacy POST returns 201
only after processing finishes; the replacement returns 202 after inserting a
job. The web client still treats any successful response as a completed result.
The new route test passes. Can we mark this operation parity-verified? Explain
the missing contract, local evidence, and the distinction between a deliberate
change and parity. Do not contact a provider or activate the new implementation.
