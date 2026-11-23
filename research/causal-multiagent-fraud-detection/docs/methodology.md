# Mathematical Methodology

## Scope
The study evaluates a decision protocol that routes selected transactions to a simulated human-review stage. Its causal target is the effect of protocol interventions inside a declared simulation model. It does not identify real-world causal effects of human review or model the causes of fraud.

## Variables and agents
For transaction i, X_i denotes features and Y_i in {0,1} the fraud label. Three predictive agents produce probabilities p_1(X), p_2(X), p_3(X): Logistic Regression, Random Forest and HistGradientBoosting.

Ensemble probability:
P_E(X) = (p_1(X) + p_2(X) + p_3(X)) / 3.

Population disagreement:
D(X) = sqrt( sum_j (p_j(X) - P_E(X))^2 / 3 ).

Secondary disagreement measure: max_j p_j(X) - min_j p_j(X).

Binary entropy:
U(X) = -P_E log(P_E) - (1-P_E) log(1-P_E),
with limiting value 0 at probabilities 0 and 1.

Entropy measures uncertainty of the ensemble probability; disagreement measures dispersion between agents.

## Decision protocol
Let t be an automated threshold, l and u review-interval boundaries, and delta a disagreement threshold.

A(X) = 1[P_E(X) >= t].

R(X) = 1[l <= P_E(X) <= u OR D(X) >= delta].

For referred cases, simulate reviewer output H with sensitivity q_1 = Pr(H=1 | Y=1,R=1) and specificity q_0 = Pr(H=0 | Y=0,R=1). The label Y is used only to generate this simulated reviewer response and score outcomes; it is not an input to predictive models, review assignment or automated decisions.

F(X) = R(X)H + (1-R(X))A(X).

The simulation is an idealisation. It does not model reviewer fatigue, workload effects, correlated errors or organisational escalation unless explicitly added.

## Structural causal model
P_j := f_j(X; theta_j), j in {1,2,3}
P_E := mean(P_1,P_2,P_3)
D := population_sd(P_1,P_2,P_3)
U := binary_entropy(P_E)
A := 1[P_E >= t]
R := 1[l <= P_E <= u OR D >= delta]
H := g(Y, epsilon_H; q_1,q_0), when R=1
F := R*H + (1-R)*A
C := c(F,Y,R)

Here theta_j are fitted parameters and epsilon_H is reviewer simulation noise. Interventions do(t,l,u,delta) and do(q_1,q_0) identify effects only within this declared SCM.

## Cost-constrained optimisation
J(t,l,u,delta) = C_FP*FP + C_FN*FN + C_R*N_R.

Minimise J on validation data subject to:
- N_R/N <= B
- Recall(F,Y) >= rho
- 0 <= l <= u <= 1

Initial illustrative settings may be C_FP=1, C_FN=10, C_R=0.5, B=0.10 and rho=0.80. These are not elicited institutional costs or operational requirements. Vary them in sensitivity analysis. If no policy meets constraints, report infeasibility rather than silently relaxing constraints.

## Simulation estimands
For policy pi=(t,l,u,delta), let J(pi;q_1,q_0) be simulated loss. Compare:
ATE_sim = E[J(pi_a;q_1,q_0) - J(pi_b;q_1,q_0)]
over held-out transactions and simulation randomness. Also report changes in recall, precision, false-positive rate, review rate and cost. These are controlled simulation contrasts, not estimates of deployment effects with actual reviewers.

## Validity safeguards
- Split before fitting preprocessing; use training-only pipelines.
- Use stratified splits and add a chronological holdout if a meaningful timestamp exists.
- Calibrate probabilities without test leakage.
- Select all policy parameters on validation data; freeze before final test.
- Repeat across seeds and report bootstrap confidence intervals.
- Compare single-agent, probability-average, entropy-only and disagreement-only policies.
- Report PR-AUC, recall, precision, F1, confusion matrix, review rate, cost, Brier score and calibration.
- Run ablations and sensitivity analyses for costs, review capacity and reviewer assumptions.

## Limitations
The public dataset may not represent contemporary mobile-money fraud; anonymised features restrict interpretation. Reviewer behaviour is simulated from assumptions. This protocol alone does not establish deployment readiness, fairness, legal compliance or real-world causal effects.
