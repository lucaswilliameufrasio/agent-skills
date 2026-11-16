---
type: llm
focus: trace
weight: 1
---

The response checks whether the snapshot format can be restored on the newer
major version (preferring a logical dump or the engine's supported upgrade path
when it cannot) and accounts for roles, grants, extensions, and sequences that
may not travel with the data.
