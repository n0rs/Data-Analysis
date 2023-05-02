import pandas as pd
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

df = pd.read_csv("https://raw.githubusercontent.com/thomasnield/machine-learning-demo-data/master/classification/employ\
ee_retention_analysis.csv", delimiter=",")

X = df.values[:, :-1]
Y = df.values[:, -1]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=1/3)

model = MLPClassifier(solver="sgd", learning_rate_init=.05, activation="relu", max_iter=100_000, hidden_layer_sizes=(3, ))

model.fit(X_train, Y_train)

matrix = confusion_matrix(y_true=Y_test, y_pred=model.predict(X_test))

print(matrix)
print(model.coefs_)
print(model.intercepts_)
print(f"Train set score: {model.score(X_train, Y_train)}")
print(f"Test set score: {model.score(X_test, Y_test)}")
