__author__ = 'Troviln'
import numpy as np
#seidel
ITERATION_LIMIT = 100
#https://en.wikipedia.org/wiki/Gauss–Seidel_method
# initialize the matrix
A = np.array([[10, -1, -2, 5],[4, 28, 7, 9],[6, 5, -23, 4],[1, 4, 5, -15]])
# initialize the RHS vector
b = np.array([-99, 0, 67, 58])

# prints the system
print("System:")
for i in range(A.shape[0]):
    row = ["{}*x{}".format(A[i, j], j + 1) for j in range(A.shape[1])]
    print(" + ".join(row), "=", b[i])
print()

x = np.zeros_like(b)
for it_count in range(ITERATION_LIMIT):
    print("Current solution:", x)
    x_new = np.zeros_like(x)

    for i in range(A.shape[0]):
        s1 = np.dot(A[i, :i], x_new[:i])
        s2 = np.dot(A[i, i + 1:], x[i + 1:])
        x_new[i] = (b[i] - s1 - s2) / A[i, i]

    if np.allclose(x, x_new, rtol=1e-8):
        break

    x = x_new

print("Solution:")
print(x)
error = np.dot(A, x) - b
print("Error:")
print(error)