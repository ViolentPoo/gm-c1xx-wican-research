#!/usr/bin/env python3
"""Normalize PID/DID CSV files by checking required columns and row counts."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


REQUIRED = {
    "data/pids.csv": ["name", "service", "pid", "request", "confidence", "status"],
    "data/dids.csv": ["name", "service", "did", "request", "confidence", "status"],
    "data/broadcast-signals.csv": ["name", "can_id", "confidence", "status"],
    "data/module-addresses.csv": ["module", "request_id", "response_id", "confidence", "status"],
}


def main() -> int:
    for rel, columns in REQUIRED.items():
        path = ROOT / rel
        with path.open(newline="", encoding="utf-8") as handle:
            reader = csv.DictReader(handle)
            missing = [column for column in columns if column not in (reader.fieldnames or [])]
            rows = list(reader)
        if missing:
            raise SystemExit(f"{rel}: missing columns {missing}")
        print(f"{rel}: {len(rows)} rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
