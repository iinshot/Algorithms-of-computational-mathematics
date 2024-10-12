import numpy as np


# vector "a" - subdiagonal part
# vector "c" - superdiagonal part
# vector "b" - main digonal
# vector "d" - free factors


def tridiagonal(matrix, d):
    n = len(d)
    b = np.zeros(n)
    c = np.zeros(n - 1)
    a = np.zeros(n - 1)
    for i in range(n):
        b[i] = matrix[i, i]
    for i in range(n - 1):
        c[i] = matrix[i, i + 1]
        a[i] = matrix[i + 1, i]
    # direct passage
    for i in range(1, n):
        factor = a[i - 1] / b[i - 1]
        b[i] -= factor * c[i - 1]
        d[i] -= factor * d[i - 1]
    # reverse passage
    x = np.zeros(n)
    x[-1] = d[-1] / b[-1]
    for i in range(n - 2, -1, -1):
        x[i] = (d[i] - c[i] * x[i + 1]) / b[i]
    return x


def print_system(matrix, d):
    n = len(d)
    for i in range(n):
        ans = ''
        for j in range(n):
            if j == 0:
                if matrix[i][j] >= 0 and matrix[i][j] != 1:
                    ans += f'{matrix[i][j]}*x{j}'
                elif matrix[i][j] == 1:
                    ans += f'x{j}'
                else:
                    ans += f'-{abs(matrix[i][j])}*x{j}'
            else:
                if matrix[i][j] >= 0 and matrix[i][j] != 1:
                    ans += f' + {matrix[i][j]}*x{j}'
                elif matrix[i][j] == 1:
                    ans += f' + x{j}'
                else:
                    ans += f' - {abs(matrix[i][j])}*x{j}'
        ans += f' = {d[i]}'
        print(ans)


def input_matrix_vector():
    n = int(input('Enter dimension of system: '))
    matrix = np.zeros((n, n))
    d = np.zeros(n)
    print('Enter factors of matrix: ')
    for i in range(n):
        row = input(f'Row {i + 1}: ').strip().split()
        matrix[i] = list(map(float, row))
    print('Enter factors of vector: ')
    for i in range(n):
        d[i] = float(input(f'd[{i + 1}]: '))
    return matrix, d


matrix, d = input_matrix_vector()
print()
print_system(matrix, d)
answer = tridiagonal(matrix, d)
print()
print('Result of system: ', answer)
print()
r = np.dot(matrix, answer) - d
print('Discrepancy vector (r = Ax - f): ', r)
# a = [0, 1, 1, 1]
# b = [2, 10, -5, 4]
# c = [1, -5, 2, 0]
# d = [-5, -18, -40, -27]

# matrix = [[2, 1, 0, 0],
#           [1, 10, -5, 0],
#           [0, 1, -5, 2],
#           [0, 0, 1, 4]]