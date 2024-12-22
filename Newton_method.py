def f(x):
    return x ** 3 - 2 * x - 5


def prime(x):
    return 3 * x ** 2 - 2


x0 = 10
max_iter = 100
epsilon = 1e-6
flag = False
iters = 0
for i in range(max_iter):
    f_x0 = f(x0)
    f_prime_x0 = prime(x0)
    if f_prime_x0 == 0:
        print('Prime is zero')
    x1 = x0 - f_x0 / f_prime_x0
    if abs(f(x1)) < epsilon:
        solution = x1
        flag = True
        iters = i
        break
    x0 = x1
if not flag:
    print('Maximum count of iterations have achieved.')
if solution is not None:
    print(f'x = {solution}, iterations: {iters}')