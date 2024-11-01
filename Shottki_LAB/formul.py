import math
import numpy as np

def a0(teta):
    teta = teta * math.pi / 180
    if teta == 0:
        return 0
    else:
        return (math.sin(teta) - teta * math.cos(teta)) / (math.pi * (1 - math.cos(teta)))

def a1(teta):
    teta = teta * math.pi / 180
    if teta == 0:
        return 0
    else:
        return (teta - math.sin(teta) * math.cos(teta)) / (math.pi * (1 - math.cos(teta)))

def g0(teta):
    teta = teta * math.pi / 180
    return 1 / math.pi * (math.sin(teta) - teta * math.cos(teta))

def g1(teta):
    teta = teta * math.pi / 180
    return 1 / math.pi * (teta - math.sin(teta) * math.cos(teta))

def g_n(n, teta):
    teta = teta * math.pi / 180
    return 2 / math.pi * (math.sin(n * teta) * math.cos(teta) - n * math.cos(n * teta) * math.sin(teta)) / (
                n * (n ** 2 - 1))

def teta_formul(E: float, Us: float, Uip: float) -> float:
    '''
    :param E: напряжение отсечки в бд 4 столбец
    :param Us: напряжение смещения
    :param Uip: источник питания
    :return: угол отсечки
    '''
    return np.arccos((E - Us) / Uip) * 180 / math.pi

def pc1max(teta: float, Ec: float, Ec0: float, rc: float, ri: float, Icnas: float):
    '''Максимальная мощность стока транзистора'''
    try:
        return 0.5 * a1(teta) * Icnas * (Ec - Ec0 - a0(teta) * Icnas * (rc + ri))
    except TypeError:
        return None

def Icnas(Ic1, teta):
    '''Ток насыщения стока'''
    try:
        return Ic1 / a1(teta)
    except TypeError:
        return None

def Ic1(teta, Ec, Ec0, rc, ri, Pc1):
    '''Амплитудла первой гармоники тока стока'''
    try:
        res1 = 0.5 * a1(teta) / a0(teta) * (Ec - Ec0) / (rc + ri)
        res2 = 2 * a1(teta) / a0(teta) * Pc1 / (rc + ri)
        return res1 - (res1 ** 2 - res2) ** .5
    except ZeroDivisionError:
        return None

def Uc1gr(teta, Ec, Ec0, rc, ri, Ic1):
    '''Амплитуда напряжения первой гармоники'''
    try:
        return Ec - Ec0 - a0(teta) / a1(teta) * Ic1 * (rc + ri)
    except ZeroDivisionError:
        return None

def Rek(Uc1gr, Ic1):
    '''Эквивалентное сопротивление нагрузки'''
    try:
        return Uc1gr / Ic1
    except ZeroDivisionError:
        return None

def Ic0(teta, Ic1):
    '''Постоянная составляющая тока стока'''
    try:
        return a0(teta) / a1(teta) * Ic1
    except ZeroDivisionError:
        return None

def P0(Ec, Ic0):
    '''Мощность ИП'''
    try:
        return Ec * Ic0
    except TypeError:
        return None

def Czk1(Czk, Q0):
    '''Усреднение по первой гармоники'''
    try:
        return Czk / (1 - Q0)
    except TypeError:
        return None

def Csz1(Csz, Q0):
    try:
        return Csz * (1 - Q0)
    except TypeError:
        return None

def Q0(teta, Ic0, ft, Csk, Czk, Eots, Ec, rc, ri):
    try:
        Csk *= 10 ** -12
        Czk *= 10 ** -12
        ft *= 10 ** 9

        res1 = Ic0 * math.cos(teta * math.pi / 180) / (2 * math.pi * ft * g0(teta))
        res2 = Csk * (Ec - Ic0 * (rc + ri))
        res3 = 2 * Czk * (0.8 + abs(Eots))
        return -(res1 + res2) / res3
    except TypeError:
        return None

def Rkan1(rkan, Q0, Q1, Ic1, teta, ft):
    try:
        ft *= 10 ** 9

        res1 = (1 - Q0) ** 2
        res2 = 0.25 * Q1 ** 2
        res3 = 3 * Ic1 * (g0(180 - teta) - 0.5 * g_n(2, 180 - teta))
        res4 = 2 * math.pi * ft * g1(teta)
        return rkan * (res1 + res2 - res3 / res4)
    except TypeError:
        return None

def Q1(Czk, ft, teta, Eots, Ic1, Csk, Uc1):
    try:
        Czk *= 10 ** -12
        Csk *= 10 ** -12
        ft *= 10 ** 9

        E0 = 0.8 + abs(Eots)
        return 1 / (2 * Czk * E0) * (Ic1 / (2 * math.pi * ft * g1(teta)) + Csk * Uc1)
    except TypeError:
        return None

def alfa(ft, teta, Csk, Rek):
    try:
        ft *= 10 ** 9
        Csk *= 10 ** -12
        return 1 + 2 * math.pi * ft * g1(teta) * Csk * Rek
    except TypeError:
        return None

