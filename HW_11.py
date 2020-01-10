import numpy as np
import random
import time
import matplotlib.pyplot as plt


## Task 1. Создайте 3 эррея различными способами (5 баллов)
ar1 = np.array([11, 21, 32, 43, 54, 65], dtype=np.int8)
print(ar1)

ar2 = np.full((3, 2), 'Hello world')
print(ar2)

ar3 = np.full((2, 5, 5), 69)
print(ar3)

ar4 = np.arange(66, 666, 66)
print(ar4)


## Task 2. Замерьте время вычисления чисел от 0 до 1 из равномерного распределения с помощью модулей random и numpy,
# изобразите зависимость времени вычисления от количества вычисляемых чисел для них. Другими словами - по x идёт то,
# сколько чисел за прогон вы взяли от 0 до 1, а по y - время, которое это заняло для random и numpy (10 баллов)
##1
timeran = []
numbran = []
for i in range(1000, 1000000, 10000):
    numbran.append(i)
    start = time.time()
    for j in range(i):
        random.random()
    stop = time.time()
    timeran.append(stop - start)
print(timeran)
len(timeran)
plt.scatter(numbran, timeran, c="red")

##2
timenp = []
numbnp = []
for i in range(1000, 1000000, 10000):
    numbnp.append(i)
    start = time.time()
    npr = np.random.uniform(low=0.0, high=1.0, size=i)
    stop = time.time()
    timenp.append(stop - start)
print(timenp)
len(timenp)
plt.scatter(numbnp, timenp, c="blue")

## Сделать функцией?
## наверное для модуля рандома как-то иначе нужно, что я пока не знаю как иначе, чем петлей

# Task 3. Сделайте функцию для проверки является ли список отсортированным (без использования sorted или sort).
# Затем реализуйте monkey sort, а потом визуализируйте следующее: распределение времени работы алгоритма от размера
# сортируемого списка. То есть по x идёт размер массива, а по y - среднее время нескольких прогонов и их отклонение
# (или дисперсия) (10 баллов)


## Task 4. Визуализируйте random walk (случайная прогулка, да)) в 2-мерном пространстве, где вы начинаете в (0, 0)
# и можете перемещаться вверх, вниз, вправо и влево Как визуализировать - скаттерплот, где по x - x, а по y - y (10 баллов)
## не случайная прогулка, а случайное блуждание!

## Task 5. Сгенерируйте и нарисуйте треугольник Серпинского (15 баллов)


## Task 6. *Сделайте программу, получающую на вход текст, и выдающую этот же текст со следующими изменениями - буквы
# во всех словах кроме первой и последней перемешаны. Для простоты пока будем считать, что пунктуации нет.
# Пример: "По рзеузльаттам илссоевадний одонго анлигсйокго унвиертисета, не иеемт занчнеия, в каокм проякде рсапжоолены
# бкувы в солве. Галовне, чотбы преавя и пслонедяя бквуы блыи на мсете. осатьлыне бкувы мгоут селдовтаь в плоонм
# бсепордяке, все-рвано ткест чтаитсея без побрелм. Пичрионй эгото ялвятеся то, что мы не чиаетм кдаужю бкуву по
# отдльенотси, а все солво цлиеком." (10 баллов)


## Task 7. *Сгенерируйте и нарисуйте коврик Серпинского. Судя по всему придётся вырезать куски квадрата,
# а не генерировать точками (15 баллов)