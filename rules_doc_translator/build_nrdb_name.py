from __future__ import annotations

from collections import defaultdict, deque
import json
from pathlib import Path
import re


LINE_PATTERN = re.compile(r'^\s*("(?:\\.|[^"\\])*")\s*:\s*("(?:\\.|[^"\\])*")\s*$')


def read_flat_yaml(path: Path) -> list[tuple[str, str]]:
    entries: list[tuple[str, str]] = []
    with path.open("r", encoding="utf-8") as file:
        for line_number, raw_line in enumerate(file, start=1):
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue

            match = LINE_PATTERN.match(line)
            if match is None:
                raise ValueError(f"Unsupported YAML format in {path}:{line_number}: {raw_line.rstrip()}")

            key = json.loads(match.group(1))
            value = json.loads(match.group(2))
            entries.append((key, value))
    return entries


def dump_flat_yaml(entries: list[tuple[str, str]], path: Path) -> None:
    with path.open("w", encoding="utf-8") as file:
        file.write("# GENERATED, DO NOT EDIT\n")
        for key, value in entries:
            file.write(f"{json.dumps(key, ensure_ascii=False)}: {json.dumps(value, ensure_ascii=False)}\n")


def build_nrdb_name() -> tuple[list[tuple[str, str]], list[tuple[str, str]]]:
    base_path = Path("generated/nrdb")
    nrdb_entries = read_flat_yaml(base_path / "nrdb.yaml")
    localized_entries = read_flat_yaml(base_path / "localize_nrdb.yaml")

    localized_names_by_id: dict[str, deque[str]] = defaultdict(deque)
    for localized_name, card_id in localized_entries:
        localized_names_by_id[card_id].append(localized_name)

    paired_entries: list[tuple[str, str]] = []
    unmatched_nrdb: list[tuple[str, str]] = []

    for nrdb_name, card_id in nrdb_entries:
        if localized_names_by_id[card_id]:
            paired_entries.append((nrdb_name, localized_names_by_id[card_id].popleft()))
        else:
            unmatched_nrdb.append((nrdb_name, card_id))

    unmatched_localized: list[tuple[str, str]] = []
    for card_id, names in localized_names_by_id.items():
        for localized_name in names:
            unmatched_localized.append((localized_name, card_id))

    dump_flat_yaml(paired_entries, base_path / "nrdb_name.yaml")
    return unmatched_nrdb, unmatched_localized


if __name__ == "__main__":
    unmatched_nrdb, unmatched_localized = build_nrdb_name()

    print("Unmatched nrdb fields:")
    for field_name, card_id in unmatched_nrdb:
        print(f"{card_id}\t{field_name}")

    print("Unmatched localize fields:")
    for field_name, card_id in unmatched_localized:
        print(f"{card_id}\t{field_name}")
