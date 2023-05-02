import numpy as np
import pandas as pd
import stemgraphic
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.distributions.empirical_distribution import ECDF


# reading data (Iris data set)
data = "C:/Users/n0rs9/PycharmProjects/pythonProject/Data Mining Tan/Chapter 2 Data Visualization/iris.csv"
df = pd.read_csv(data, sep=",")

print(df.describe())

# stem and leaf plot
"""fig, ax = stemgraphic.stem_graphic(df["sepal length"])
plt.show()

# Histograms
fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=4)
ax0.hist(df["sepal length"], bins=20)
ax0.set_xlabel("sepal length")

ax1.hist(df["sepal width"], bins=20)
ax1.set_xlabel("sepal width")

ax2.hist(df["petal length"], bins=20)
ax2.set_xlabel("petal length")

ax3.hist(df["petal width"], bins=20)
ax3.set_xlabel("petal width")

ax0.set_ylabel("Count")
plt.show()

# 2D Histogram
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
hist, xedges, yedges = np.histogram2d(df["petal width"], df["petal length"], bins=(3, 3))
xpos, ypos = np.meshgrid(xedges[:-1]+xedges[1:], yedges[:-1]+yedges[1:]) - (xedges[1]-xedges[0])

xpos = xpos.flatten()*1./2
ypos = ypos.flatten()*1./2
zpos = np.zeros_like(xpos)

dx = xedges[1] - xedges[0]
dy = yedges[1] - yedges[0]
dz = hist.flatten()

max_height = np.max(dz)
min_height = np.min(dz)

ax.bar3d(xpos, ypos, zpos, dx, dy, dz)
plt.ylabel("petal length")
plt.xlabel("petal width")
plt.xlim(2.5, 0)
plt.show()

# boxplot
fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=4)
ax0.boxplot(df["sepal length"])
ax0.set_ylim(0, 8)
ax0.set_ylabel("Values [cm]")
ax0.set_xlabel("sepal length")

ax1.boxplot(df["sepal width"])
ax1.set_xlabel("sepal width")
ax1.set_ylim(0, 8)

ax2.boxplot(df["petal length"])
ax2.set_xlabel("petal length")
ax2.set_ylim(0, 8)

ax3.boxplot(df["petal width"])
ax3.set_xlabel("petal width")
ax3.set_ylim(0, 8)

plt.show()

# boxplot of different classes
# setosa
setosa_sl = df[df["class"] == "Iris-setosa"]["sepal length"]
setosa_sw = df[df["class"] == "Iris-setosa"]["sepal width"]
setosa_pl = df[df["class"] == "Iris-setosa"]["petal length"]
setosa_pw = df[df["class"] == "Iris-setosa"]["petal width"]

# versicolour
versicolor_sl = df[df["class"] == "Iris-versicolor"]["sepal length"]
versicolor_sw = df[df["class"] == "Iris-versicolor"]["sepal width"]
versicolor_pl = df[df["class"] == "Iris-versicolor"]["petal length"]
versicolor_pw = df[df["class"] == "Iris-versicolor"]["petal width"]

# virginica
virginica_sl = df[df["class"] == "Iris-virginica"]["sepal length"]
virginica_sw = df[df["class"] == "Iris-virginica"]["sepal width"]
virginica_pl = df[df["class"] == "Iris-virginica"]["petal length"]
virginica_pw = df[df["class"] == "Iris-virginica"]["petal width"]

fig, (ax0, ax1, ax2) = plt.subplots(nrows=1, ncols=3)
ax0.boxplot([setosa_sl, setosa_sw, setosa_pl, setosa_pw])
ax0.set_ylabel("Values [cm]")
ax0.set_xlabel("Setosa")

ax1.boxplot([versicolor_sl, versicolor_sw, versicolor_pl, versicolor_pw])
ax1.set_xlabel("Versicolour")

ax2.boxplot([virginica_sl, virginica_sw, virginica_pl, virginica_pw])
ax2.set_xlabel("Virginica")

plt.show()

# Pie chart
plt.pie(df["class"].value_counts(), labels=["setosa", "versicolor", "virginica"])
plt.show()

# empirical cumulative distribution function (ECDF)
e_sl = ECDF(df["sepal length"])
e_sw = ECDF(df["sepal width"])
e_pl = ECDF(df["petal length"])
e_pw = ECDF(df["petal width"])

fig, ((ax0, ax1), (ax2, ax3)) = plt.subplots(nrows=2, ncols=2)

ax0.plot(e_sl.x, e_sl.y)
ax1.plot(e_sw.x, e_sl.y)
ax2.plot(e_pl.x, e_pl.y)
ax3.plot(e_pw.x, e_pw.y)

plt.show()

# percentile plot
p_sl = [np.percentile(df["sepal length"], i) for i in range(100)]
p_sw = [np.percentile(df["sepal width"], j) for j in range(100)]
p_pl = [np.percentile(df["petal length"], k) for k in range(100)]
p_pw = [np.percentile(df["petal width"], l) for l in range(100)]
plt.plot(p_sl, label="sepal length")
plt.plot(p_sw, label="sepal width")
plt.plot(p_pl, label="petal length")
plt.plot(p_pw, label="petal width")
plt.legend()
plt.show()

# 3D scatter plot
fig = plt.figure()
ax = fig.add_subplot(projection="3d")
ax.scatter(df["sepal width"], df["sepal length"], df["petal width"])
ax.set_xlabel("sepal width")
ax.set_ylabel("sepal length")
ax.set_zlabel("petal width")
plt.show()"""

