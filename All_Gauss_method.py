import math
import numpy as np
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


def polynom_legendre(n, x):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return ((2 * n - 1) * x * polynom_legendre(n - 1, x) - (n - 1) * polynom_legendre(n - 2, x)) / n

def prime(func, x, h = 1e-6):
    return (func(x + h) - func(x - h)) / (2 * h)


def newton(func, derivative, first, epsilon=1e-8, max_iters=100):
    x = first
    for i in range(max_iters):
        fx = func(x)
        dfx = derivative(x)
        if abs(dfx) < epsilon:
            break
        x_new = x - fx / dfx
        if abs(x_new - x) < epsilon:
            return x_new
        x = x_new
    return x


def get_nodes(n):
    nodes = np.zeros(n)
    first = np.cos(np.pi * (2 * np.arange(1, n + 1) - 1) / (2 * n))

    for i in range(n):
        x = first[i]
        nodes[i] = newton(
            lambda x_i: polynom_legendre(n, x_i),
            lambda x_i: prime(lambda x : polynom_legendre(n,x), x_i), x)
    return nodes


def get_weights(n, nodes):
    weights = np.zeros(n)
    for i in range(n):
      weights[i] = 2 / ((1 - nodes[i] ** 2) * (prime(lambda x: polynom_legendre(n, x), nodes[i]) ** 2))
    return weights


def gauss_quadrature(func, a, b, epsilon=1e-6, max_nodes=20):
    n = 2
    prev_int = 0
    iters = 0
    while n <= max_nodes:
        nodes = get_nodes(n)
        weights = get_weights(n, nodes)
        transform = (b - a) / 2 * nodes + (b + a) / 2
        integral = np.sum(weights * np.vectorize(func)(transform)) * (b - a) / 2
        iters += 1
        if abs(integral - prev_int) < epsilon:
            return integral, iters
        prev_int = integral
        n += 1
    return integral, iters


low = float(input('Enter an lower bound: '))
up = float(input('Enter an upper bound: '))
func = input('Enter function: ')
x = sp.symbols('x')
function = lambda x_val: eval(str(func), {"__builtins__": None, 'x': x_val}, global_context)
result, iters = gauss_quadrature(function, low, up)
print(f'Result: {result}, Iterations: {iters}')