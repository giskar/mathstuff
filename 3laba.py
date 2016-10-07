__author__ = 'Troviln'
import numpy as np

def seidel(m, b, eps):
    n = len(m)
    r = range(n)
    x = [0 for i in r]
    conv = False
    while not conv:
        p = x.copy()
        for i in r:
            var = sum(m[i][j] * x[j] for j in range(i))
            var += sum(m[i][j] * p[j] for j in range(i+1, n))
            x[i] = (b[i] - var) / m[i][i]

        conv = sum((x[i]-p[i])**2 for i in r) < eps
        print(x)
    return x

# initialize the matrix
m = [[10, -1, -2, 5],[4, 28, 7, 9],[6, 5, -23, 4],[1, 4, 5, -15]]
# initialize the RHS vector
b = [-99, 0, 67, 58]

eps = 0.01

print(seidel(m, b, eps))