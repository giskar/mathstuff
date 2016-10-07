__author__ = 'Troviln'
# from copy import copy, deepcopy


def make_one(a, b, i):
    d = 1 / a[i][i]
    for k in range(len(a[i])):
        a[i][k] *= d

    b[i] *= d
    return a, b


def make_zero(a, b, i, j):
    n = len(a)
    m = len(a[0])

    for k in range(n):
        if k != i and a[k][j] == 1:
            break

    d = a[i][j]

    for l in range(m):
        a[i][l] -= a[k][l] * d

    b[i] -= b[k] * d

    return a, b


def solve(a, b):
    n = len(a)
    m = len(a[0])
    # a = deepcopy(a)
    # b = copy(b)
    for j in range(m):
        a, b = make_one(a, b, j)
        r = list(range(n))
        r.remove(j)
        for i in r:
            a, b = make_zero(a, b, i, j)

    return a, b


def input_data(argv):
    a = []
    b = []
    b = argv[1].split(' ')

    m = len(b)
    b = [float(b[j]) for j in range(m)]

    t = argv[0].split(' ')
    n = len(t) // m
    k = 0
    for i in range(n):
        a.append([])
        for j in range(m):
            a[i].append(float(t[k]))
            k += 1

    print("Input Data:")
    for i in range(n):
        print(a[i],b[i])
    return a, b

def determinant(matrix, mul):
    width = len(matrix)
    if width == 1:
        return mul * matrix[0][0]
    else:
        sign = -1
        total = 0
        for i in range(width):
            m = []
            for j in range(1, width):
                buff = []
                for k in range(width):
                    if k != i:
                        buff.append(matrix[j][k])
                m.append(buff)
            sign *= -1
            total += mul * determinant(m, sign * matrix[0][i])
        return total




if __name__ == "__main__":
    #data = ['7 8 4 -6 -1 6 -2 -6 2 9 6 -4 5 9 1 1', '-126 -42 -115 -67']
    data = ['-8 5 8 -6 2 7 -8 -1 -5 -4 1 -6 5 -9 -2 8', '-144 25 -21 103']
    a, b = input_data(data)
    matrix = a
    print("Matrix Determinant: \n", determinant(matrix, 1))
    a, b = solve(a, b)
    print("Gauss-Jordan method: \n", b)






