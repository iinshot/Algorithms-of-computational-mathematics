import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return x ** 2 + y


def solution(x):
    return 2 * np.exp(x) - x ** 2 - 2 * x - 2


def euler(y_0, x_0, x_end, step):
    N = int((x_end - x_0) / step)
    x_values = np.linspace(x_0, x_end, N + 1)
    y_values = np.zeros(N + 1)
    y_values[0] = y_0
    for n in range(N):
        y_values[n + 1] = y_values[n] + step * f(x_values[n], y_values[n])
    return x_values, y_values


x0 = 0
y0 = 0
x_end = 1
h_values = [0.5, 0.05, 0.01]
for h in h_values:
    x_euler, y_euler = euler(y0, x0, x_end, h)
    plt.plot(x_euler, y_euler, label=f'Approx solution (step = {h})', linestyle='dashed')
x_exact = np.linspace(x0, x_end, 100)
y_exact = solution(x_exact)
plt.plot(x_exact, y_exact, label='Exact solution', color='black')
plt.title('Comparison between exact solution and Euler method, function: x^2 + y', pad=20)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
