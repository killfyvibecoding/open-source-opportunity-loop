#!/usr/bin/env python3
"""Validate the repository's required Skill files without third-party packages."""

from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    ROOT / "SKILL.md",
    ROOT / "agents" / "openai.yaml",
    ROOT / "references" / "source-catalog.md",
    ROOT / "references" / "search-workflow.md",
    ROOT / "references" / "license-and-health.md",
    ROOT / "references" / "monetization-playbook.md",
    ROOT / "references" / "product-thinking.md",
    ROOT / "scripts" / "test_product_thinking.py",
]


def main() -> int:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED if not path.is_file()]
    if missing:
        print("Missing required files:")
        print("\n".join(f"- {item}" for item in missing))
        return 1

    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not skill.startswith("---\n") or "name: open-source-opportunity-loop" not in skill:
        print("SKILL.md does not contain the expected frontmatter.")
        return 1
    if "[TODO" in skill:
        print("SKILL.md still contains TODO placeholders.")
        return 1

    product_test = subprocess.run(
        ["python3", str(ROOT / "scripts" / "test_product_thinking.py")],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if product_test.returncode:
        print(product_test.stdout, end="")
        print(product_test.stderr, end="")
        return product_test.returncode

    print("Skill structure is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
