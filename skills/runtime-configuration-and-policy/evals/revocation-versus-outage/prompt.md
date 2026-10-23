---
tags: [skill-creator]
max_turns: 10
timeout_seconds: 180
allowed_tools: [Read, Glob, Grep, Skill]
---

A sample service reads protected settings from a secret manager, with an
environment fallback and a cached snapshot. The proposed implementation uses
the cached snapshot after every error or missing value. An administrator can
explicitly revoke a setting, and startup needs credentials to reach the manager.
Is this fallback sufficient? Recommend a minimal failure/adoption contract and
tests. Do not inspect or retrieve any credentials, install tools, or call services.
