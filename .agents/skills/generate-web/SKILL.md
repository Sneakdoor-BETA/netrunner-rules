---
name: generate-web
description: Generate the web version of the Netrunner rules documentation. Use this skill when the user asks to "生成中文网页" or "生成英文网页".
---

Run one of these commands based on the user request:

- If the user asks for "生成中文网页":

```bash
uv run python -m rules_doc_generator -t web -p translation -o translation/final
```

- If the user asks for "生成英文网页":

```bash
uv run python -m rules_doc_generator -t web -p data -o html
```
