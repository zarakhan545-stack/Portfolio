# Causal-Aware Multi-Agent Fraud Detection

Researcher: Zarafishan Ashiq

**Status: reproducible experimental implementation added; empirical execution on the full public dataset is still pending. No empirical performance results are claimed.**

This project evaluates a decision protocol for fraud detection using three calibrated predictive agents, probability disagreement, ensemble uncertainty, and a simulated human-review stage. Its causal scope is limited to interventions within an explicitly declared simulation model; it does not identify real-world effects of actual human reviewers.

## Dataset

Primary benchmark: [ULB/Worldline credit-card fraud dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud), also accessible through OpenML dataset ID 1597. The benchmark is highly imbalanced (492 fraud cases among 284,807 transactions in the canonical dataset description). Raw data is not included in this repository. See [data/README.md](data/README.md).

## Implemented agents and pipeline

- Class-weighted Logistic Regression
- Class-weighted Random Forest
- Class-weighted HistGradientBoosting
- Training-fold-only sigmoid calibration
- Stratified 60/15/25 train/validation/test split
- Validation-only selection of automated threshold and review policy
- Simulated reviewer sensitivity/specificity scenarios
- Combined, entropy-only, disagreement-only and no-review ensemble comparators
- PR-AUC / average precision, ROC-AUC, Brier score, precision, recall, F1, false-positive rate, review rate and declared cost
- Stratified bootstrap intervals and reviewer-simulation variability
- Frozen-policy sensitivity grid for reviewer quality, false-negative cost and review capacity

## Run locally or in Google Colab

Python 3.11 is recommended.

```bash
python -m pip install -r requirements.txt
python -m pytest -q
python -m src.pipeline --data data/creditcard.csv --output outputs
```

Alternatively, omit `--data` to retrieve OpenML dataset ID 1597 (internet required):

```bash
python -m src.pipeline --output outputs
```

Outputs are written to `outputs/results.json` and `outputs/dataset_metadata.json`; generated data and outputs are gitignored. The raw dataset must not be committed.

## Integrity and interpretation safeguards

- Preprocessing, model fitting and calibration use training data only.
- Policy parameters are selected on validation data only; test data is held out for final evaluation.
- Exact duplicate rows are removed before splitting and the count is recorded.
- Reviewer sensitivity and specificity are assumptions in a simulation, not observed human accuracy.
- Initial costs, review budget, recall floor and reviewer assumptions are illustrative, not operationally elicited.
- The random stratified split is not evidence of future-time generalisation; a chronological robustness evaluation remains desirable.
- Synthetic smoke-test outputs are software checks only and must never be described as research findings.

## Current completion checklist

- [x] Research question, mathematical decision protocol and experimental design
- [x] Reproducible model-training and evaluation implementation
- [x] Unit tests and GitHub Actions workflow
- [x] Dataset instructions and checksum/metadata capture for local CSV
- [x] Baselines, simulated reviewer evaluation and sensitivity analysis code
- [ ] Execute full pipeline on the real ULB/Worldline dataset
- [ ] Inspect real outputs, feasibility, calibration and leakage
- [ ] Complete expanded ablations and robustness experiments
- [ ] Verify and complete peer-reviewed literature review
- [ ] Write results and discussion from actual outputs

**Do not call this a completed empirical study until the unchecked items are completed and the real outputs have been reviewed.**

## Research documents

- [Mathematical methodology](docs/methodology.md)
- [Experimental protocol](docs/experimental_protocol.md)
- [Literature review plan](docs/literature_review_plan.md)
- [Implementation guide and bundle](IMPLEMENTATION.md)
- [Deterministic decision protocol](src/decision_protocol.py)
- Full training/evaluation pipeline and test suite: included in [implementation bundle](implementation_bundle.tar.gz)
