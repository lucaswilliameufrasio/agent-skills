#!/usr/bin/env python3
"""Structural and privacy checks for this skills repository (stdlib only).

Run from anywhere: python3 scripts/validate_repo.py
Exits non-zero when any check fails.
"""

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
errors = []


def fail(path, message):
    errors.append(f"{path.relative_to(ROOT)}: {message}")


def tracked_text_files():
    skip_dirs = {".git", "node_modules"}
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if skip_dirs.intersection(path.relative_to(ROOT).parts):
            continue
        yield path


def parse_frontmatter(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if match is None:
        fail(path, "missing YAML frontmatter")
        return None
    block = match.group(1)
    name = re.search(r"^name:\s*(.+?)\s*$", block, re.M)
    description = re.search(r"^description:\s*(.*)$", block, re.M)
    if name is None:
        fail(path, "frontmatter lacks name")
    if description is None:
        fail(path, "frontmatter lacks description")
        return None
    if description.group(1).strip() in {"", ">-", ">", "|", "|-"}:
        # Folded/literal block: require an indented continuation line.
        tail = block[description.end():]
        if not re.match(r"\n\s+\S", tail):
            fail(path, "description is empty")
    return name.group(1).strip("\"'") if name else None


def check_skills():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    skill_dirs = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file():
            fail(skill_dir / "SKILL.md", "missing")
            continue
        name = parse_frontmatter(skill_file)
        if name is not None and name != skill_dir.name:
            fail(skill_file, f"name '{name}' != directory '{skill_dir.name}'")
        if f"skills/{skill_dir.name}/SKILL.md" not in readme:
            fail(ROOT / "README.md", f"does not list skill '{skill_dir.name}'")
        install = f"--skill {skill_dir.name} --global"
        if install not in readme:
            fail(ROOT / "README.md", f"lacks install command for '{skill_dir.name}'")
    known = {p.name for p in skill_dirs}
    for listed in re.findall(r"\(skills/([^/)]+)/SKILL\.md\)", readme):
        if listed not in known:
            fail(ROOT / "README.md", f"lists nonexistent skill '{listed}'")


def check_evals():
    for path in SKILLS.glob("*/evals.json"):
        check_eval_json(path, path.parent.name)
    for path in SKILLS.glob("*/evals/evals.json"):
        check_eval_json(path, path.parent.parent.name)
    for case in SKILLS.glob("*/evals/*/case.yaml"):
        case_dir = case.parent
        if not (case_dir / "prompt.md").is_file():
            fail(case, "case has no prompt.md")
        graders = list((case_dir / "graders").glob("*.md"))
        if not graders:
            fail(case, "case has no graders/*.md")
        text = case.read_text(encoding="utf-8")
        script = re.search(r"^\s*scaffold_script:\s*(\S+)", text, re.M)
        if script and not (case_dir / script.group(1)).is_file():
            fail(case, f"scaffold_script '{script.group(1)}' not found")


def check_eval_json(path, skill):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(path, f"invalid JSON: {exc}")
        return
    if data.get("skill_name") != skill:
        fail(path, f"skill_name '{data.get('skill_name')}' != '{skill}'")
    evals = data.get("evals")
    if not isinstance(evals, list) or not evals:
        fail(path, "evals must be a non-empty list")
        return
    seen = set()
    for item in evals:
        ident = item.get("id")
        if ident in seen:
            fail(path, f"duplicate eval id {ident}")
        seen.add(ident)
        for key in ("prompt", "expected_output"):
            if not str(item.get(key, "")).strip():
                fail(path, f"eval {ident} lacks {key}")
        for rel in item.get("files", []):
            if not (path.parent / rel).exists() and not (ROOT / rel).exists():
                fail(path, f"eval {ident} references missing file '{rel}'")


LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def check_links():
    for path in tracked_text_files():
        if path.suffix != ".md":
            continue
        in_fence = False
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if line.lstrip().startswith("```"):
                in_fence = not in_fence
            if in_fence:
                continue
            for target in LINK.findall(line):
                if re.match(r"[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
                    continue
                relative = unquote(target.split("#", 1)[0])
                if relative and not (path.parent / relative).exists():
                    fail(path, f"line {number}: broken link '{target}'")


PRIVATE_PATTERNS = [
    (re.compile(r"(?<![\w.])/(?:home|Users)/(?!<|\$|\{|user\b|you\b|name\b|example\b)[A-Za-z][\w.-]*/"), "absolute personal home path"),
    (re.compile(r"\b(?:10(?:\.\d{1,3}){3}|192\.168(?:\.\d{1,3}){2}|172\.(?:1[6-9]|2\d|3[01])(?:\.\d{1,3}){2})\b"), "private network address"),
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "private key block"),
    (re.compile(r"[\w.+-]+@(?!example\.(?:com|org|net)\b)[\w-]+\.[A-Za-z]{2,}"), "email address"),
]
# Allowlisted literal matches (public contact data intentionally in the repo).
PRIVATE_ALLOW = set()


def check_privacy():
    for path in tracked_text_files():
        if path.suffix not in {".md", ".json", ".yaml", ".yml", ".sh", ".py", ".toml", ".txt"}:
            continue
        for number, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            for pattern, label in PRIVATE_PATTERNS:
                for match in pattern.finditer(line):
                    if match.group(0) in PRIVATE_ALLOW:
                        continue
                    fail(path, f"line {number}: possible {label}: '{match.group(0)}'")


def main():
    check_skills()
    check_evals()
    check_links()
    check_privacy()
    if errors:
        print("\n".join(errors))
        print(f"\n{len(errors)} problem(s) found")
        return 1
    print("repository checks passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
