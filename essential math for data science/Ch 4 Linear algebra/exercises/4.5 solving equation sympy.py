from sympy import *

A = Matrix([
    [3, 1, 0],
    [2, 4, 1],
    [3, 1, 8]
])

B = Matrix([
    54,
    12,
    6
])


X = A.inv() * B


print(X)