# Operational workflow skills: scope and evaluation

These five skills capture portable engineering procedures, not a particular
organization's architecture, operational policy, or incident history.

## Ownership and overlap

| Skill | Owns | Does not replace |
| --- | --- | --- |
| `runtime-configuration-and-policy` | Typed setting/policy authoring, revisions, publication and consumer adoption | Product decisions, credential protocols or permission to activate effects |
| `migration-parity-audit` | Current-source capability parity and explicit cutover prerequisites | General architecture, an authorized migration executor or a deployment plan |
| `backup-restore-drills` | Consistent recovery sets and isolated, observable restoration proof | Key-management policy, live restore approval or an application rollback |
| `credential-lifecycle-and-rotation` | Credential identity, custody, renewal/revocation and adoption | Provider-specific authentication documentation or generic secret handling |
| `isolated-worker-execution` | Execution authority, enforced isolation, owned process trees and safe result promotion | A security audit, queue-admission policy or general shutdown guidance |

The existing architecture, testing, secrets, asynchronous-workflow and deployment
skills remain canonical for their own responsibilities. References to them are
complementary, not duplicated policies or automatic installation dependencies.

## Scenario tests

Each skill has two tests under `skills/<name>/evals/<case>/`: `prompt.md`,
`case.yaml` (schema 1.1), and three substantive criteria under `graders/`.
All scenarios are synthetic. They require design answers, not executing a
restore, rotating a real credential, deploying, or running less-trusted code.

| Skill | Cases |
| --- | --- |
| Runtime configuration | Concurrent policy publication; revocation versus outage |
| Migration parity | Equal counts without parity; asynchronous contract change |
| Backup/restore | Successful import hiding errors; host-loss recovery set |
| Credential lifecycle | Lost refresh response; adoption after revocation |
| Isolated execution | Rootless containers without containment; cancelled jobs and artifacts |

To repeat a case, give a fresh agent only the task body from `prompt.md` and,
for the with-skill condition, the selected `SKILL.md`. Do not expose case outcomes,
graders, prior answers, or other skill files to the executor. Run a separate
baseline without the skill. Keep outputs and snapshots in an explicitly chosen
private workspace on persistent storage outside this public checkout. Use
synthetic identities and do not connect to shared or production services.

Grade the actual answer against each criterion with quoted evidence, not keyword
presence. Use an independent grader and preserve failures. A statement about a
proposed test is not evidence that it ran; a design artifact cannot independently
verify a claim that no external action occurred. The skill-creator review viewer
can show the answers and criterion results for human feedback.

## Recorded design-evaluation results

Initial evaluation used 20 separate responses: ten scenarios, each with and
without its skill. Independent grading found two with-skill omissions: a concrete
before/after no-damage oracle for restore drills, and explicit revocation-test
outcomes for credential adoption. Both skills were clarified and both of their
cases rerun with fresh paired baselines, adding eight responses. Earlier outputs
and scores were preserved rather than overwritten.

One credential criterion was clarified before the rerun to judge explicit design
oracles and recommendations, not unobserved execution. Both rerun conditions used
the same revised criterion. The other three skills retained their initial cases.

| Final selected skill version | With skill | Without skill |
| --- | --- | --- |
| `runtime-configuration-and-policy` | 6/6 | 3/6 |
| `migration-parity-audit` | 6/6 | 4/6 |
| `backup-restore-drills` | 6/6 | 4/6 |
| `credential-lifecycle-and-rotation` | 6/6 | 4/6 |
| `isolated-worker-execution` | 6/6 | 5/6 |
| **Total criteria** | **30/30** | **20/30** |

These are small, single-sample, independently judged **design checks**, not
statistically established effectiveness or implemented-system verification.
Some criteria already pass in the baseline and do not discriminate skill value.
No trigger-selection accuracy, native platform sandbox, live secret provider,
production restore, cutover, or autonomous task-completion guarantee was tested.
The harness did not expose token/timing measurements; no speed/cost comparison
is claimed, and absent metrics were not represented as measured zeros.

