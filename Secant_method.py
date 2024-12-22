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


func = input('Enter function: ')
x = sp.symbols('x')
function1 = lambda x: eval(func, {"__builtins__": None, 'x': x}, global_context)
x0 = 1
x1 = 2
max_iter = 100
epsilon = 1e-6
flag = False
iters = 0
for i in range(max_iter):
    x2 = x1 - function1(x1) * (x0 - x1) / (function1(x0) - function1(x1))
    if abs(function1(x2)) < epsilon:
        solution = x2
        flag = True
        iters = i
        break
    x0, x1 = x1, x2
if not flag:
    print('Maximum count of iterations have achieved.')
if solution is not None:
    print(f'x = {solution}, iterations: {iters}')