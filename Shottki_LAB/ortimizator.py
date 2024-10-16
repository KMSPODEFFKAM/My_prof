import math
import random

class Simulated_annealing:

    def __init__(self, x, eps):

        self.temperatura_start = 3000
        self.temperatura_end = 1
        self.koeff_tem = 0.9999

        self.eps = eps

        self.obl_x = x

        self.poz_start = [random.uniform(self.obl_x[i][0], self.obl_x[i][1]) for i in range(len(self.obl_x))]
        self.poz_next = []

        self.energy_start = 0
        self.energy_end = 0

    def calculate_temp(self):
        return self.temperatura_start * self.koeff_tem

    def test_func(self, x: list):
        return (1.5 - x[0] + x[0] * x[1]) ** 2\
               + (2.25 - x[0] + x[0] * x[1] ** 2) ** 2\
               + (2.625 - x[0] + x[0] * x[1] ** 3) ** 2

    def func_estimation(self):
        if abs(self.dres) >= self.eps or self.temperatura_start > self.temperatura_end:
            return True
        else:
            return False

    def main(self, function):

        # определяем позицию
        self.poz_next = [(random.uniform(self.obl_x[elem][0], self.obl_x[elem][1]))for elem in range(len(self.obl_x))]

        # результат позиции
        res_start = function(self.poz_start)
        res_next = function(self.poz_next)

        print(f'Начальные показатели = {self.poz_start}')
        print(f'Следущие показатели = {self.poz_next}')

        print(f'Начальная энергия = {res_start}')
        print(f'Конечная энергия = {res_next}')

        self.dres = res_next - res_start

        print(f'Разность энергии = {self.dres}')

        if self.dres < 0:
            self.poz_start = self.poz_next
            self.energy_start = res_next
            print(f'Новая энергия = {self.energy_start}')
        else:
            if random.uniform(0, 1) < math.exp(-self.dres / self.temperatura_start):
                self.energy_start = res_next
                self.poz_start = self.poz_next
                print(f'Новая энергия = {self.energy_start}')
            else:
                print(f'Ничего не поменялось!')

        self.temperatura_start = self.calculate_temp()


        print(f'Температура = {self.temperatura_start}')

    def calculate_algoritm(self, function):
        self.main(function)

        while(self.func_estimation()):
            self.main(function)

class  Particle_swarm:
    def __init__(self, count_point):
        self.count_point = count_point



if __name__ == '__main__':

    opt = Simulated_annealing([[-4.5, 4.5], [-4.5, 4.5]], 0.00001)
    res = opt.calculate_algoritm(opt.test_func)
    print(opt.poz_start)



