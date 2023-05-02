from sympy import *

x = symbols("x")

f = 3 * x ** 3 + 1

slope_at_3 = diff(f, x, 3)

print(slope_at_3)