# Final Exam Interactive Slides Manual (Generated 2025-12-19)


## 1) What is in-scope for the final exam (based on provided slides)

Only topics that appear in the provided HTML slides are treated as in-scope. If something is listed in a syllabus image but is not present in any provided slide file, it is excluded.

### In-scope (present in slides)

**A. Classification (trees & validation)**
- Feature-selection / split scoring: Gini, Entropy / Information Gain, Fisher score (interactive lab).
- Decision-tree building: splitting, stopping, overfit intuition (interactive tree builder).
- Rule generation from a decision tree; sequential covering (interactive rule/covering slide).
- Validation strategies: holdout vs k-fold cross-validation (interactive lab).

**B. Association Pattern Mining (Apriori)**
- Frequent pattern mining model (market-basket simulation).
- Apriori algorithm mechanics: L1 counting, candidate generation, pruning (Apriori property), joining via prefix logic, scanning for L2/L3.
- Association rule generation; support & confidence.
- Interestingness: confidence trap; correlation/phi; chi-square significance.

### Extra exam rule (given by instructor)
- **Neural Networks (extra-topic):** one **very simple** concept-only question will appear in every set (no medium/hard).

### Excluded - NOT IN FINAL EXAM (not found in provided slides)
- Naïve Bayes classifier (mentioned in syllabus image, but not present in the provided slide files).
- Precision/Recall/F1, Sensitivity/Specificity (not found in provided slide files).
- Enumeration-tree algorithm and recursive suffix-based pattern growth (not found in provided slide files).
- Brute-force frequent itemset mining (not explicitly present in provided slide files; Apriori is used instead).

## 2) Slide inventory (recommended study order)

### 2.1 Classification block
1. `index.html` — course navigation / foundations & classification overview.
2. `fs_and_splits_lab.html` — feature selection & split scoring lab (Gini/Entropy/Fisher).
3. `tree_builder.html` — build a decision tree interactively.
4. `tree_rules_and_covering.html` — tree-to-rules + sequential covering.
5. `validation_strategies_lab.html` — holdout vs k-fold validation lab.

### 2.2 Association mining block (Apriori)
6. `apriori_lab.html` — market basket concept + Apriori walkthrough + prefix merging.
7. `apriori_part1_market_L1.html` — Part 1 (market + L1).
8. `apriori_part2_pairs_L2.html` — Part 2 (pairs/L2).
9. `apriori_part3_evolution_rules.html` — Part 3 (evolution L2→L3, support/confidence, rule generation, pruning).
10. `apriori_part4_Statistical Coefficient of Correlation.html` — Part 4 (correlation/phi + confidence trap).
11. `apriori_part5_Statistical Significance The Chi-Square Test__vTWO.html` — Part 5 (chi-square significance).

### 2.3 Neural-net micro block (extra-topic)
12. `boundary_sculptor_UnlimitedNeuron.html` — decision boundary intuition.
13. `neuron_xray.html` — neuron/activation intuition.
14. `deep_layers.html` — depth intuition.
15. `high_dim.html` — high-dimensional intuition.

## 3) How students should use each interactive slide

- **Always click every button / slider at least once** and read the narrative text that updates after interaction.
- If a slide shows multiple scenarios (buttons), treat each scenario as a separate mini-example.
- If a slide has a stepper (Next/Previous), the *state changes* (L1→C2→L2→…); study the transitions, not just the final state.
