import numpy as np


# function for gauss method
def gauss(matrix, b):
    n = len(b)
    for i in range(n):
        # find main element
        max_row_index = np.argmax(np.abs(matrix[i:, i])) + i
        matrix[[i, max_row_index]] = matrix[[max_row_index, i]]
        # change rows
        b[i], b[max_row_index] = b[max_row_index], b[i]
        for j in range(i + 1, n):
            index = matrix[j][i] / matrix[i][i]
            matrix[j] = matrix[j] - index * matrix[i]
            b[j] = b[j] - index * b[i]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - np.dot(matrix[i], x)) / matrix[i][i]
    return x


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
print_system(matrix, b)
print()
answer = gauss(matrix, b)
print("Answer of system:", answer)
print()
r = np.dot(matrix, answer) - b
print('Discrepancy vector (r = Ax - f):', r)