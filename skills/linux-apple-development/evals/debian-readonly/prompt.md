---
tags: [skill-creator]
max_turns: 12
timeout_seconds: 300
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit, Bash]
---

Quero usar omarchy-apple-dev num Debian 13 x86_64 controlado por SSH do meu Mac.
Vi que Ubuntu 24.04 foi testado, então posso copiar a lista apt e o Swift dele
e dizer que Debian está suportado? Não tenho sudo. Pensei em rodar --user-only
--repair só para diagnosticar, e criar symlinks das libs que faltarem. Preciso
de um plano sem executar nada: quero compilar um app SwiftUI macOS completo,
de preferência no modo no-xcode para economizar o download.
