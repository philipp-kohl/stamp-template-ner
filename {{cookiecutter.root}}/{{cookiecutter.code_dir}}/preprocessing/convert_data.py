from pathlib import Path

from spacy.cli.convert import convert
from wasabi import Printer

from {{cookiecutter.code_dir}}.configuration import get_all_raw_data, processed_data_dir

files = get_all_raw_data()

for file in files:
    convert(input_path=file, output_dir=processed_data_dir, converter="ner", file_type="spacy",
            msg=Printer(no_print=False))
