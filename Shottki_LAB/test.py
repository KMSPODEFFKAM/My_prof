import matplotlib.pyplot as plt
import formul
import numpy as np

fig, ax = plt.subplots()
teta = np.linspace(0, 180, 100)
a0 = [formul.a0(i) for i in teta]
a1 = [formul.a1(i) for i in teta]
ax.plot(teta, a0, label='a₀(θ)')
ax.plot(teta, a1, label='a₁(θ)')
ax.grid()
ax.set_title('Коэффициенты разложения косинусоидального импульса тока')
ax.set_xlim(0, 180)
ax.set_ylim(0)
ax.set_xlabel('θ, град')
ax.set_ylabel('Коэффициент, б/р')
ax.legend()
plt.show()