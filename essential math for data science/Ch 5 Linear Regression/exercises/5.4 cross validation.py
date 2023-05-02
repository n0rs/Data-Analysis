import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import KFold, cross_val_score

df = pd.read_csv("https://raw.githubusercontent.com/thomasnield/machine-learning-demo-data/master/regression/linear_nor\
mal.csv", delimiter=",")

X = df.values[:, :-1]
Y = df.values[:, -1]

kfold = KFold(n_splits=3, random_state=7, shuffle=True)

LR = LinearRegression()
results = cross_val_score(LR, X, Y, cv=kfold)

print(results)

print(f"MSE: mean={results.mean():.3f} (stdev-{results.std():.3f})")

# moderately well