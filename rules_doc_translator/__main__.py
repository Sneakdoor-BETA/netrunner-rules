from argparse import ArgumentParser

from rules_doc_translator.localize_NRDB import localize_NRDB


parser = ArgumentParser()
parser.add_argument("--nrdb", const=True, help="Generate NRDB card info", action="store_const")
args = parser.parse_args()

if args.nrdb is not None:
    localize_NRDB()
