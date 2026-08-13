import numpy as np
from scipy.stats import binom
from statsmodels.stats.contingency_tables import mcnemar

y_true    = np.load("Commitment-Mining/y_true-ft-lstm.npy")
y_pred_lr = np.load("Commitment-Mining/test/y_pred-ft-lstm-aug.npy")
y_pred_svm = np.load("Commitment-Mining/test/y_pred-ft-gru-aug.npy")

# For LLM models
# y_pred_lr = np.where(y_pred_lr == "C", 0, 1)
# y_pred_svm = np.where(y_pred_svm == "C", 0, 1)

correct_model_A = (y_pred_lr == y_true)
correct_model_B = (y_pred_svm == y_true)

n00 = np.sum(correct_model_A & correct_model_B)
n01 = np.sum(correct_model_A & ~correct_model_B)
n10 = np.sum(~correct_model_A & correct_model_B)
n11 = np.sum(~correct_model_A & ~correct_model_B)

table = [[n00, n01],
         [n10, n11]]

print("           Model_B correct   Model_B wrong")
print(f"Model_A correct   {n00:5d}       {n01:5d}")
print(f"Model_A wrong     {n10:5d}       {n11:5d}")

discordant = n01 + n10

result_chi = mcnemar(table, exact=False, correction=False)
result_exact = mcnemar(table, exact=True, correction=False)

x = min(n01, n10)
mid_p = result_exact.pvalue - binom.pmf(x, discordant, 0.5)

print(f"\nDiscordant pairs: {discordant}")

print(f"Mid-p value: {mid_p:.6f}")