Raw answers, private workspace paths, task/session identifiers and detailed
grading records are deliberately not included in the public repository. This
summary contains only synthetic scenario descriptions and aggregate scores.
Human feedback on the generated review remains welcome; it is not recorded as
having happened.

## Collection and privacy checks

The local collection gate validated skill metadata, eval schemas, JSON, local
links, Python syntax, whitespace and the existing safe fixture suites. New
skill bodies, examples, test prompts and grading criteria were manually reviewed
for generalization and scanned for known private identifiers, paths, endpoints,
issue identifiers and credential patterns. A prose slash-list was identified as
a scanner false positive, not treated as leaked filesystem data.

Do not add source transcripts, private incident descriptions, organization
policies, operational topology, or source-specific defaults to make tests more
realistic. Use neutral examples instead. Automated scanning is an additional
check, not a proof that every possible identifying detail has been removed.

Creating and testing these files does not install skills, change harness
configuration, authorize operational actions, or publish a release.

## Correction, pipeline, and operations skills (2026-11-16)

Eight skills added together (`agent-correction-tree`, `pipeline-latency`,
`schema-migration-safety`, `flaky-test-diagnosis`, `local-fast-gates`,
`dependency-freshness`, `remote-host-hardening`, `postmortem`) and the new
instance-move case for `backup-restore-drills` were checked with 26 synthetic
scenarios from their `evals/`. Each scenario was answered by a fresh executor
with only the prompt and, for the with-skill condition, the selected skill
files; a separate executor answered without the skill. Executors and graders
used Claude Sonnet as subagents. Answers were relabelled A/B in random order
before grading, and three independent graders split each expected outcome into
atomic criteria and judged both answers against the same criteria with quoted
evidence.

| Skill | With skill | Without skill |
| --- | --- | --- |
| `agent-correction-tree` | 18/19 | 11/19 |
| `pipeline-latency` | 17/17 | 8/17 |
| `schema-migration-safety` | 18/18 | 13/18 |
| `flaky-test-diagnosis` | 15/15 | 14/15 |
| `local-fast-gates` | 11/11 | 9/11 |
| `dependency-freshness` | 16/16 | 10/16 |
| `remote-host-hardening` | 16/16 | 13/16 |
| `postmortem` | 8/8 | 6/8 |
| `backup-restore-drills` (instance move) | 7/7 | 7/7 |
| **Total criteria** | **126/127** | **91/127** |

The one with-skill miss (no run-time cost stated for a proposed hook) also
failed in the baseline; `agent-correction-tree` now names hook run time in the
cost it must report. That clarification was not re-run. Largest differences:
the baseline accepted a fixed runner vendor and a uniform deploy target, offered
retries, skipped a full-suite gate before PR selection, hand-wrote or edited
migrations, inherited global toolchain versions without upstream lookup, and
put personal preferences into shared repository rules.

Same limits as above: single samples, criteria written by the skill author,
graders from the same model family, design answers rather than executed work,
and no trigger-selection or timing/cost measurement. The `flaky-test-diagnosis`,
`postmortem/2`, and `backup-restore-drills` cases barely discriminate and should
be made harder. Raw answers and per-criterion grades stay outside this
repository.

### SRE and design review skills (2026-11-16)

Same method, nine scenarios, blinded single grader:

| Skill | With skill | Without skill |
| --- | --- | --- |
| `slo-and-alerting` | 15/15 | 14/15 |
| `incident-response` | 19/19 | 18/19 |
| `technical-design-review` | 18/18 | 16/18 |
| **Total criteria** | **52/52** | **48/52** |

The baseline was already strong on these topics, so these scenarios
discriminate little. Differences: the baseline set an SLO from stakeholder
agreement rather than a measured baseline, proposed a production rollback (and,
outside the criteria, a credential revocation) without an explicit approval
gate, and listed design concerns without separating blocking issues from
suggestions or naming one-way doors. Harder scenarios (ambiguous ownership,
pressure to skip approval, designs with subtle data-migration traps) are needed
before claiming a material effect.

