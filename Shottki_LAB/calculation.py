import formul
import parametrs_tranzition

def main(num_tr, f, teta, u, p):
    data = parametrs_tranzition.parametrs_tranzitions(num_tr)

    pc1max = formul.pc1max(teta=teta, Ec=u, Ec0=data.get('e_c0'), rc=data.get('r_s'),
                            ri=data.get('r_i'), Icnas=0.2)
    ic1 = formul.Ic1(teta=teta, Ec=u, Ec0=data.get('e_c0'), rc=data.get('r_s'), ri=data.get('r_i'), Pc1=p)
    uc1 = formul.Uc1gr(teta=teta, Ec=u, Ec0=data.get('e_c0'), rc=data.get('r_s'), ri=data.get('r_i'), Ic1=ic1)
    rek = formul.Rek(Uc1gr=uc1, Ic1=ic1)
    ic0 = formul.Ic0(teta=teta, Ic1=ic1)
    p0 = formul.P0(Ec=u, Ic0=ic0)
    q0 = formul.Q0(teta=teta, Ic0=ic0, ft=data.get('ft'), Csk=data.get('c_sk'), Czk=data.get('c_ek'),
                   Eots=data.get('e_ots'), Ec=u, rc=data.get('r_s'), ri=data.get('r_i'))
    czk1 = formul.Czk1(Czk=data.get('c_ek'), Q0=q0)
    csz1 = formul.Csz1(Csz=data.get('c_sz'), Q0=q0)
    q1 = formul.Q1(Czk=data.get('c_ek'), ft=data.get('ft'), teta=teta, Eots=data.get('e_ots'), Ic1=ic1,
                   Csk=data.get('c_sk'), Uc1=uc1)
    rkan1 = formul.Rkan1(rkan=data.get('r_k'), Q0=q0, Q1=q1, Ic1=ic1, teta=teta, ft=data.get('ft'))
    alfa = formul.alfa(ft=data.get('ft'), teta=teta, Csk=data.get('c_sk'), Rek=rek)
    beta = formul.beta(ft=data.get('ft'), teta=teta, Csz1=csz1, rkan1=rkan1, alfa=alfa)
    c0 = formul.C0(Csz1=csz1, Csk=data.get('c_sk'), Czk1=czk1)
    ksi = formul.ksi(Csz1=csz1, Czk1=czk1, ft=data.get('ft'), teta=teta, C0=c0, Rek=rek)
    roc = formul.roc(ft=data.get('ft'), teta=teta, Li=data.get('l_i'), ksi=ksi,
                     beta=beta, Rek=rek, ri=data.get('r_i'), rc=data.get('r_s'))
    pn = formul.Pn(Ic1=ic1, Rek=rek, rc=data.get('r_s'), ri=data.get('r_i'), roc=roc, f=f, ft=data.get('ft'), teta=teta)
    rn = formul.Rn(Rek=rek, ri=data.get('r_i'), rc=data.get('r_s'),
                   roc=roc, f=f, ft=data.get('ft'), teta=teta, ksi=ksi, beta=beta)
    xn = formul.Xn(Rek=rek, ri=data.get('r_i'), f=f, ft=data.get('ft'), teta=teta, ksi=ksi, beta=beta,
                   Li=data.get('l_i'))
    lvh = formul.Lvh(li=data.get('l_i'), ksi=ksi)
    cvh = formul.Cvh(Czk1=czk1, ksi=ksi, alfa=alfa, ft=data.get('ft'), teta=teta, ri=data.get('r_i'))
    rvh = formul.Rvh(re=data.get('r_z'), ri=data.get('r_i'), rkan1=rkan1,
                     ft=data.get('ft'), teta=teta, alfa=alfa, ksi=ksi, Li=data.get('l_i'))
    xvh = formul.Xvh(f=f, Lvh=lvh, Cvh=cvh)
    ivh = formul.Ivh(ksi=ksi, f=f, ft=data.get('ft'), teta=teta, Ic1=ic1)
    pvh = formul.Pvh(Ivh=ivh, rvh=rvh)
    ku = formul.KU(Pn=pn, Pvh=pvh)
    kpd = formul.KPD(Pn=pn, Pvh=pvh, P0=p0)
    pras = formul.Pras(Pn=pn, Pvh=pvh, P0=p0)
    ez = formul.Ez(Eots=data.get('e_ots'), Ic1=ic1, teta=teta, ft=data.get('ft'), Czk=data.get('c_ek'))
    ezmax = formul.Ezmax(Ez=ez, Ic1=ic1, ft=data.get('ft'), teta=teta, Czk=data.get('c_ek'))

    n = 3

    res = {'Название транзистора': data.get('name'),
           'Частота, ГГц': f,
           'Угол отсечки, град': teta,
           'Напряжение, В': u,
           'Выходная мощность стока, Вт': p,
           'Максимальная мощность на стоке, Вт': round(pc1max, n),
           'Амплитуда первой гармоники тока стока, мА': round(ic1 * 10 ** 3, n),
           'Амплиутда первой гармоники напряжения стока, В': round(uc1, n),
           'Эквивалентное сопротивление, Ом': round(rek, n),
           'Постоянная составляющая тока стока, мА': round(ic0 * 10 ** 3, n),
           'Потребляемая мощность, Вт': round(p0, n),
           'Q0': round(q0, n),
           'Усредненное значение по первой гармонике емкости Сзк1, пФ': round(czk1, n),
           'Усредненное значение по первой гармонике емкости Ссз1, пФ': round(csz1, n),
           'q1': round(q1, n),
           'Сопротивление канала по первой гармоники, Ом': round(rkan1, n),
           'alfa': round(alfa, n),
           'beta': round(beta, n),
           'C0, пФ': round(c0, n),
           'Сопротивление обратной связи, Ом': round(roc, n),
           'Мощность нагрузки, Вт': round(pn, n),
           'Активное сопротивление нагрузки, Ом': round(rn, n),
           'Реактивное сопротивление нагрузки, Ом': round(xn, n),
           'Входная индуктивность, нГн': round(lvh, n),
           'Входная емкасть, пФ': round(cvh * 10 ** 12, n),
           'Активное входное сопротивление, Ом': round(rvh, n),
           'Реактивное входное сопротивление, Ом': round(xvh, n),
           'Амплитуда входного тока, А': round(ivh, n),
           'Выходная мощность, Вт': round(pvh, n),
           'Коэффициент усиления': round(ku, n),
           'КПД': round(kpd, n),
           'Рассеиваемая мощность, Вт': round(pras, n),
           'Напряжение на затворе, В': round(ez, n),
           'Максимальное напряжение на затворе, В': round(ezmax, n)
           }

    return res