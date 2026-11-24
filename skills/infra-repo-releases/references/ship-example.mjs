#!/usr/bin/env node
// Reference ship command for releases through an infrastructure repository
// (skill infra-repo-releases). Copy into the application repository as scripts/ship.mjs and
// adapt the constants below. No dependencies beyond Node, git, gh and docker.
//
//   node scripts/ship.mjs              release the default branch and wait until it is live
//   node scripts/ship.mjs --dry-run    check and print the plan only
//   node scripts/ship.mjs --no-deploy  build and push the image only
//
// The image build must accept the revision (Dockerfile: ARG APP_REVISION, baked into the binary)
// and the service must return it from the health endpoint: {"status":"ok","revision":"<tag>"}.
import { execFileSync } from 'node:child_process';
import { existsSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, join, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

const ROOT = resolve(dirname(fileURLToPath(import.meta.url)), '..');
// ---- Adapt these ----
const DEFAULT_BRANCH = 'main';
const INFRA = resolve(process.env.INFRA_DIR || join(ROOT, '..', 'api-infra'));
const MANIFEST_PATH = 'production/manifest.toml'; // relative to the infrastructure repository
const MANIFEST = join(INFRA, MANIFEST_PATH);
const IMAGE_REPO = 'ghcr.io/acme/api';
const SOURCE_REPO = 'https://github.com/acme/api';
const PLATFORM = 'linux/amd64';
const RELEASES_PAGE = 'the deploy platform (project → releases)';
const REVISION_BUILD_ARG = 'APP_REVISION';
// The one line that names the image tag, and how to write it back.
const TAG_LINE = /IMAGE_TAG = "([^"]*)"/;
const tagLine = (tag) => `IMAGE_TAG = "${tag}"`;
// Production base URL (health and readiness endpoints live under it).
const PUBLIC_URL = process.env.PUBLIC_URL || 'https://api.example.com';
const HEALTH_PATH = '/healthz';
const READY_PATH = '/readyz';
// ---- End of settings ----

const args = new Set(process.argv.slice(2));
const dryRun = args.has('--dry-run');
const noDeploy = args.has('--no-deploy');
for (const a of args) {
	if (!['--dry-run', '--no-deploy'].includes(a)) fail(`Unknown option: ${a}`);
}

function fail(message) {
	console.error(`\n✗ ${message}`);
	process.exit(1);
}

function run(cmd, cmdArgs, cwd = ROOT) {
	execFileSync(cmd, cmdArgs, { cwd, stdio: 'inherit' });
}

function capture(cmd, cmdArgs, cwd = ROOT) {
	return execFileSync(cmd, cmdArgs, { cwd, encoding: 'utf8', stdio: ['ignore', 'pipe', 'pipe'] }).trim();
}

function succeeds(cmd, cmdArgs, cwd = ROOT) {
	try {
		execFileSync(cmd, cmdArgs, { cwd, stdio: 'ignore' });
		return true;
	} catch {
		return false;
	}
}

function step(n, total, text) {
	console.log(`\n==> [${n}/${total}] ${text}`);
}

const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

// ---------- Checks ----------

for (const tool of ['git', 'gh', 'docker']) {
	if (!succeeds(tool, ['--version'])) fail(`${tool} not found in PATH.`);
}

const branch = capture('git', ['rev-parse', '--abbrev-ref', 'HEAD']);
if (branch !== DEFAULT_BRANCH) fail(`Release from ${DEFAULT_BRANCH} (you are on ${branch}). Merge the pull request first.`);
if (capture('git', ['status', '--porcelain'])) fail('The repository has uncommitted changes.');
run('git', ['fetch', '--quiet', 'origin', DEFAULT_BRANCH]);
const head = capture('git', ['rev-parse', 'HEAD']);
const remoteHead = capture('git', ['rev-parse', `origin/${DEFAULT_BRANCH}`]);
if (head !== remoteHead) fail('The local default branch differs from its remote. Pull with rebase, or send your commits through a pull request.');

if (!existsSync(MANIFEST)) fail(`Manifest not found at ${MANIFEST}. Set INFRA_DIR.`);
if (capture('git', ['status', '--porcelain'], INFRA)) fail(`${INFRA} has uncommitted changes.`);
const infraBranch = capture('git', ['rev-parse', '--abbrev-ref', 'HEAD'], INFRA);
if (infraBranch !== DEFAULT_BRANCH) fail(`The infrastructure checkout is on ${infraBranch}; switch to ${DEFAULT_BRANCH}.`);
run('git', ['pull', '--rebase', '--quiet'], INFRA);

const tag = head.slice(0, 12);
const image = `${IMAGE_REPO}:${tag}`;
const manifestText = readFileSync(MANIFEST, 'utf8');
const currentTag = manifestText.match(TAG_LINE)?.[1];
if (!currentTag) fail('Image tag line not found in the manifest.');
const publicUrl = PUBLIC_URL.replace(/\/+$/, '');
const imageExists = succeeds('docker', ['manifest', 'inspect', image]);

