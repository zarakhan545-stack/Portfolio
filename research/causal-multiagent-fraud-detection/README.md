# Causal-Aware Multi-Agent Fraud Detection

Researcher: Zarafishan Ashiq

**Status: proposed methodology and experimental scaffold. No empirical experiments or results are claimed.**

This project studies a decision protocol for fraud detection using three predictive agents, probability disagreement, uncertainty, and a simulated human-review stage. Its causal scope is the decision protocol under explicit simulation assumptions; it does not model the causes of fraud or identify real-world effects of human review.

## Dataset
Planned source: [ULB/Worldline credit-card fraud dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud). Obtain the data from its source, record the download details and terms, and do not commit raw data unless redistribution rights are clear.

## Proposed agents
- Logistic Regression
- Random Forest
- HistGradientBoosting

For agent probabilities p1, p2, p3, define ensemble probability as their mean and disagreement as their population standard deviation. Binary entropy of the ensemble probability is a separate uncertainty measure.

A transaction is referred for review if its ensemble probability lies in a validation-selected interval or agent disagreement exceeds a validation-selected threshold. Referred cases receive a simulated reviewer decision with declared sensitivity and specificity assumptions. These assumptions are not observed human performance.

## Files
- docs/methodology.md — structural causal model, equations, optimisation and estimands.
- docs/experimental_protocol.md — data splits, model fitting, validation, test protocol and robustness checks.
- src/decision_protocol.py — deterministic policy calculations.

## Integrity safeguards
- Fit preprocessing and calibration without test data.
- Select thresholds and policy parameters on validation data only.
- Freeze the policy before final test evaluation.
- Report confidence intervals, baselines, ablations and sensitivity analyses.
- Never present demo/synthetic outputs as empirical findings.
- The initial review budget (10%), recall floor (80%) and relative costs (FP=1, FN=10, review=0.5) are illustrative only, not estimated operational values.

No dataset has been processed and no model has been trained in this repository version.
