---
tags: [skill-creator]
max_turns: 12
timeout_seconds: 180
allowed_tools: [Read, Write]
---

I want to untangle our C# service and its PowerShell packaging scripts. An import
scan found zero references to the AuditBridge NuGet package, so it looks dead.
But deployment config names an AuditBridge type loaded through reflection and
an optional Windows build copies its native DLL. The generated dependency file
also lists it. A wrapper around it checks access and adds audit records. Can we
remove the package and wrapper? Explain your decision and safe next steps based
only on these facts; don't install, upgrade, or run anything.
