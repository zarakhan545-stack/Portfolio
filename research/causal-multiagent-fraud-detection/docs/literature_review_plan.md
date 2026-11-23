# Literature review plan

This is a structured search plan, not a claim that the literature review is complete.

## Search themes
1. Credit-card fraud detection under extreme class imbalance.
2. Probability calibration for rare-event classifiers.
3. Ensemble disagreement and uncertainty-based selective prediction / human review.
4. Decision-theoretic optimisation with review-capacity constraints.
5. Evaluation protocols, temporal drift and leakage in fraud datasets.
6. Causal inference versus structural causal simulation in human-in-the-loop decision systems.

## Seed sources to verify and read
- Dal Pozzolo et al., *Calibrating Probability with Undersampling for Unbalanced Classification* (2015). Verify exact venue, pages and DOI before citation.
- Carcillo et al., *Combining Unsupervised and Supervised Learning in Credit Card Fraud Detection* (Information Sciences, 2019). Verify bibliographic metadata.
- Lebichot et al., *Deep-Learning Domain Adaptation Techniques for Credit Cards Fraud Detection* (2019). Verify conference metadata.
- ULB/Worldline dataset documentation and the Fraud Detection Handbook should support data provenance and evaluation choices, not substitute for peer-reviewed methodological literature.

## Required review output
For every paper, record its research question, dataset, split strategy, imbalance treatment, calibration, metrics, limitations and the exact gap addressed by this study. Distinguish established findings from proposed hypotheses. Confirm each DOI and citation against the publisher or Crossref before writing the manuscript.

## Gap claim to test, not assume
A potential contribution is a controlled comparison of probability disagreement and ensemble entropy as review-routing signals under fixed review-capacity and cost/recall constraints, with reviewer accuracy varied explicitly as a simulation assumption. The review must establish whether this exact combination is novel; do not claim novelty based only on a small keyword search.