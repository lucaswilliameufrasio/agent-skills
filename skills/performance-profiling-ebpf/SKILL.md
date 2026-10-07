---
name: performance-profiling-ebpf
description: >-
  Diagnose a measured performance bottleneck with runtime profilers, operating
  system tools, perf, or eBPF/bpftrace. Use when CPU, scheduling, syscall,
  allocation, lock, or kernel-level behavior needs profiling, or when validating
  whether eBPF/perf tooling is available. Reproduce the workload first, treat
  eBPF as optional and Linux-specific, and do not change privileges or kernel
  settings automatically.
---

# Runtime profiling and optional eBPF

Profiling explains behavior under a specific workload; it does not replace
reproduction or prove a performance improvement. Start from a measured symptom,
profile the relevant process while representative load is active, then validate
any code change with the same benchmark.

## Select the least invasive useful profiler

Inspect runtime, build symbols, existing observability, and the measured symptom.
Choose application/runtime profiling (for example Go pprof, Rust samply/perf,
Node CPU profiles, or a BEAM-appropriate profiler) before kernel profiling when
it can answer the question. Consider CPU, allocation/heap, lock/block, scheduler,
syscall, and I/O views based on evidence; do not collect every profile by
default. Keep debug symbols and build flags comparable across candidates.

Correlate profile windows with the exact workload, commit, duration, and
environment. Check overhead and profile the service rather than accidentally
profiling the load generator or fixture. A synthetic CPU endpoint can validate
capture mechanics, but is not evidence about a real product workload.

## eBPF/perf readiness and permissions

eBPF is optional and Linux-specific. Before attempting capture, check only the
necessary readiness facts: OS/kernel support, relevant BTF/perf availability,
tool/version, target process visibility, and permission status. Report
`unsupported`, `tool missing`, `permission denied`, `timed out`, or `ready`
separately; readiness is not proof that a useful profile was captured.

Never automatically run privileged commands, change `perf_event_paranoid` or
other sysctls, add capabilities, disable seccomp, or expose profiler endpoints.
If elevated privileges are necessary, explain the exact command, target, scope,
duration, and risk, then ask the user before running it. Scope capture to the
intended process and stop it after a bounded interval. Do not profile unrelated
processes on a shared host.

## Protect profile data

Raw pprof, cpuprofile, stacks, and flamegraphs can contain executable names,
symbols, local paths, and workload details. Store raw artifacts in an ignored,
access-controlled location; do not attach or commit them automatically. Prefer
sanitized summaries of tool/version, mode, duration, top symbols/percentages,
and readiness status. Review before sharing, and never persist arbitrary
environment dumps, full command lines, secrets, or unrelated host details.

## Interpret and fall back

Compare profiles only when workload, machine/architecture, runtime, build flags,
and capture duration are sufficiently similar. Missing symbols or denied
`perf_event` access do not mean the code is cheap. If eBPF is unavailable, use
the runtime profiler, sampled process CPU/RSS, traces, or an isolated
microbenchmark. State limitations and do not weaken host security to make a
profile work.

Use `performance-benchmarking-and-load-testing` to establish reproducible load
and `performance-optimization` to validate improvements against the original
objective.
