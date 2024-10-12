import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


def interp(f, n):
    x_array = np.linspace (-1,1, n)
    y_array = [f(x) for x in x_array]
    return x_array, y_array


def Lagrange(func, n, x):
    x_array, y_array = interp(func, n)
    result = 0,0
    for i in range(n):
        p = 1.0
        for j in range(n):
            if i != j:
                p *= (x - x_array[j]) / (x_array[i] - x_array[j])
        result += p * y_array[i]
    return result


n = int(input('Enter count of nodes: '))
a = -1
b = 1
func_input = input('Enter function: ')
x = sp.Symbol('x')
func = sp.sympify(func_input)
f = sp.lambdify(x, func, 'numpy')
x_values = np.linspace(a, b, 100)
y_values1 = [f(x) for x in x_values]
y_values2 = [Lagrange(f, n, x) for x in x_values]

fig, ax = plt.subplots()
ax.plot(x_values, y_values1, color='blue', label='Primitive')
ax.plot(x_values, y_values2, label='Lagrange', color='green', linestyle='--')
x_nodes, y_nodes = interp(f, n)
ax.scatter(x_nodes, y_nodes, color='red', label='Set points')
ax.legend()
plt.grid()
plt.show()