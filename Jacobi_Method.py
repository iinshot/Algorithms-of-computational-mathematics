import numpy as np
import matplotlib.pyplot as plt


def jacobi(matrix, coefficients, first, epsilon, max_iter = 100):
    n = len(coefficients)
    x = first.copy()
    residuals = []
    for iter_count in range(max_iter):
        x_new = np.zeros_like(x)
        for i in range(n):
            sum_j = sum(matrix[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (coefficients[i] - sum_j) / matrix[i][i]
        residual = np.dot(matrix, x_new) - coefficients
        residuals.append(np.linalg.norm(residual))
        if np.linalg.norm(x_new - x) < epsilon:
            print(f'The discrepancy rate: {residuals[-1]}')
            return x_new, residuals
        x = x_new
    print('Maximum count of iterations have achieved.')
    print(f'The discrepancy rate: {residuals[-1]}')
    return x_new, residuals


def print_system(matrix, coefficients):
    print('Your system:')
    n = len(coefficients)
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
        ans += f' = {coefficients[i]}'
        print(ans)


def input_matrix_vector():
    n = int(input('Enter dimension of system: '))
    matrix = np.zeros((n, n))
    coefficients = np.zeros(n)
    print('Enter factors of matrix: ')
    for i in range(n):
        row = input(f'Row {i + 1}: ').strip().split()
        matrix[i] = list(map(float, row))
    print('Enter factors of vector: ')
    for i in range(n):
        coefficients[i] = float(input(f'b[{i + 1}]: '))
    return matrix, coefficients


A, b = input_matrix_vector()
eps = float(input('Enter epsilon: '))
print()
print_system(A, b)
print()
one = np.zeros_like(b)
result, iterations = jacobi(A, b, one, eps)
print(f'Number of iterations: {len(iterations)}')
print(f'Answer: {result}')

plt.plot(iterations, linestyle='--')
plt.yscale('log')
plt.title('Dependence of the discrepancy rate on the iteration number')
plt.xlabel('Number of iteration')
plt.ylabel('Discrepancy rate')
plt.grid()
plt.show()

# A = np.array([[4, -1, 0, 0],
#               [-1, 4, -1, 0],
#               [0, -1, 4, -1],
#               [0, 0, -1, 3]], dtype=float)
# b = np.array([15, 10, 10, 10])