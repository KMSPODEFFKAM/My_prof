import matplotlib.pyplot as plt
import numpy as np

class RadarTaget:

    def __init__(self, sig: float, f: float):

        self.sig = sig
        self.c = 3e8
        self.w0 = 2 * np.pi * f
        self.la = self.c / f

    def otr_signal(self, p0: float, sig: float, g1=1.0, g2=1.0):

        res1 = np.sqrt((2 * p0 * self.la ** 2 * g1 * g2 * sig) / (4 * np.pi) ** 3)


    def func2(self):
        pass