#!/usr/bin/env python3
"""Validate the Praxis Atlas repository without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "select-methodologies"
SKILL_MD = SKILL / "SKILL.md"
REFERENCES = SKILL / "references"
REQUIRED_ROOT = (
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "GOVERNANCE.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "CITATION.cff",
    "AGENTS.md",
    "tests/scenarios/selection-invariants.md",
)
LINK_PATTERN = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
ROUTE_PATTERN = re.compile(r"references/([0-9]{2}-[^`\s|)]+\.md)")


def check(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip()
    return values


def validate_links(markdown: Path, errors: list[str]) -> None:
    text = markdown.read_text(encoding="utf-8")
    for raw in LINK_PATTERN.findall(text):
        target = raw.split("#", 1)[0].strip()
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        resolved = (markdown.parent / unquote(target)).resolve()
        check(resolved.exists(), f"Broken link in {markdown.relative_to(ROOT)}: {raw}", errors)


def main() -> int:
    errors: list[str] = []
    for relative in REQUIRED_ROOT:
        check((ROOT / relative).is_file(), f"Missing required root file: {relative}", errors)

    check(SKILL_MD.is_file(), "Missing installable skill", errors)
    check((SKILL / "agents" / "openai.yaml").is_file(), "Missing skill UI metadata", errors)
    check((SKILL / "assets" / "icon.svg").is_file(), "Missing skill icon", errors)

    skill_text = SKILL_MD.read_text(encoding="utf-8") if SKILL_MD.is_file() else ""
    metadata = frontmatter(skill_text)
    check(metadata.get("name") == "select-methodologies", "Unexpected skill name", errors)
    check(bool(metadata.get("description")), "Missing skill description", errors)
    check(len(skill_text.splitlines()) < 500, "SKILL.md exceeds progressive-disclosure limit", errors)

    reference_files = sorted(REFERENCES.glob("*.md")) if REFERENCES.is_dir() else []
    check(len(reference_files) == 37, f"Expected 37 reference files, found {len(reference_files)}", errors)
    routed = set(ROUTE_PATTERN.findall(skill_text))
    actual = {path.name for path in reference_files}
    check(routed == actual, f"Routing mismatch: missing={sorted(actual-routed)}, unknown={sorted(routed-actual)}", errors)

    for reference in reference_files:
        text = reference.read_text(encoding="utf-8")
        h1 = [line for line in text.splitlines() if line.startswith("# ")]
        check(len(h1) == 1, f"Expected one H1 in {reference.relative_to(ROOT)}, found {len(h1)}", errors)

    for markdown in ROOT.rglob("*.md"):
        if ".git" in markdown.parts:
            continue
        text = markdown.read_text(encoding="utf-8")
        check("[TODO" not in text, f"Unresolved TODO placeholder in {markdown.relative_to(ROOT)}", errors)
        validate_links(markdown, errors)

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"Validation failed with {len(errors)} error(s).")
        return 1

    print(f"Validation passed: {len(reference_files)} catalogs and references checked.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
