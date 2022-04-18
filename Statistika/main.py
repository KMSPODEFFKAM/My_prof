import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os.path
import seaborn as sns
import scipy.stats

'''
1. Создать документ показывающий все необходимые данные по статистике
2. Создать модуль для рисовки данных (оптимальный или универсальный)
3. Создать график нормального распределения
4. Создать и описать все гипотезы 
Какие гипотезы: 
4.1. Гипотеза о нормальности - принять или отклонить
'''

def Stat_Doc(name_Doc):
    myfail = open(str(name_Doc) + '.txt', 'w+')
    myfail.write('Среднее значение:\n' + str(data.mean()) +
                 '\nМедиана: \n' + str(data.median()) +
                 '\nМинимальное значение:\n' + str(data.min()) +
                 '\nМаксимальное значение: \n' + str(data.max()) +
                 '\nРазмах:\n' + str(data.max() - data.min()) +
                 '\nСтандартное отклонение:\n' + str(data.std()) +
                 '\nКоличество выборок: ' + str(len(data)))
    myfail.close()

def Filtr(uslovie1, arg1, z):
    if z == '<':
        data_filtr = data[data[str(uslovie1)] < arg1]
    if z == '==':
        data_filtr = data[data[str(uslovie1)] == arg1]
    if z == '>':
        data_filtr = data[data[str(uslovie1)] > arg1]
    if z == '!=':
        data_filtr = data[data[str(uslovie1)] == arg1]
    print(data_filtr)

def Normal():
    stat, p = scipy.stats.shapiro(data)
    if p < 0.05:
        print('Распределение не нормальное')
    else:
        print('Нормальное')

def Box_Graf(name_graf, new_data, name_stolb, name_title=''):
    sns.boxplot(new_data[str(name_stolb)])
    plt.title(str(name_title))
    plt.savefig(str(name_graf) + ' box', dpi=1000)
    plt.close()

def Goroh(name_graf, new_data, x, y, name_title=''):
    sns.scatterplot(data=new_data, x=str(x), y=str(y))
    plt.title(str(name_title))
    plt.savefig(str(name_graf) + ' goroh', dpi=1000)
    plt.close()

def Histogramm(name_graf, new_data, name_stolb, m=50, name_title=''):
    plt.hist(new_data[str(name_stolb)], bins=m)
    plt.title(str(name_title))
    plt.savefig(str(name_graf) + ' hist', dpi=1000)
    plt.close()

def Crate_papka(name_papka, path='C:/Users\DEXP\PycharmProjects\Scine_Project_NSY'):
    fullpath = os.path.join(path, name_papka)
    os.mkdir(fullpath)

def Modul_Graf(name_papka, new_data, name_stolb):
    Box_Graf(name_papka)
    Goroh(name_papka, 'Chastota', 'Amplituda')
    Histogramm(name_papka, new_data, name_stolb)

def Norm():
    stat_n, p_n = scipy.stats.normaltest(data_filtr1['Amplituda'])
    if p_n < 0.05:
        print(p_n, 'Не нормальное распределение')
    else:
        print(p_n, 'Нормальное распределение')

data = pd.read_excel('Nefedov_Cable_Load.xlsx')
data_filtr1 = data[data['Azimut'] == -100]
data_filtr2 = data[data['Azimut'] == -90]