# drift.py

from typing import List


def detect_drift(intended: str, running: str) -> List[str]:
    drift_items = []

    intended_lines = set(intended.strip().splitlines())
    running_lines = set(running.strip().splitlines())

    missing = intended_lines - running_lines
    extra = running_lines - intended_lines

    for line in missing:
        drift_items.append(f"Missing line: {line}")

    for line in extra:
        drift_items.append(f"Unexpected line: {line}")

    return drift_items