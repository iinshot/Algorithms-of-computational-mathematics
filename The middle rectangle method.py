import math
import numpy as np
import matplotlib.pyplot as plt
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

def right_method(func, lower, upper, epsilon):
    n = 1
    h = (upper - lower) / n
    prev_integral = 0
    while True:
        integral = 0
        for i in range(n):
            integral += func(upper - i * h)
        integral *= h
        if abs(integral - prev_integral) < epsilon:
            break
        prev_integral = integral
        n *= 2
        h = (upper - lower) / n
    return integral


def left_method(func, lower, upper, epsilon):
    n = 1
    h = (upper - lower) / n
    prev_integral = 0
    while True:
        integral = 0
        for i in range(n):
            integral += func(lower + i * h)
        integral *= h
        if abs(integral - prev_integral) < epsilon:
            break
        prev_integral = integral
        n *= 2
        h = (upper - lower) / n
    return int(n), integral


print('Enter an lower bound')
low = float(input())
print('Enter an upper bound')
up = float(input())
print('Enter an epsilon')
epsilon = float(input())
print('Enter function')
func = input()
x = sp.symbols('x')
try:
    function1 = lambda x: eval(func, {"__builtins__": None, 'x': x}, global_context)
    num_partitions, result1 = left_method(function1, low, up, epsilon)
    result2 = right_method(function1, low, up, epsilon)
    result = (result1 + result2) / 2
    num_partition, result = left_method(function1, low, up, epsilon)
    print()
    print(f'Result of integral: {result}')
    round_result = round(result, 2)
    function = sp.sympify(func)
    x_values = np.linspace(low, up, num_partition)
    y_values = [function.subs(x, val) for val in x_values]
    plt.plot(x_values, y_values, label=str(func))
    plt.title(f'F({int(up)}) - F({int(low)}) ≈ {round_result},'
              f' F(x) - primitive, ε = {epsilon}, partitions = {num_partition}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5, ls='--')
    plt.axvline(0, color='black', linewidth=0.5, ls='--')
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()
except Exception as e:
    print(f'Error {e}')