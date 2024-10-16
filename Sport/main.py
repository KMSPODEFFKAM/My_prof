import matplotlib.pyplot as plt
import datetime
# Вес
ves = [90, 80, 70]
# ИМТ
bmi = []
# динамика жира
dj = []
# Висцелярный жир
vj = []

rost = 181

def write():
    _ves = float(input('Вес: '))
    _dj = float(input('Динамика жира: '))
    _vj = float(input('Висцелярный жир: '))
    ves.append(_ves)
    dj.append(_dj)
    vj.append(_vj)

def main():
    print('Сегодня: ' + str(datetime.datetime.now()))
    write()
    print(ves)
    ves_plot()

def ves_plot():
    plt.plot([i for i in range(len(ves))], ves)
    plt.plot([i for i in range(len(ves))], [80 for i in range(len(ves))], linestyle="--")
    for i in range(len(ves)):
        plt.scatter(i, ves[i], color='black')
        plt.text(i, 1.018 * ves[i], str(ves[i]), fontsize=18)
    plt.grid()
    plt.ylim(0.97 * min(ves), 1.04 * max(ves))
    plt.show()

if __name__ == '__main__':
    ves_plot()