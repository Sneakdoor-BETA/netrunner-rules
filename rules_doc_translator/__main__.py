from argparse import ArgumentParser

from rules_doc_translator.localize_NRDB import localize_NRDB
from rules_doc_translator.to_Paratranz import yaml2json
from rules_doc_translator.from_Paratranz import json2yaml


parser = ArgumentParser()
parser.add_argument("--nrdb", const=True, help="Generate NRDB card info", action="store_const")
parser.add_argument("--yaml2json", const=True, help="Generate texts in JSON", action="store_const")
parser.add_argument("--json2yaml", const=True, help="Generate texts in YAML", action="store_const")
args = parser.parse_args()

if args.nrdb is not None:
    localize_NRDB()
elif args.yaml2json is not None:
    yaml2json()
elif args.json2yaml is not None:
    json2yaml()
