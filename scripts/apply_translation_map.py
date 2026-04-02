#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
REF_DIR = ROOT / ".agents" / "skills" / "translate-rule" / "references"


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def build_term_map() -> dict[str, str]:
    term_map: dict[str, str] = {}
    for filename in ["wording.json", "phrasing.json", "terminology.json"]:
        for row in load_json(REF_DIR / filename):
            term_map[row["en"]] = row["translation"]
    return term_map


TERM_MAP = build_term_map()
CARD_MAP = load_yaml(REF_DIR / "localize_name.yaml")
PRODUCT_MAP = {
    "System Gateway Starter Pack": "系统入口起始包",
}
SUBTYPE_MAP = {
    "directive": "指令",
    "directives": "指令",
    "connections": "人脉",
    "region": "区域",
    "regions": "区域",
    "alliance": "联盟",
    "current": "局势",
    "lockdown": "封锁",
    "consoles": "控制台",
    "icebreakers": "破解器",
    "Icebreaker": "破解器",
    "terminal": "终端",
    "stealth": "隐匿",
}


def localize_tag(kind: str, value: str) -> str:
    trimmed = value.strip()
    if kind == "card":
        return CARD_MAP.get(trimmed, trimmed)
    if kind == "term":
        return TERM_MAP.get(trimmed, trimmed)
    if kind == "subtype":
        return TERM_MAP.get(trimmed, SUBTYPE_MAP.get(trimmed, trimmed))
    if kind == "product":
        return PRODUCT_MAP.get(trimmed, trimmed)
    return value


TAG_RE = re.compile(r"\{(card|term|subtype|product):([^{}]+)\}")


def localize_tags(text: str) -> str:
    def repl(match: re.Match[str]) -> str:
        kind = match.group(1)
        value = match.group(2)
        return "{" + kind + ":" + localize_tag(kind, value) + "}"

    return TAG_RE.sub(repl, text)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Apply a JSON mapping of key->translation to a translation file."
    )
    parser.add_argument("target", help="Target translation JSON file")
    args = parser.parse_args()

    mapping = json.load(__import__("sys").stdin)
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
