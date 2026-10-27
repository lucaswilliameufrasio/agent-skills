# Desktop QA decision scenarios

Each case uses `prompt.md`, `case.yaml` and three trace graders. Give an evaluated
agent only the prompt, not the case outcome or graders. For with-skill runs, also
provide `SKILL.md` and its references. For a baseline, do not provide the skill.
These are decision-only prompts: do not install tools, change app code, control
real desktops or use actual databases while answering them.

Compare answers and grade every clause in each assertion. These checks cover:

- `ssh-egui`: missing image inspection, wgpu/glow coverage and safe fixture/storage.
- `gpui-display-failure`: graphics readiness, shared-session approval and DPI evidence.
- `slint-version-gate`: version checks, privileged endpoint exposure and native coverage.

## Initial evaluation (2026-10-27)

Three paired runs using the harness default model, one sample per configuration:
9/9 criteria with the skill and 5/9 without it. Parent review graded the responses;
no independent grader or human design review is implied. Metrics for tokens and
duration were not returned by the harness and are unavailable.

Both configurations caught the principal unsafe shortcuts. Baseline misses were
specific omissions in compound criteria: isolated application storage, the pinned
GPUI revision, explicit inspected frames/scale mapping, and keeping Slint control
out of production builds. These outcomes suggest better procedural completeness,
not a demonstrated general quality advantage. Longer answers have more room to
mention checklist items. The tests do not measure aesthetic judgment, actual
rendering, tool execution or automatic skill activation.

Artifact saving initially failed because the temporary filesystem was full.
The agents resumed only to save their original responses on persistent storage;
no app operations or cleanup of unrelated files were performed. Raw responses,
grades, aggregate benchmark and static review viewer remain outside this public
checkout. Missing timing fields in generated benchmark summaries are not zero
cost or zero runtime measurements.

## Next verification layer

A real environment pass must separately prove a newly built native app window,
actual screenshot inspection, targeted interaction, a state assertion and owned
resource teardown. Run that in an authorized app checkout with synthetic data;
do not infer it from these scenario scores. Visual acceptance also needs review
of the actual before/after images.
