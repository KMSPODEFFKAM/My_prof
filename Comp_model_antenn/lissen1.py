import matplotlib.pyplot as plt
import numpy as np

'''
#1 Задание. Построить график ДН АР
'''

def func_ras1(teta):
    return 1

def func_1(N, f0, func_ras):
    l = 30 / f0
    dx = l / 2
    L = dx * (N - 1)
    x_i = [i * dx - L/2 for i in range(N)]

    f_0 = np.zeros(720, ctype=complex)
    teta = [i * 0.5 for i in range(720)]

    for i in range(N):
        for j in range(720):
            f_0[j] += func_ras(teta[j]) * np.exp(1j * 2 * np.pi / l * x_i[i] * np.sin(teta[j]))
    return f_0
if __name__ == '__main__':
    print(func_1(16, 3, func_ras1))