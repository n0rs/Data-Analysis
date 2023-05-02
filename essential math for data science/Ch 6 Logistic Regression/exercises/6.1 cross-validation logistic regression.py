import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold, cross_val_score

df = pd.read_csv("https://raw.githubusercontent.com/thomasnield/machine-learning-demo-data/master/classification/light_\
dark_font_training_set.csv", delimiter=",")

X = df.values[:, :-1]
Y = df.values[:, -1]

kfold = KFold(n_splits=3, random_state=7, shuffle=True)
model = LogisticRegression(penalty="none")
results = cross_val_score(model, X, Y, cv=kfold)

print(f"Accuracy mean: {results.mean():.3f} (stdev={results.std():.3f})")