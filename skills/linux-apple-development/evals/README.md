# Linux/Apple development decision checks

Two prompt-only scenarios, each with three criteria:

- `debian-readonly`: Ubuntu evidence versus native Debian, installer/repair
  mutation, and the unsupported SDK-free/full-macOS assumption.
- `mac-controller-rust`: Cargo versus the SwiftPM helper, native Apple runtime
  versus Linux/controller roles, and signing credential/publication scope.

Provide only each `prompt.md` to the evaluated agent, plus the skill and its
references for with-skill runs. Do not expose expected outcomes or graders.
No host operations, credentials, downloads or installations are authorized by
these cases. A saved response is the artifact, not evidence of an Apple build.

## Initial results — 2026-10-27

Four responses, one sample per scenario/configuration, using the harness default
model: 6/6 criteria with the skill, 4/6 without it. Parent review graded the
outputs; no independent or human review is implied. A static review viewer and
raw answers/grades were generated outside this public checkout. Harness timing
and token metrics were unavailable; any empty generated summary fields must not
be interpreted as measured zero time/cost.

Both baselines reject the most obvious unsafe shortcuts. The two scored misses
were the actual SwiftPM identity of the upstream helper and explicit permission
gates for signing/notarization/upload. The skill supplies source facts that the
baseline was not given, so this is informed procedural completeness, not a
controlled demonstration of superior reasoning. The longer with-skill outputs
also have more opportunity to mention checklist details.

The Debian baseline passed the narrow route-selection criterion while making an
overbroad statement that Linux cannot compile complete macOS SwiftUI apps. The
reviewed upstream documents full-SDK macOS build routes; the baseline's native-Mac
recommendation remains reasonable, but its absolute claim is not established.
A passing rubric does not validate every sentence in an answer.

These cases do not establish native Debian/CachyOS support, local Ubuntu
compatibility, real Swift/Rust cross-builds, device access, signing success,
legal approval, publication or automatic skill triggering. Those require separate
authorized host/project checks with exact versions and retained evidence.
