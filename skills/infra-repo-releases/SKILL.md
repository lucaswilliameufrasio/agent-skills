---
name: infra-repo-releases
description: >-
  Release an app by changing an image tag in a separate infrastructure repository
  through a reviewed pull request, or decide when a direct deploy API is
  acceptable. Use to set up or run releases, write a ship command, or plan deploy
  audit and alerts.
---

# Releases through an infrastructure repository

The application repository builds an image; a separate infrastructure repository
holds the deployment manifest that names which image runs. A release is a pull
request in the infrastructure repository that changes one line: the image tag.
The deploy platform watches that repository and redeploys when the manifest on
its default branch changes.

Prefer this over calling the platform's deploy API directly. The git history of
the infrastructure repository becomes the deploy record: who released, what
changed, who approved, and how to roll back, all without a deploy token on a
laptop or in CI.

## Invariants

1. **The tag is the commit.** Tag images with the first 12 characters of the
   application commit on the default branch. Never deploy `latest` or any
   moving tag; a moving tag makes the manifest lie about what runs.
2. **Build once, promote the tag.** Build for the production architecture, push,
   and confirm the registry has the tag before touching the manifest. Do not
   rebuild an existing tag.
3. **One line per release.** The release diff changes only the image tag line.
   Stop if the edit would touch anything else; configuration changes get their
   own reviewed pull request.
4. **Release from the default branch only.** The local default branch must be
   clean and equal to its remote. Never release a feature branch.
5. **The running service reports its revision.** Bake the tag into the image
   at build time and return it from a cheap health endpoint, for example
   `{"status":"ok","revision":"<tag>"}`. Without it nobody can tell whether a
   release is live, and the release command cannot verify itself.
6. **Done means observed.** A release is finished when production reports the
   new revision and the readiness check passes, not when the merge succeeds.
7. **Rollback is a release.** Roll back with the same one-line pull request
   naming the previous tag (find it in the manifest's history). Check first
   that database migrations of the newer version still work with the older
   code; migrations normally only move forward.

## The ship command

Give each application one command that runs the whole release so people do not
improvise it. It must:

1. Check tools, the clean and up-to-date default branch, and a clean
   infrastructure checkout on its default branch (pull it).
2. Print the plan (commit, image, old tag to new tag, production URL) and stop
   there with `--dry-run`.
3. Build with the platform flag, the source and revision labels and the
   revision build argument; push; verify the tag exists in the registry. Skip
   the build when the tag already exists.
4. Create a release branch in the infrastructure repository, change the tag
   line, verify the diff is exactly one line, commit, push, open the pull
   request, follow the repository's merge rules (for example rebase before a
   normal merge), and return to the default branch.
5. Poll the health endpoint until it reports the new revision (with a timeout
   and a pointer to the platform's release page), then check readiness.

See [references/ship-example.mjs](references/ship-example.mjs) for a
dependency-free Node implementation to adapt (constants at the top).

Merging a release pull request ships to production: an agent runs the command
or merges the pull request only when the user asked for that release.

## Direct deploy API: when and what it requires

Calling the platform's deploy endpoint with a token (or the CI job's short-lived
identity) is acceptable for previews, internal tools, or services that need
deploys faster than review allows. It moves the evidence out of git, so it is
only acceptable when the platform provides all of the following:

- **Identity per actor.** Prefer short-lived CI identity tokens (OIDC) bound to
  repository, ref and environment. A shared static token records "the token",
  not the person; if one is unavoidable, issue one per person or per pipeline,
  name it after its owner, give it an expiry, and store it outside shell
  history.
- **Narrow permission.** The platform only accepts images or refs that match a
  configured pattern for that service, so a leaked token cannot ship an
  arbitrary image.
- **An audit record for every deploy** with actor, credential, service, image
  or commit, time, and result, kept and reviewable.
- **Alerts** for failed deploys and automatic rollbacks, and a notice for
  successful production deploys, delivered to a channel someone reads.

## Audit and alerts are required either way

The repository approach makes the record visible, but the platform still has to
connect a merged commit to what happened:

- Record each manifest application with the infrastructure commit, its author
  and a summary of the change; record rejections too.
- Alert on failed deploys, automatic rollbacks and manifest applications that
  were blocked; announce successful production releases.
- Protect the infrastructure repository's default branch (reviews, no force
  push) and limit who can merge: merge rights are deploy rights.
- Keep the platform's read access to the infrastructure repository read-only.

## Checklist for a new application

- [ ] Infrastructure repository with the manifest; platform reads it from the
      default branch.
- [ ] Health endpoint returns the revision; image build takes it as an argument.
- [ ] Ship command with dry run, one-line diff guard and live verification.
- [ ] Runbook in the infrastructure repository: release, rollback, first install.
- [ ] Platform audit for manifest applications and alerts configured.
- [ ] Branch protection and merge permissions reviewed.
