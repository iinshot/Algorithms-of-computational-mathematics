import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    return x ** 2 + y


def solution(x):
    return 2 * np.exp(x) - x ** 2 - 2 * x - 2


def runge_kutta_4(y_0, x_0, x_end, step):
    N = int((x_end - x_0) / step)
    x_values = np.linspace(x_0, x_end, N + 1)
    y_values = np.zeros(N + 1)
    y_values[0] = y_0
    for n in range(N):
        k1 = f(x_values[n], y_values[n])
        k2 = f(x_values[n] + step / 2, y_values[n] + step * k1 / 2)
        k3 = f(x_values[n] + step / 2, y_values[n] + step * k2 / 2)
        k4 = f(x_values[n] + step, y_values[n] + step * k3)
        y_values[n + 1] = y_values[n] + step * (k1 + 2 * k2 + 3 * k3 + k4) / 6
    return x_values, y_values


x0 = 0
y0 = 0
x_end = 1
h_values = [0.1, 0.05, 0.01]
for h in h_values:
    x_rk, y_rk = runge_kutta_4(y0, x0, x_end, h)
    plt.plot(x_rk, y_rk, label=f'Approx solution (step = {h})', linestyle='dashed')
x_exact = np.linspace(x0, x_end, 100)
y_exact = solution(x_exact)
plt.plot(x_exact, y_exact, label='Exact solution', color='black')
plt.title('Comparison between exact solution and Runge-Kutt 4-th order method, function: x^2 + y', pad=20)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid()
plt.show()
