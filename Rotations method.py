import numpy as np


def matrix_rotation(ksi):
    return np.array([[np.cos(ksi), -np.sin(ksi)], [np.sin(ksi), np.cos(ksi)]])


def jacobi_rotation(matrix, epsilon = 1e-10, max_iterations = 100):
    n = len(matrix)
    matrix_D = np.copy(matrix)
    matrix_P = np.identity(n)
    for z in range(max_iterations):
        max_diagonal = 0
        p, q = 0, 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if abs(matrix_D[i, j]) > max_diagonal:
                    max_diagonal = abs(matrix_D[i, j])
                    p, q = i, j
        if max_diagonal < epsilon:
            eig = np.diag(matrix_D)
            return eig, z + 1
        ksi = 0.5 * np.arctan2(2 * matrix_D[p, q], matrix_D[p, p] - matrix_D[q, q])
        c = np.cos(ksi)
        s = np.sin(ksi)
        matrix_R = np.identity(n)
        matrix_R[p, p] = matrix_R[q, q] = c
        matrix_R[p, q] = -s
        matrix_R[q, p] = s
        matrix_D = matrix_R.T @ matrix_D @ matrix_R
        matrix_P = matrix_P @ matrix_R
    return None


def input_matrix():
    n = int(input('Enter dimension of system: '))
    matrix = np.zeros((n, n))
    print('Enter factors of matrix: ')
    for i in range(n):
        row = input(f'Row {i + 1}: ').strip().split()
        matrix[i] = list(map(float, row))
    return matrix


A = input_matrix()
own, iters = jacobi_rotation(A)
print(f"Own values: {own}")
print(f"Iterations: {iters}")