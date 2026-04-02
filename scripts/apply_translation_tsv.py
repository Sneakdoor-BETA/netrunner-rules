#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

from apply_translation_map import load_json, localize_tags


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Apply key<TAB>translation lines from stdin to a translation JSON file."
    )
    parser.add_argument("target", help="Target translation JSON file")
    args = parser.parse_args()

    mapping: dict[str, str] = {}
    import sys

    for raw_line in sys.stdin.read().splitlines():
        if not raw_line.strip():
            continue
        if "\t" not in raw_line:
            raise ValueError(f"Line is missing a tab separator: {raw_line!r}")
        key, translation = raw_line.split("\t", 1)
        mapping[key] = translation

    target_path = Path(args.target)
    data = load_json(target_path)
    for entry in data:
        key = entry["key"]
        if key in mapping:
            entry["translation"] = localize_tags(mapping[key])

    with target_path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
        f.write("\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
