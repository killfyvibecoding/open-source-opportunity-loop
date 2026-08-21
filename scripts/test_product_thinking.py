#!/usr/bin/env python3
"""Behavioral contract for the product-thinking layer."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def require(text: str, needle: str, label: str) -> None:
    if needle not in text:
        raise AssertionError(f"missing {label}: {needle}")


def main() -> int:
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    router = (ROOT / "references" / "interaction-router.md").read_text(encoding="utf-8")
    product_ref = ROOT / "references" / "product-thinking.md"

    require(skill, "Product thinking gate", "product thinking gate in SKILL.md")
    require(skill, "desired outcome", "outcome-first product framing")
    require(skill, "opportunity -> solution -> experiment", "opportunity-to-experiment chain")
    require(router, "Product discovery", "product discovery route")
    if not product_ref.is_file():
        raise AssertionError("missing product-thinking reference")

    reference = product_ref.read_text(encoding="utf-8")
    for needle in ("buyer", "job_to_be_done", "assumption", "MVP"):
        require(reference, needle, f"product-thinking reference concept: {needle}")

    print("Product-thinking contract is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
