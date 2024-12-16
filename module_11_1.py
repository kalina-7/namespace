# мпортируем используемые библиотеки, предварительно установив их
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''библиотека pandas'''

# чтение и вывод таблицы из файла
df = pd.read_csv('data.csv')
print(df)
print(20*'_')

# создание таблицы
data_1 = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6]})
data_2 = pd.DataFrame({'B': [4, 5, 6, 7, 8, 9]})
data_3 = pd.DataFrame({'C': [7, 8, 9, 10, 11, 12]})
data_4 = pd.DataFrame({'D': ['first', 'second', 'first', 'second', 'second', 'first']})

data = data_1.join([data_2, data_3, data_4])
print(data)
print(20*'_')

# вывод среднего значения каждого столбца
table = pd.pivot_table(data, values=['A', 'B','C'], index='D', aggfunc={'A': "mean", 'B': "mean", 'C': "mean"})
print(table)
print(20*'_')

# вывод уникального значения столбца 'D'
print(pd.unique(data['D']))
print(20*'_')

'''библиотека numpy'''

# создаём два массива и объединяем их
a = np.array([1, 2, 3, 4, 5, 6])
b = np.array([7, 8, 9, 10, 11, 12])
print(np.concatenate((a, b)))
print(20*'_')

# создаём массив и выводим общее количество элементов в массиве
c = np.array([[[0, 1, 2, 3],
               [4, 5, 6, 7]],

              [[8, 9, 10, 11],
               [12, 13, 14, 15]],

              [[16, 17, 18, 19],
               [20, 21, 22, 23]]])

print(c.size)
print(20*'_')

# создаём два массива и складываем их вертикально и горизонтально
d1 = np.array([[1, 2, 3, 4],
               [5, 6, 7, 8]])

d2 = np.array([[9, 10, 11, 12],
               [13, 14, 15, 16]])

print(np.vstack((d1, d2)))
print(20*'_')
print(np.hstack((d1, d2)))
print(20*'_')

'''библиотека matplolib'''

# создаём фигуру по координатам x, y и отображаем её
fig, ax = plt.subplots()
ax.plot([1, 8, 10, 11, 5], [4, 8, 9, 12, 16])

# создаём график трёх функций от x в количестве 100 выборок с равными интервалами, вычисленных за интервал [0, 2]
x = np.linspace(0, 2, 100)

plt.figure(figsize=(8, 5), layout='constrained')
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()

# создаём точечный график x от y и заданными размером и цветом маркера
x = [5, 8, 1, 10, 7, 15, 2, 13, 9, 11, 6, 4, 12, 14, 3, 16]
y = [15, 13, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 11, 10, 9]

fig, ax = plt.subplots(figsize=(5, 2.7))
ax.scatter(x, y, s=100, facecolor='C1', edgecolor='r')
plt.show()