#!/usr/bin/env python3
"""Report duplicate request/CAN identifiers across research CSV files."""

from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def collect(path: Path, key: str) -> dict[str, list[str]]:
    found: dict[str, list[str]] = defaultdict(list)
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            value = row.get(key, "").strip()
            if value:
                found[value].append(row.get("name") or row.get("module") or path.name)
    return found


def main() -> int:
    datasets = [
        (ROOT / "data/pids.csv", "request"),
        (ROOT / "data/dids.csv", "request"),
        (ROOT / "data/broadcast-signals.csv", "can_id"),
    ]
    for path, key in datasets:
        duplicates = {k: v for k, v in collect(path, key).items() if len(v) > 1}
        print(f"{path.relative_to(ROOT)}: {len(duplicates)} duplicate {key} values")
        for value, names in sorted(duplicates.items()):
            print(f"  {value}: {', '.join(names)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
