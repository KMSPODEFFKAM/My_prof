import numpy as np
import requests
import re
import scipy.special

import matplotlib.pyplot as plt

# номер варианта
n = 5

url = 'https://jenyay.net/uploads/Student/Modelling/task_02_01.txt'

rr = requests.get(url = url)

with open('index.html', 'w', encoding="utf-8") as file:
    file.write(rr.text)

with open('index.html', 'r', encoding="utf-8") as file:
    data = file.readlines()


data_1 = data[:]
for i in range(20):
    data_1.remove('\n')

s = re.sub("D|=|fmin|fmax|;|", "", data_1[n-1])
s1 = s.split()

D = float(s1[1])
Fmin = float(s1[2])
Fmax = float(s1[3])

c = 3108
r = D/2

f = np.linspace(Fmin, Fmax, 104)

la = np.zeros(f.size)
k = np.zeros(f.size)
for i in range(f.size):
    la[i] = c/f[i]
    k[i] = (2np.pi) / la[i]

# Ф-ция Бесселя первого рода
def Bess_1(i, x):
    return scipy.special.spherical_jn(i, x)
# Ф-ция Бесселя второго рода
def Bess_2(i, x):
    return scipy.special.spherical_yn(i, x)
# Ф-ция Бесселя третьего рода
def Bess_3(i, x):
    return Bess_1(i, x) + Bess_2(i, x) * 1.0j

def a_n(i, x):
    return Bess_1(i, x) / Bess_3(i, x)

def b_n(i, x):
    return (x * Bess_1(i-1, x) - i * Bess_1(i, x)) / (x * Bess_3(i-1, x) - i * Bess_3(i, x))

sigma = np.zeros(f.size)
sum = np.zeros(f.size, dtype=complex)
for i in range(f.size):
    for n in range(1, 20):
        sum[i] += (-1)n * (n + 0.5) * (b_n(n, k[i]r) - a_n(n, k[i]r))
        sigma[i] = la[i]2/np.pi * np.abs(sum[i])2

plt.grid()
plt.plot(f*10-9, sigma)
plt.xlabel('Частота, ГГц')
plt.ylabel('ЭПР')
plt.savefig('График.jpeg')
plt.show()
