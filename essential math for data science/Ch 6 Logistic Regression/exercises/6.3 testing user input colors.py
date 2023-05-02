import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv("https://raw.githubusercontent.com/thomasnield/machine-learning-demo-data/master/classification/light_\
dark_font_training_set.csv", delimiter=",")

X = df.values[:, :-1]
Y = df.values[:, -1]

model = LogisticRegression(solver="liblinear")
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.33, random_state=10)
model.fit(X_train, Y_train)
prediction = model.predict(X_test)

# Test a prediction
while True:
    n = input("Input a color {red}, {green}, {blue}: ")
    (r, g, b) = n.split(",")
    x = model.predict(np.array([[int(r), int(g), int(b)]]))
    if model.predict(np.array([[int(r), int(g), int(b)]]))[0] == 0.0:
        print("Use a light font")
    else:
        print("Use a dark font")
