import numpy as np
from scipy.linalg import solve_triangular


# first: count matrix L, second: decision of Ly = b, third: decision of Ux = y
def Kholesky_solve(matrix_A, b):
    n = len(b)
    for i in range(n):
        matrix_L = np.linalg.cholesky(matrix_A)
        y = solve_triangular(matrix_L, b, lower=True, check_finite=False)
        x = solve_triangular(matrix_L, y, lower=True, trans=1, check_finite=False)
    return x


# checking for symmetry
def is_symmetry(matrix):
    if not all(len(row) == len(matrix) for row in matrix):
        return False
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


def print_system(matrix, b):
    n = len(b)
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
        ans += f' = {b[i]}'
        print(ans)


def input_matrix_vector():
    n = int(input('Enter dimension of system: '))
    matrix = np.zeros((n, n))
    b = np.zeros(n)
    print('Enter factors of matrix: ')
    for i in range(n):
        row = input(f'Row {i + 1}: ').strip().split()
        matrix[i] = list(map(float, row))
    print('Enter factors of vector: ')
    for i in range(n):
        b[i] = float(input(f'b[{i + 1}]: '))
    return matrix, b


matrix, b = input_matrix_vector()
print()
print('A system of linear algebraic equations:')
print_system(matrix, b)
print()
if np.all(np.linalg.eigvals(matrix) > 0):
    if is_symmetry(matrix):
        answer = Kholesky_solve(matrix, b)
        print('Result of system: ', answer)
    else:
        print('Matrix is not symmetric.')
else:
    print('Matrix is not positive.')
print()
print('Discrepancy vector (r = Ax - f):')
r = np.dot(matrix, answer) - b
print(r)
