import numpy as np
import matplotlib.pyplot as plt


def seidel(matrix, coefficients, first=None, epsilon = 1e-10, max_iter = 100):
    n = len(coefficients)
    x = np.zeros_like(coefficients) if first is None else first.copy()
    residuals = []
    for it_count in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            sum1 = np.dot(matrix[i, :i], x[:i])
            sum2 = np.dot(matrix[i, i + 1:], x_old[i + 1:])
            x[i] = (coefficients[i] - sum1 - sum2) / matrix[i, i]
        residual = np.dot(matrix, x) - coefficients
        residuals.append(np.linalg.norm(residual, ord=np.inf))
        if np.linalg.norm(x - x_old, ord=np.inf) < epsilon:
            print(f'The discrepancy rate: {residuals[-1]}')
            return x, residuals
    print('Maximum count of iterations have achieved.')
    print(f'The discrepancy rate: {residuals[-1]}')
    return x, residuals


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
result, iterations = seidel(A, b, one, eps)
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