console.log(`Commit:     ${head} (${capture('git', ['log', '-1', '--format=%s'])})`);
console.log(`Image:      ${image}${imageExists ? ' (already pushed)' : ''}`);
console.log(`Manifest:   ${currentTag} -> ${tag}${currentTag === tag ? ' (already this one)' : ''}`);
console.log(`Production: ${publicUrl}`);

if (dryRun) {
	console.log('\n--dry-run: nothing was released.');
	process.exit(0);
}

const total = noDeploy ? 1 : 3;

// ---------- 1. Image ----------

step(1, total, imageExists ? `Image ${image} is already in the registry` : `Build ${PLATFORM} and push ${image}`);
if (!imageExists) {
	run('docker', [
		'build',
		'--platform', PLATFORM,
		'--label', `org.opencontainers.image.source=${SOURCE_REPO}`,
		'--label', `org.opencontainers.image.revision=${head}`,
		'--build-arg', `${REVISION_BUILD_ARG}=${tag}`,
		'-t', image,
		'.'
	]);
	run('docker', ['push', image]);
	if (!succeeds('docker', ['manifest', 'inspect', image])) fail('The image is not in the registry after the push.');
}
console.log('Image pushed.');

if (noDeploy) {
	console.log('\n--no-deploy: the manifest was not changed.');
	process.exit(0);
}

// ---------- 2. Manifest ----------

if (currentTag === tag) {
	step(2, total, `The manifest already names ${tag}; nothing to change`);
} else {
	step(2, total, `Change the manifest tag (${currentTag} -> ${tag}) through a pull request`);
	const releaseBranch = `chore/release-${tag}`;
	run('git', ['switch', '--quiet', '-c', releaseBranch], INFRA);
	writeFileSync(MANIFEST, manifestText.replace(TAG_LINE, tagLine(tag)));
	const changed = capture('git', ['diff', '--numstat'], INFRA);
	if (changed !== `1\t1\t${MANIFEST_PATH}`) {
		run('git', ['checkout', '--', '.'], INFRA);
		run('git', ['switch', '--quiet', DEFAULT_BRANCH], INFRA);
		run('git', ['branch', '-D', releaseBranch], INFRA);
		fail(`The edit would change more than the tag line (${changed}). Nothing was pushed.`);
	}
	// For a merge commit the pull request title is the first line of the body.
	const [subjectLine, ...bodyLines] = capture('git', ['log', '-1', '--format=%s%n%b']).split('\n');
	const subject = /^Merge pull request #/.test(subjectLine) ? bodyLines.find((l) => l.trim()) ?? subjectLine : subjectLine;
	run('git', ['commit', '--quiet', '-am', `chore: release ${tag} (${subject})`], INFRA);
	run('git', ['push', '--quiet', '-u', 'origin', releaseBranch], INFRA);
	const prUrl = capture('gh', ['pr', 'create', '--fill', '--base', DEFAULT_BRANCH, '--head', releaseBranch], INFRA).split('\n').pop();
	console.log(`Pull request: ${prUrl}`);
	// Follow the repository's merge rules; here: rebase, then a normal merge commit.
	run('git', ['fetch', '--quiet', 'origin'], INFRA);
	run('git', ['rebase', '--quiet', `origin/${DEFAULT_BRANCH}`], INFRA);
	if (capture('git', ['rev-parse', 'HEAD'], INFRA) !== capture('git', ['rev-parse', `origin/${releaseBranch}`], INFRA)) {
		run('git', ['push', '--quiet', '--force-with-lease', 'origin', releaseBranch], INFRA);
	}
	run('gh', ['pr', 'merge', prUrl, '--merge'], INFRA);
	run('git', ['switch', '--quiet', DEFAULT_BRANCH], INFRA);
	run('git', ['pull', '--rebase', '--quiet'], INFRA);
	run('git', ['branch', '--quiet', '-d', releaseBranch], INFRA);
	console.log('Merged; the platform redeploys with the new tag.');
}

// ---------- 3. Production ----------

step(3, total, `Waiting for ${publicUrl}${HEALTH_PATH} to report revision ${tag}`);
const deadline = Date.now() + 10 * 60_000;
let revision = '';
while (Date.now() < deadline) {
	try {
		const res = await fetch(`${publicUrl}${HEALTH_PATH}`, { signal: AbortSignal.timeout(10_000) });
		revision = (await res.json()).revision ?? '';
		if (revision === tag) break;
	} catch {
		// Unreachable during the switch: try again.
	}
	await sleep(10_000);
}
if (revision !== tag) {
	fail(
		`Production did not report revision ${tag} within 10 minutes (it reports "${revision || 'nothing'}"). ` +
			`Check ${RELEASES_PAGE}.` +
			(imageExists && revision === 'dev'
				? ' The image already existed and was built without the revision; the deploy may still have happened.'
				: '')
	);
}
const ready = await fetch(`${publicUrl}${READY_PATH}`, { signal: AbortSignal.timeout(10_000) }).catch(() => null);
if (!ready?.ok) fail(`Revision ${tag} is up, but the readiness check answered ${ready?.status ?? 'nothing'}.`);
console.log(`\n✓ ${tag} in production (${publicUrl}): health and readiness ok.`);
