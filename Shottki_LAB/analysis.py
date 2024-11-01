import numpy as np
import seaborn
import matplotlib.pyplot as plt
import formul
import parametrs_tranzition

class Analys:

    def formul_dict(self, num_tr, f, teta, u, p):
        self.data = parametrs_tranzition.parametrs_tranzitions(num_tr)

        pc1max = formul.pc1max(teta=teta, Ec=u, Ec0=self.data.get('e_c0'), rc=self.data.get('r_s'),
                               ri=self.data.get('r_i'), Icnas=self.data.get('icnas'))
        ic1 = formul.Ic1(teta=teta, Ec=u, Ec0=self.data.get('e_c0'), rc=self.data.get('r_s'), ri=self.data.get('r_i'), Pc1=p)
        uc1 = formul.Uc1gr(teta=teta, Ec=u, Ec0=self.data.get('e_c0'), rc=self.data.get('r_s'), ri=self.data.get('r_i'), Ic1=ic1)
        rek = formul.Rek(Uc1gr=uc1, Ic1=ic1)
        ic0 = formul.Ic0(teta=teta, Ic1=ic1)
        p0 = formul.P0(Ec=u, Ic0=ic0)
        q0 = formul.Q0(teta=teta, Ic0=ic0, ft=self.data.get('ft'), Csk=self.data.get('c_sk'), Czk=self.data.get('c_ek'),
                       Eots=self.data.get('e_ots'), Ec=u, rc=self.data.get('r_s'), ri=self.data.get('r_i'))
        czk1 = formul.Czk1(Czk=self.data.get('c_ek'), Q0=q0)
        csz1 = formul.Csz1(Csz=self.data.get('c_sz'), Q0=q0)
        q1 = formul.Q1(Czk=self.data.get('c_ek'), ft=self.data.get('ft'), teta=teta, Eots=self.data.get('e_ots'), Ic1=ic1,
                       Csk=self.data.get('c_sk'), Uc1=uc1)
        rkan1 = formul.Rkan1(rkan=self.data.get('r_k'), Q0=q0, Q1=q1, Ic1=ic1, teta=teta, ft=self.data.get('ft'))
        alfa = formul.alfa(ft=self.data.get('ft'), teta=teta, Csk=self.data.get('c_sk'), Rek=rek)
        beta = formul.beta(ft=self.data.get('ft'), teta=teta, Csz1=csz1, rkan1=rkan1, alfa=alfa)
        c0 = formul.C0(Csz1=csz1, Csk=self.data.get('c_sk'), Czk1=czk1)
        ksi = formul.ksi(Csz1=csz1, Czk1=czk1, ft=self.data.get('ft'), teta=teta, C0=c0, Rek=rek)
        roc = formul.roc(ft=self.data.get('ft'), teta=teta, Li=self.data.get('l_i'), ksi=ksi,
                         beta=beta, Rek=rek, ri=self.data.get('r_i'), rc=self.data.get('r_s'))
        pn = formul.Pn(Ic1=ic1, Rek=rek, rc=self.data.get('r_s'), ri=self.data.get('r_i'), roc=roc, f=f, ft=self.data.get('ft'), teta=teta)
        rn = formul.Rn(Rek=rek, ri=self.data.get('r_i'), rc=self.data.get('r_s'),
                       roc=roc, f=f, ft=self.data.get('ft'), teta=teta, ksi=ksi, beta=beta)
        xn = formul.Xn(Rek=rek, ri=self.data.get('r_i'), f=f, ft=self.data.get('ft'), teta=teta, ksi=ksi, beta=beta,
                       Li=self.data.get('l_i'))
        lvh = formul.Lvh(li=self.data.get('l_i'), ksi=ksi)
        cvh = formul.Cvh(Czk1=czk1, ksi=ksi, alfa=alfa, ft=self.data.get('ft'), teta=teta, ri=self.data.get('r_i'))
        rvh = formul.Rvh(re=self.data.get('r_z'), ri=self.data.get('r_i'), rkan1=rkan1,
                         ft=self.data.get('ft'), teta=teta, alfa=alfa, ksi=ksi, Li=self.data.get('l_i'))
        xvh = formul.Xvh(f=f, Lvh=lvh, Cvh=cvh)
        ivh = formul.Ivh(ksi=ksi, f=f, ft=self.data.get('ft'), teta=teta, Ic1=ic1)
        pvh = formul.Pvh(Ivh=ivh, rvh=rvh)
        ku = formul.KU(Pn=pn, Pvh=pvh)
        kpd = formul.KPD(Pn=pn, Pvh=pvh, P0=p0)
        pras = formul.Pras(Pn=pn, Pvh=pvh, P0=p0)
        ez = formul.Ez(Eots=self.data.get('e_ots'), Ic1=ic1, teta=teta, ft=self.data.get('ft'), Czk=self.data.get('c_ek'))
        ezmax = formul.Ezmax(Ez=ez, Ic1=ic1, ft=self.data.get('ft'), teta=teta, Czk=self.data.get('c_ek'))

        res = {'Максимальная мощность на стоке, Вт': pc1max,
               'Амплитуда первой гармоники тока стока, мА': ic1 * 10 ** 3,
               'Амплиутда первой гармоники напряжения стока, В': uc1,
               'Эквивалентное сопротивление, Ом': rek,
               'Постоянная составляющая тока стока, мА': ic0 * 10 ** 3,
               'Потребляемая мощность, Вт': p0,
               'Q0': q0,
               'Усредненное значение по первой гармонике емкости Сзк1, пФ': czk1,
               'Усредненное значение по первой гармонике емкости Ссз1, пФ': csz1,
               'q1': q1,
               'Сопротивление канала по первой гармоники, Ом': rkan1,
               'alfa': alfa,
               'beta': beta,
               'C0, пФ': c0,
               'Сопротивление обратной связи, Ом': roc,
               'Мощность нагрузки, Вт': pn,
               'Активное сопротивление нагрузки, Ом': rn,
               'Реактивное сопротивление нагрузки, Ом': xn,
               'Входная индуктивность, нГн': lvh * 10 ** 9,
               'Входная емкасть, пФ': cvh * 10 ** 12,
               'Активное входное сопротивление, Ом': rvh,
               'Реактивное входное сопротивление, Ом': xvh,
               'Амплитуда входного тока, А': ivh,
               'Выходная мощность, Вт': pvh,
               'Коэффициент усиления': ku,
               'КПД': kpd,
               'Рассеиваемая мощность, Вт': pras,
               'Напряжение на затворе, В': ez,
               'Максимальное напряжение на затворе, В': ezmax
               }

        return res

    def main_logic(self, name_type, name_x, name_y, start, end, num_tr, f, teta, u, p):
        fig, ax = plt.subplots(num=name_y)

        if name_type == 'Линейный':

            y = []
            x = np.linspace(start, end, 400)
            if name_x == 'Частота, ГГц':
                for i in x:
                    try:
                        y.append(self.formul_dict(num_tr, i, teta, u, p).get(name_y))
                    except TypeError:
                        y.append(None)
                    except ZeroDivisionError:
                        y.append(None)
            if name_x == 'Угол отсечки, град':
                for i in x:
                    try:
                        y.append(self.formul_dict(num_tr, f, i, u, p).get(name_y))
                    except TypeError:
                        y.append(None)
                    except ZeroDivisionError:
                        y.append(None)

            ax.set_xlabel(name_x)
            ax.set_ylabel(name_y)
            ax.set_xlim(start, end)
            ax.plot(x, y)
            plt.title(f'Транзистор {self.data.get("name")}')
            ax.grid()
            plt.show()

        if name_type == 'Тепловая карта':
            pass
