---
type: llm
focus: trace
weight: 1
---

The response updates and verifies local develop with git pull --rebase before explicitly rebasing the feature branch even when it appears current, then validates the resulting head before merge.
