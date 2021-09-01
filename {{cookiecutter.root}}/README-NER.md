# Additional Information for NER

Data is expected in [Conll/NER Format](https://spacy.io/api/cli#converters). If this is not applicable, write your own transformer and save the [DocBin](https://spacy.io/api/docbin) in `./data/processed/`.

1. Copy your data to `data/raw` folder or load the data via dvc.
2. Convert data: Call `python {{cookiecutter.code_dir}}/preprocessing/convert_data.py` from project root directory.
3. Train with command: `python -m spacy train {{cookiecutter.code_dir}}/config/config.cfg --output ./models --paths.train ./data/processed/train.spacy --paths.dev ./data/processed/dev.spacy` from project root directory. Note: change the path in case the filenames are not the same as here.