def beta(ft, teta, Csz1, rkan1, alfa):
    try:
        ft *= 10 ** 9
        Csz1 *= 10 ** -12
        return 2 * math.pi * ft * g1(teta) * Csz1 * rkan1 * alfa
    except TypeError:
        return None

def C0(Csz1, Csk, Czk1):
    try:
        return Csz1 + Csk * (1 + Csz1 / Czk1)
    except TypeError:
        return None

def ksi(Csz1, Czk1, ft, teta, C0, Rek):
    try:
        Csz1 *= 10 ** -12
        Czk1 *= 10 ** -12
        ft *= 10 ** 9
        C0 *= 10 ** -12
        return 1 + Csz1 / Czk1 + 2 * math.pi * ft * g1(teta) * C0 * Rek
    except TypeError:
        return None

def roc(ft, teta, Li, ksi, beta, Rek, ri, rc):
    try:
        ft *= 10 ** 9
        Li *= 10 ** -9
        return 2 * math.pi * ft * g1(teta) * Li * ksi + beta * (Rek - ri - 2 * rc) + ri * (ksi - 1)\
               - rc * (ksi - 1) ** 2
    except TypeError:
        return None

def Pn(Ic1, Rek, rc, ri, roc, f, ft, teta):
    try:
        rez1 = f / (ft * g1(teta))
        rez2 = rez1 ** 2 * roc
        rez3 = Rek - rc - ri + rez2
        return 0.5 * Ic1 ** 2 * rez3
    except TypeError:
        return None

def Rn(Rek, ri, rc, roc, f, ft, teta, ksi, beta):
    try:
        f *= 10 ** 9
        ft *= 10 ** 9

        res1 = Rek - ri - rc
        res2 = (f / (ft * g1(teta))) ** 2
        res3 = (ksi - 1) ** 2 + 2 * beta
        return (res1 + res2 * roc) / (1 + res2 * res3)
    except TypeError:
        return None

def Xn(Rek, ri, f, ft, teta, ksi, beta, Li):
    try:
        f *= 10 ** 9
        ft *= 10 ** 9
        Li *= 10 ** -9

        res1 = f / (ft * g1(teta))
        res2 = (ksi - 1) ** 2 + 2 * beta
        res3 = 2 * math.pi * ft * g1(teta) * Li
        res4 = Rek - ri
        res5 = ksi - beta - 1
        res6 = res1 / (1 + res1 ** 2 * res2)
        res7 = res4 * ksi - Rek - res3 + res1 ** 2 * (res3 * res5 - ri * beta)
        return res6 * res7
    except TypeError:
        return None

def Lvh(li, ksi):
    try:
        return li / ksi
    except TypeError:
        return None

def Cvh(Czk1, ksi, alfa, ft, teta, ri):
    try:
        Czk1 *= 10 ** -12
        ft *= 10 ** 9
        return ksi * Czk1 / (alfa + 2 * math.pi * ft * g1(teta) * Czk1 * ri)
    except TypeError:
        return None

def Rvh(re, ri, rkan1, ft, teta, alfa, ksi, Li):
    try:
        Li *= 10 ** -9
        ft *= 10 ** 9
        res1 = 2 * math.pi * ft * g1(teta) * Li
        return re + (res1 + ri + alfa * rkan1) / ksi
    except TypeError:
        return None

def Xvh(f, Lvh, Cvh):
    try:
        f *= 10 ** 9
        Lvh *= 10 ** -9
        return 2 * math.pi * f * Lvh - 1 / (2 * math.pi * f * Cvh)
    except TypeError:
        return None
    except ZeroDivisionError:
        return None

def Ivh(ksi, f, ft, teta, Ic1):
    try:
        return ksi * f / (ft * g1(teta)) * Ic1
    except TypeError:
        return None

def Pvh(Ivh, rvh):
    try:
        return 0.5 * Ivh ** 2 * rvh
    except TypeError:
        return None

def KU(Pn, Pvh):
    try:
        return Pn / Pvh
    except TypeError:
        return None
    except ZeroDivisionError:
        return None

def KPD(Pn, Pvh, P0):
    try:
        return (Pn - Pvh) / P0
    except:
        return None

def Pras(Pn, Pvh, P0):
    try:
        return P0 - Pn + Pvh
    except TypeError:
        return None

def Ez(Eots, Ic1, teta, ft, Czk):
    try:
        ft *= 10 ** 9
        Czk *= 10 ** -12
        return Eots - Ic1 * math.cos(teta * math.pi / 180) / (2 * math.pi * ft * g1(teta) * Czk)
    except TypeError:
        return None

def Ezmax(Ez, Ic1, ft, teta, Czk):
    try:
        ft *= 10 ** 9
        Czk *= 10 ** -12
        return Ez + Ic1 / (2 * math.pi * ft * g1(teta) * Czk)
    except TypeError:
        return None