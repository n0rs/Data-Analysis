from numpy import array
from numpy.linalg import det

i_hat = array([1, 0])
j_hat = array([2, 2])
transformation = array([i_hat, j_hat]).transpose()

determinant = det(transformation)

print(determinant)