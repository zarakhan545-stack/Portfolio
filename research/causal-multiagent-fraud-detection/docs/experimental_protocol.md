# Experimental Protocol — Pre-registration Draft

## Research questions
1. Does agent disagreement identify useful review cases beyond ensemble entropy?
2. Under fixed review capacity, can the protocol reduce declared decision cost while meeting a recall constraint?
3. How sensitive are results to reviewer sensitivity/specificity assumptions and cost ratios?

## Dataset
Planned source: ULB/Worldline credit-card fraud dataset distributed via Kaggle: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud. Record download date, source terms, checksum, schema, class prevalence, missingness, duplicates and exclusions. Do not commit raw data unless redistribution rights are confirmed.

## Splits
Primary protocol: stratified 60% training, 15% validation and 25% final test, with fixed reported seed. If timestamps support meaningful chronology, add a separate chronological holdout. Do not conflate the two protocols.

## Preprocessing and fitting
- Exclude identifiers and target from predictors.
- Fit imputers, scalers, encoders and feature selection only within training folds using pipelines.
- Fit Logistic Regression, Random Forest and HistGradientBoosting.
- Handle class imbalance using training-only class weights or sampling; leave validation/test prevalence unchanged.
- Calibrate probabilities without fitting on test labels.

## Policy selection
Select t, l, u and delta on validation data over a predeclared grid. Enforce review-budget and recall constraints. Record the grid, tie-breaking rule and infeasible combinations. Test data must not influence policy selection.

## Reviewer simulation
For referred cases, sample reviewer output conditional on true label using declared q_1 and q_0. These are assumptions, not measured human accuracy. Evaluate weak, moderate and strong reviewer scenarios using multiple simulation seeds. Clearly label this as simulation.

## Comparators and ablations
1. Each single agent.
2. Mean-probability ensemble without review.
3. Entropy-only review.
4. Disagreement-only review.
5. Combined interval-or-disagreement review.
6. Optional majority-vote comparator.

## Outcomes
Primary: declared cost per transaction under each cost scenario, subject to review-budget and recall constraints.

Secondary: PR-AUC, ROC-AUC (interpreted carefully under class imbalance), recall, precision, F1, false-positive rate, false-negative count, review rate, Brier score, calibration curve and latency only if measured reproducibly.

## Statistical analysis
- Evaluate the frozen policy once on the held-out test set.
- Report confusion matrices and uncertainty intervals.
- Use stratified bootstrap and paired comparisons where appropriate.
- Repeat model fitting over multiple seeds; report variability, not only the best run.
- Plot sensitivity over cost ratios, review budget, recall floor, q_1 and q_0.
- Report all tested variants; avoid selective reporting.

## Reproducibility checklist
- [ ] Dataset source, terms, checksum and schema recorded.
- [ ] Split indices and seeds saved.
- [ ] Training-only preprocessing pipelines used.
- [ ] Calibration method documented.
- [ ] Validation policy grid and tie-break rule recorded.
- [ ] Test set kept untouched until policy freeze.
- [ ] Reviewer assumptions and simulation seeds documented.
- [ ] Baselines, ablations and sensitivity analyses completed.
- [ ] Confidence intervals and limitations reported.
- [ ] No synthetic/demo output presented as empirical evidence.

## Stop/go rule
Do not describe this as an empirical study or submit numerical findings until data has been obtained lawfully, the protocol executed, and results checked for leakage and reproducibility.
