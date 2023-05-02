import pandas as pd
from scipy.stats import t
from math import sqrt

df = pd.read_csv("https://raw.githubusercontent.com/thomasnield/machine-learning-demo-data/master/regression/linear_nor\
mal.csv", delimiter=",")

correlation = df.corr(method="pearson")
print(correlation)

n = df.shape[0]
print(n)

lower_cv = t(n - 1).ppf(.025)
upper_cv = t(n - 1).ppf(.975)

r = correlation["y"]["x"]

test_value = r / sqrt((1 - r ** 2) / (n - 2))

print(f"Test value: {test_value}")
print(f"Critical range: {lower_cv}, {upper_cv}")

if test_value < lower_cv or test_value > upper_cv:
    print("correlation proven, reject H0")
else:
    print("correlation not proven, keep H0")

if test_value > 0:
    p_value = 1.0 - t(n - 1).cdf(test_value)
else:
    p_value = t(n - 1).cdf(test_value)

p_value = p_value * 2

print(f"P-value: {p_value}")