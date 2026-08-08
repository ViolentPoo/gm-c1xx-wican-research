#!/usr/bin/env python3
"""Lightweight equation audit for unresolved placeholders."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    for rel in ["data/pids.csv", "data/dids.csv"]:
        path = ROOT / rel
        with path.open(newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                equation = (row.get("equation") or "").lower()
                confidence = row.get("confidence", "")
                if "unknown" in equation and confidence in {"Confirmed", "Strongly likely"}:
                    print(f"WARN {rel}: {row.get('name')} has {confidence} but unknown equation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
