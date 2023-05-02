from numpy import array
from numpy.linalg import det

m = array([
    [2, 1],
    [6, 3]
])

determinant = det(m)

print(determinant)
if determinant == 0:
    print("The matrix is linearly dependent")
else:
    print("The matrix is not linearly dependent")