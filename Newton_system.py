import numpy as np
import math
import sympy as sp

global_context = {
    'cos': math.cos,
    'sin': math.sin,
    'tg': math.tan,
    'sqrt': math.sqrt,
    'exp': math.exp,
    'log': math.log,
    'pi': math.pi,
    'arctg': math.atan,
}

f1_input = input('Enter the first function: ')
f2_input = input('Enter the second function: ')
x = sp.symbols('x')
y = sp.symbols('y')

functions = {
    'f1': lambda x, y: eval(str(f1_input), {"__builtins__": None, 'x': x, 'y': y}, global_context),
    'f2': lambda x, y: eval(str(f2_input), {"__builtins__": None, 'x': x, 'y': y}, global_context)
}


def jacobian(f1, f2, x, y, h = 1e-7):
    df1_dx = (f1(x + h, y) - f1(x, y)) / h
    df1_dy = (f1(x, y + h) - f1(x, y)) / h
    df2_dx = (f2(x + h, y) - f2(x, y)) / h
    df2_dy = (f2(x, y + h) - f2(x, y)) / h
    return np.array([[df1_dx, df1_dy], [df2_dx, df2_dy]])


def newton_method(f, x0, y0, epsilon = 1e-7, max_iter = 100):
    x_n = np.array([x0, y0])
    for i in range(max_iter):
        F = np.array([f['f1'](x_n[0], x_n[1]), f['f2'](x_n[0], x_n[1])])
        J_matrix = jacobian(f['f1'], f['f2'], x_n[0], x_n[1])
        delta = np.linalg.solve(J_matrix, F)
        x_n = x_n - delta
        if np.linalg.norm(delta) < epsilon:
            return x_n, i + 1
    raise Exception("Метод не сошелся")


x0 = float(input('Enter the first x: '))
y0 = float(input('Enter the first y: '))
result, iters = newton_method(functions, x0, y0)
print(f'Result: {result}, Iterations: {iters}')
