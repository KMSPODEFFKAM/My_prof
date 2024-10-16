import matplotlib.pyplot as plt
import numpy as np

def sin(t, f, faza):
    return np.sin(2 * np.pi * f * t + faza)

def rect(t, tau):
    if t > 0 and t < tau:
        return 1
    else:
        return 0

def exp(t, tau):
    return np.exp(-3 * t / tau)

if __name__ == '__main__':
    n = 2048
    ns = int(n / 2)
    end = 10
    start = 0
    time = np.linspace(start, end, n)
    freq = np.linspace(0, 0.5 * n / (end - start), ns)
    signal = [exp(time[i], 4) * sin(time[i], 10, 0) for i in range(n)]
    spectr = 1 / ns * np.fft.fft(signal)[:ns]
    #plt.plot(time, signal)
    plt.plot(freq, abs(spectr))
    plt.show()