import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("https://raw.githubusercontent.com/thomasnield/machine-learning-demo-data/master/regression/linear_nor\
mal.csv", delimiter=",")

X = df.values[:, :-1]
Y = df.values[:, -1]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=7, train_size=1/3)

LR = LinearRegression()
fit = LR.fit(X_train, Y_train)

result = fit.score(X_test, Y_test)

print(score)
