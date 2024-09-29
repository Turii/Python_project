import numpy as np
from itertools import combinations

# Scores from both study groups
scores_a = [68, 77, 82, 85]
scores_b = [53, 64, 71]
all_scores = scores_a + scores_b

# Calculate the observed mean difference
mean_a = np.mean(scores_a)
mean_b = np.mean(scores_b)
observed_diff = abs(mean_a - mean_b)

# Generate all possible combinations of dividing 7 scores into two groups of 4 and 3
combinations_a = list(combinations(all_scores, 4))

# Initialize a list to store differences from all possible combinations
diffs = []

# Calculate mean differences for each possible combination
for comb in combinations_a:
    group_a = comb
    group_b = [score for score in all_scores if score not in group_a]

    mean_a_comb = np.mean(group_a)
    mean_b_comb = np.mean(group_b)
    diff = abs(mean_a_comb - mean_b_comb)
    diffs.append(diff)

# Calculate the p-value as the proportion of combinations with a difference
# as extreme as or more extreme than the observed difference
extreme_count = sum(1 for d in diffs if d >= observed_diff)
p_value = extreme_count / len(diffs)

# Print the results
print(f"Observed Difference: {observed_diff}")
print(f"P-Value: {p_value}")