### Previously unevaluated skills and harder scenarios (2026-11-16)

The ten skills that had no evals received two or three scenarios each, and the
six skills whose earlier cases barely discriminated received one harder case
(pressure to skip a step or a subtle trap). Same method: Sonnet executors, one
with-skill executor per skill, grouped baseline executors, A/B relabelling,
three blinded graders.

| Skill | With skill | Without skill |
| --- | --- | --- |
| `followable-guides` | 11/11 | 2/11 |
| `vault-bootstrap-configuration` | 13/13 | 5/13 |
| `single-state-enum` | 11/11 | 6/11 |
| `insert-only-predeploy-import` | 11/11 | 6/11 |
| `actions-billing-local-validation` | 12/12 | 8/12 |
| `opencode-session-inventory` | 12/12 | 9/12 |
| `engineering-comment-scenarios` | 10/11 | 7/11 |
| `vault-namespace-ownership` | 10/10 | 9/10 |
| `jira-issue-writing` | 11/11 | 10/11 |
| `comment-writing` | 7/8 | 7/8 |
| `flaky-test-diagnosis` (harder case) | 4/4 | 2/4 |
| `postmortem` (harder case) | 5/5 | 4/5 |
| `incident-response` (harder case) | 4/5 | 5/5 |
| `slo-and-alerting` (harder case) | 4/4 | 4/4 |
| `technical-design-review` (harder case) | 5/5 | 5/5 |
| `backup-restore-drills` (harder case) | 5/5 | 5/5 |
| **Total criteria** | **135/138** | **94/138** |

With-skill misses led to two clarifications, not re-run: `incident-response`
asked for approval at every step after an explicit blanket authorization (it
now treats such authorization as covering reversible mitigations only), and
`comment-writing` led an outage update with the cause (it now leads incident
updates with impact and status and labels unconfirmed causes). The third miss,
not acknowledging that an audit finding was valid, failed in both conditions.
Notable baseline failures: copying `.env` values into Vault with secrets on the
command line, offering an empty commit to retry billing-blocked CI, skipping
related records in an import, modelling a wizard with a step index and separate
state, and accepting a longer sleep as a flaky-test fix.

The harder SLO, design-review, and restore cases still did not discriminate:
the baseline already handles low-traffic alerting, destructive currency
backfills, and refusing to restore over live data. Same limits as above.

## Skill triggering (2026-11-16)

Earlier rounds handed each skill to the executor, so they measured behaviour
after loading, not whether an agent picks the skill on its own. A triggering
check gave 14 fresh Sonnet subagents a realistic request in Portuguese that
named no skill, inside a disposable Go repository, and read each transcript for
`Skill` tool calls.

- **Before** (about 150 installed skills, descriptions averaging ~400
  characters): the listing showed descriptions for only 58 of 151 skills; most
  new skills appeared as bare names. That run also framed requests as a
  "simulation", which suppressed tool use, so it loaded no skill at all and is
  not a valid baseline.
- **After** removing unused global skills (115 left) and shortening this
  repository's descriptions to ~190 characters: 104 of 115 skills listed with
  descriptions, and 12 of 14 requests loaded the expected skill. The misses: a
  slow-endpoint request loaded the third-party `diagnose` instead of
  `performance-optimization` (overlapping scope), and "is this ready to
  commit?" loaded nothing (the agent ran lint and tests anyway). Both
  descriptions were sharpened afterwards. On a re-run (with a
  real uncommitted change for the commit case), the slow-endpoint request
  loaded `performance-optimization`; the commit request still loaded no skill,
  though the agent ran format, lint, and tests and flagged the missing test.
  Final count: 13 of 14.

`validate_repo.py` now rejects descriptions over 260 characters so the
listing budget stays usable. One sample per request; the result depends on
which other skills a user has installed.
