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
