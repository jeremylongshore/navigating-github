#!/usr/bin/env python3
"""Validate the public skill, plugin catalog, and command wiring."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "navigating-github" / "SKILL.md"
COMMAND = ROOT / "commands" / "github-learn.md"
PLUGIN = ROOT / ".claude-plugin" / "plugin.json"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
EXPECTED_NAME = "navigating-github"


def frontmatter_scalar(document: str, key: str) -> str | None:
    frontmatter = document.split("---", 2)[1]
    match = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", frontmatter, re.MULTILINE)
    if not match:
        return None
    return match.group(1).strip().strip('"').strip("'")


def main() -> int:
    failures: list[str] = []

    def require(condition: bool, message: str) -> None:
        if not condition:
            failures.append(message)

    skill = SKILL.read_text(encoding="utf-8")
    command = COMMAND.read_text(encoding="utf-8")
    plugin = json.loads(PLUGIN.read_text(encoding="utf-8"))
    marketplace = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    entry = marketplace["plugins"][0]

    require(plugin["name"] == EXPECTED_NAME, "plugin name drifted")
    require(entry["name"] == EXPECTED_NAME, "marketplace entry name drifted")
    require(entry["source"] == "./", "marketplace entry must use local source")
    require(plugin["version"] == entry["version"], "manifest versions differ")
    require(
        frontmatter_scalar(skill, "version") == plugin["version"],
        "skill and manifest versions differ",
    )
    require(
        frontmatter_scalar(skill, "compatibility") is not None,
        "current compatibility metadata is missing",
    )
    require(
        frontmatter_scalar(skill, "compatible-with") is None,
        "deprecated compatible-with metadata returned",
    )
    require(plugin["skills"] == "./skills/", "plugin skills path drifted")
    require(plugin["commands"] == "./commands/", "plugin commands path drifted")
    require(
        "${CLAUDE_PLUGIN_ROOT}/skills/navigating-github/SKILL.md" in command,
        "command does not use the plugin-root skill path",
    )
    require(
        "${CLAUDE_SKILL_DIR}/skills/" not in command,
        "command contains the stale skill-root path",
    )

    for heading in ("## Prerequisites", "## Error Handling", "## Resources"):
        require(heading in skill, f"required skill section missing: {heading}")

    for reference in (
        "claude-github-platforms.md",
        "error-recovery-playbook.md",
        "git-concepts-glossary.md",
        "github-review-apps.md",
        "learning-curriculum.md",
        "safety-rules.md",
        "skill-assessment-guide.md",
    ):
        require(
            (SKILL.parent / "references" / reference).is_file(),
            f"required reference missing: {reference}",
        )

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1

    print("Repository consistency: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
