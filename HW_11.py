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

plt.figure(figsize=(12, 8))
plt.scatter(numbran, timeran, c="red", label='random')

##2
timenp = []
numbnp = []
for i in range(1000, 1000000, 10000):
    numbnp.append(i)
    start = time.time()
    npr = np.random.uniform(low=0.0, high=1.0, size=i)
    stop = time.time()
    timenp.append(stop - start)

plt.scatter(numbnp, timenp, c="blue", label='numpy')
plt.legend()

## Сделать функцией?
## наверное для модуля рандома как-то иначе нужно, что я пока не знаю как иначе, чем петлей


# Task 3. Сделайте функцию для проверки является ли список отсортированным (без использования sorted или sort).
# Затем реализуйте monkey sort, а потом визуализируйте следующее: распределение времени работы алгоритма от размера
# сортируемого списка. То есть по x идёт размер массива, а по y - среднее время нескольких прогонов и их отклонение
# (или дисперсия) (10 баллов)

def is_sorted(data):
    """
    Determine whether the data is sorted.
    :param data: list - data that mast be sorted
    :return: True if the data is sorted and False if not
    """
    for i in range(len(data) - 1):
    if data[i] > data[i + 1]:
        return False
    else:
        return True

def monkysort(data):
    """
    Shuffle data until sorted
    :param data: list - data that mast be sorted
    :return: data sorted my monkey algorithm
    """
    while not is_sorted(data):
        random.shuffle(data)
    return data

monkeymean = [] # average sorting time
monkeysd = [] # standard deviation of sorting time
size = []
progon = 15 # number of repetition for the same data size
for i in range(2, 10000, 50):
    timepr = []
    size.append(i)
    for j in range(0, progon):
        data = np.random.randint(1, 100000, i)
        start = time.time()
        monkysort(data)
        stop = time.time()
        timepr.append(stop - start)
    timemean = np.mean(timepr)
    timesd = np.var(timepr)**0.5
    monkeymean.append(timemean)
    monkeysd.append(timesd)

plt.title("Monkey time")
plt.scatter(size, monkeymean, c = 'green', label='mean time' )
plt.scatter(size, monkeysd, c = 'pink', label='sd of time')
plt.xlabel('sample size')
plt.ylabel('time')
plt.legend()


## Task 4. Визуализируйте random walk (случайная прогулка, да)) в 2-мерном пространстве, где вы начинаете в (0, 0)
# и можете перемещаться вверх, вниз, вправо и влево Как визуализировать - скаттерплот, где по x - x, а по y - y (10 баллов)
## не случайная прогулка, а случайное блуждание!

# defining the number of steps
n = 10000
# creating two array for containing x and y coordinate of size equals to the number of size and filled up with 0's
x = np.zeros(n)
y = np.zeros(n)
# filling the coordinates with random variables
for i in range(1, n):
    val = random.randint(1, 4)
    if val == 1:
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1]
    elif val == 2:
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1]
    elif val == 3:
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
    else:
        x[i] = x[i - 1]
        y[i] = y[i - 1] - 1
# plotting the graph
plt.title("Random walk ($n = " + str(n) + "$ steps)")
plt.scatter(x, y, s=1, c = 'green')
## График прикладывать? Там красота :)


## Task 5. Сгенерируйте и нарисуйте треугольник Серпинского (15 баллов)
# пока не получилось! :( сделаю обязательно!

## Task 6. *Сделайте программу, получающую на вход текст, и выдающую этот же текст со следующими изменениями - буквы
# во всех словах кроме первой и последней перемешаны. Для простоты пока будем считать, что пунктуации нет.
# Пример: "По рзеузльаттам илссоевадний одонго анлигсйокго унвиертисета, не иеемт занчнеия, в каокм проякде рсапжоолены
# бкувы в солве. Галовне, чотбы преавя и пслонедяя бквуы блыи на мсете. осатьлыне бкувы мгоут селдовтаь в плоонм
# бсепордяке, все-рвано ткест чтаитсея без побрелм. Пичрионй эгото ялвятеся то, что мы не чиаетм кдаужю бкуву по
# отдльенотси, а все солво цлиеком." (10 баллов)


## Task 7. *Сгенерируйте и нарисуйте коврик Серпинского. Судя по всему придётся вырезать куски квадрата,
# а не генерировать точками (15 баллов)