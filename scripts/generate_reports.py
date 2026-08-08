#!/usr/bin/env python3
"""Placeholder report generator for future expanded research."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    outputs = sorted((ROOT / "output").glob("*.md"))
    print("Generated reports currently maintained as Markdown files:")
    for path in outputs:
        print(f"- {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
