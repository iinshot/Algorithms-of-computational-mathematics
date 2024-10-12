import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

num_nodes = int(input('Enter count of nodes: '))
func_input = input('Enter function: ')
x = sp.Symbol('x')
func = sp.sympify(func_input)
f = sp.lambdify(x, func, 'numpy')
# enter nodes and function
x_nodes = np.linspace(-1, 1, num_nodes + 1)
y_nodes = [f(x) for x in x_nodes]

# dimension of system
N = num_nodes + 1

# systems for getting coefficients
matrix = np.zeros((N, N))
b = np.zeros(N)

for i in range(1, N - 1):
    matrix[i, i - 1] = 1
    matrix[i, i] = 4
    matrix[i, i + 1] = 1
    b[i] = (3 / (x_nodes[i + 1] - x_nodes[i]) * (y_nodes[i + 1] - y_nodes[i]) -
            (3 / (x_nodes[i] - x_nodes[i - 1])) * (y_nodes[i] - y_nodes[i - 1]))

# border
matrix[0, 0] = 1
matrix[N - 1, N - 1] = 1
b[0] = 0
b[N - 1] = 0

# solve of system
c = np.linalg.solve(matrix, b)

# solve of a[i], b[i], d[i]
coefficients = []
for i in range(num_nodes):
    a_i = y_nodes[i]
    h_i = x_nodes[i + 1] - x_nodes[i]
    b_i = (y_nodes[i + 1] - y_nodes[i]) / h_i - h_i * (2 * c[i] + c[i + 1]) / 3
    d_i = (c[i + 1] - c[i]) / (3 * h_i)
    coefficients.append((a_i, b_i, c[i], d_i))


# for estimate function
def spline(x_val):
    for item in range(num_nodes):
        if x_nodes[item] <= x_val <= x_nodes[item + 1]:
            a_el, b_el, c_el, d_el = coefficients[item]
            diff_x = x_val - x_nodes[item]
            return a_el + b_el * diff_x + c_el * diff_x ** 2 + d_el * diff_x ** 3
    return None


x_spline = np.linspace(-1, 1, 100)
y_spline = [spline(x) for x in x_spline]
y_original = [f(x) for x in x_spline]

plt.plot(x_spline, y_spline, label='Cubic spline', color='blue')
plt.scatter(x_nodes, y_nodes, color='red', label='Set points')
plt.plot(x_spline, y_original, label='Primitive', color='green', linestyle='--')
plt.title('Cubic Spline')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()