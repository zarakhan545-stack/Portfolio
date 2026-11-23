# Dataset instructions

Do not upload the raw `creditcard.csv` dataset to this repository.

1. Download the ULB/Worldline Credit Card Fraud Detection dataset from Kaggle under its current terms, or allow the pipeline to fetch OpenML dataset ID 1597.
2. For manual download, place the extracted CSV at `data/creditcard.csv`.
3. Run from the project directory: `python -m src.pipeline --data data/creditcard.csv --output outputs`.
4. Record retrieval date and checksum. The pipeline records the SHA-256 fingerprint for local CSV files, row counts and exact duplicate exclusions.

The OpenML route requires internet access. If it fails, download the CSV manually and pass `--data`.