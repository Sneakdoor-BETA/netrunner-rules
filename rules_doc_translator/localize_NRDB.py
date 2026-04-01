import json
import yaml


def localize_NRDB():
    dst_filename = "generated/nrdb/localize_nrdb.yaml"
    data_filename = "translation/references/cards.json"

    result: dict[str, str] = dict()
    with open(data_filename, "r", encoding="utf-8") as data_file:
        items = json.load(data_file)
        for item in items:
            k = item["title_zhCN"]
            v = item["id"]
            result[k] = v
            if "：" in k:
                k1, _ = k.split("：")
                result[k1] = v

    with open(dst_filename, "w") as dst_file:
        yaml.dump(result, dst_file, sort_keys=False, encoding="utf-8", allow_unicode=True, width=100000, default_style='"')
