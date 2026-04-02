#!/usr/bin/env python3
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "translation" / "yaml2json"

TAG_RE = re.compile(r"\{([a-zA-Z/]+):?([^{}]*)\}")
BRACKET_TOKEN_RE = re.compile(r"\[[^\[\]]+\]")


def tag_multiset(text: str) -> Counter[tuple[str, str]]:
    counter: Counter[tuple[str, str]] = Counter()
    for kind, value in TAG_RE.findall(text):
        counter[(kind, value)] += 1
    return counter


def bracket_multiset(text: str) -> Counter[str]:
    return Counter(BRACKET_TOKEN_RE.findall(text))


def has_ascii_words_in_tags(text: str) -> list[str]:
    issues = []
    for kind, value in TAG_RE.findall(text):
        if kind in {"ref", "curly", "/n", "n"}:
            continue
        if re.search(r"[A-Za-z]", value):
            issues.append("{" + (f"{kind}:{value}" if value else kind) + "}")
    return issues


def main() -> int:
    findings: dict[str, list[dict[str, object]]] = defaultdict(list)

    for path in sorted(BASE.glob("*.json")):
        data = json.loads(path.read_text())
        for entry in data:
            key = entry["key"]
            original = entry["original"]
            translation = entry["translation"]

            if not translation.strip():
                findings["untranslated"].append(
                    {"file": path.name, "key": key, "original": original}
                )
                continue

            tag_issues = has_ascii_words_in_tags(translation)
            if tag_issues:
                findings["ascii_in_tags"].append(
                    {
                        "file": path.name,
                        "key": key,
                        "original": original,
                        "translation": translation,
                        "issues": tag_issues,
                    }
                )

            original_tags = tag_multiset(original)
            translation_tags = tag_multiset(translation)
            if Counter({k: v for k, v in original_tags.items() if k[0] in {"ref", "n", "/n", "curly"}}) != Counter(
                {k: v for k, v in translation_tags.items() if k[0] in {"ref", "n", "/n", "curly"}}
            ):
                findings["structural_tag_mismatch"].append(
                    {
                        "file": path.name,
                        "key": key,
                        "original": original,
                        "translation": translation,
                    }
                )

            if bracket_multiset(original) != bracket_multiset(translation):
                findings["bracket_token_mismatch"].append(
                    {
                        "file": path.name,
                        "key": key,
                        "original": original,
                        "translation": translation,
                    }
                )

    print(json.dumps(findings, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
