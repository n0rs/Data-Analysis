import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("https://raw.githubusercontent.com/thomasnield/machine-learning-demo-data/master/regression/linear_nor\
mal.csv", delimiter=",")

X = df.values[:, :-1]

Y = df.values[:, -1]

fit = LinearRegression().fit(X, Y)

m = fit.coef_.flatten()

b = fit.intercept_.flatten()

print(f"m = {m[0]}")
print(f"b = {b[0]}")

plt.plot(X, Y, "o")
plt.plot(X, m*X+b)
plt.show()
