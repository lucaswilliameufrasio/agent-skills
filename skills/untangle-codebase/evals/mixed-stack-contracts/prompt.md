---
tags: [skill-creator]
max_turns: 12
timeout_seconds: 180
allowed_tools: [Read, Write]
---

Audit only; don't edit anything. Our repo has a Rust native library exposed to a
Python worker through a C ABI and a Kotlin Android client consuming its events.
Cargo.lock resolves a transport crate to 0.9, although latest docs describe 2.x.
The worker and client copy event names and retry constants. The worker's retry
limit differs intentionally because it owns durable delivery. Old stored events
need a version-specific decoder. CI checks Rust, Python, and Android separately.
How would you untangle this? Give a concrete investigation and verification plan
without assuming the duplicated constants should all become one shared package.
