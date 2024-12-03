import numpy as np


def norm(vector):
    sum_squares = 0
    for i in vector:
        sum_squares += i ** 2
    return sum_squares ** 0.5


def normalize(vector):
    normal = norm(vector)
    return vector / normal


def input_matrix():
    n = int(input('Enter dimension of system: '))
    matrix = np.zeros((n, n))
    print('Enter factors of matrix: ')
    for i in range(n):
        row = input(f'Row {i + 1}: ').strip().split()
        matrix[i] = list(map(float, row))
    return matrix


def direct(matrix, epsilon = 1e-6,max_iterations = 1000):
    n = matrix.shape[0]
    b = np.random.rand(n)
    b = b / normalize(b)
    for i in range(max_iterations):
        b_new = matrix @ b
        b_new = normalize(b_new)
        eig = b_new.T @ matrix @ b_new
        if norm(b_new - b) < eps:
            return eig, b_new, i + 1
        b = b_new
    return None


A = input_matrix()
eps = float(input('Enter epsilon: '))
own, own_vec, iters = direct(A, eps)
print()
print(f'Iterations: {iters}')
print(f'Own number: {own}')
print(f'Own vector: {own_vec}')