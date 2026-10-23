---
tags: [skill-creator]
max_turns: 10
timeout_seconds: 180
allowed_tools: [Read, Glob, Grep, Skill]
---

A sample headless worker uses an external identity provider with rotating
refresh credentials. The provider may have accepted a renewal whose response
was lost; its retry/grace behavior has not been checked. The desktop keyring is
unavailable, so someone proposes saving plaintext or encrypting with a key stored
beside the file. Recommend a safe renewal/custody approach and qualification
plan. Do not fetch tokens, call the provider, install a keyring, or invent a
provider protocol.
