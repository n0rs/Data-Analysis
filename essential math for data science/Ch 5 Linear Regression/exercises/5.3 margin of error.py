import pandas as pd
from scipy.stats import t
from math import sqrt


points = list(pd.read_csv("https://raw.githubusercontent.com/thomasnield/machine-learning-demo-data/master/regression/linear\
_normal.csv", delimiter=",").itertuples())

n = len(points)


x_0 = 50
x_mean = sum(p.x for p in points) / n

m = 1.75919315
b = 4.69359655

t_value = t(n - 2).ppf(.975)

s_e = sqrt(sum((p.y - (m * p.x + b)) ** 2 for p in points) / (n - 2))

margin_error = t_value * s_e * sqrt(1 + (1 / n) + (n * (x_0 + x_mean) ** 2) / (n * sum(p.x ** 2 for p in points) - sum(p.x for p in points) ** 2))

y_predict = m * x_0 + b

prediction_interval1 = y_predict + margin_error
prediction_interval2 = y_predict - margin_error

print(f"For x = 50 the 95% prediction interval is between {prediction_interval2} and {prediction_interval1}")

