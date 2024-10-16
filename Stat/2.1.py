import matplotlib.pyplot as plt
x = [i for i in range(6)]

res = [0.32 * 10 ** -3, 6.4 * 10 ** -3, 51.2 * 10 ** -3, 0.2048, 0.4096, 0.3277]
f = []
for i in range(6):
    f.append(sum(res[:i + 1]))
plt.plot(x, res)
plt.grid()
plt.xlabel('xi')
plt.ylabel('pi')
plt.show()
plt.step(x, f)
plt.grid()
plt.xlabel('xi')
plt.ylabel('Fi')
plt.show()