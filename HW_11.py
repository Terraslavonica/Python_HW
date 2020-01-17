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

def timerandom(gofrom, goto, step):
    timeran = []
    numbran = range(gofrom, goto, step)
    for i in numbran:
        start = time.time()
        for j in range(i):
            random.random()
        stop = time.time()
        timeran.append(stop - start)
    #return timeran

def timenumpy(gofrom, goto, step):
    timenp = []
    numbnp = range(gofrom, goto, step)
    for i in numbnp:
        start = time.time()
        npr = np.random.uniform(low=0.0, high=1.0, size=i)
        stop = time.time()
        timenp.append(stop - start)
    #return timenp

def mytimeplot(gofrom, goto, step):
    timeran = timerandom(gofrom, goto, step)
    timenp = timenumpy(gofrom, goto, step)
    numbran = range(gofrom, goto, step)
    numbnp = range(gofrom, goto, step)
    gr = plt.figure(figsize=(12, 8))
    plt.scatter(numbran, timeran, c="red", label='random')
    plt.scatter(numbnp, timenp, c="blue", label='numpy')
    plt.legend()
    return gr

mytimeplot(1000, 1000000, 10000)


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
progon = range(15) # number of repetition for the same data size
for i in range(2, 15, 2):
    timepr = []
    size.append(i)
    for j in progon:
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
plt.scatter(size, monkeymean, c = 'green', label='mean time')
plt.errorbar(size, monkeymean, monkeysd, linestyle='None')
plt.scatter(size, monkeysd, c = 'red', label='sd of time')
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
plt.plot(x, y, s=1, c = 'green')
# plt.scatter(x, y, s=1, c = 'green')


## Task 5. Сгенерируйте и нарисуйте треугольник Серпинского (15 баллов)
# defining the number of steps
n = 15000
# creating two array for containing x and y coordinate of size equals to the number of size and filled up with 0's
x = np.zeros(n)
y = np.zeros(n)
# Choose the vertex of a triangle
A = np.array([8, 3])
B = np.array([5, -1])
C = np.array([-3, -2])
# filling the coordinates with random variables
for i in range(1, n):
    val = random.randint(1, 3)
    if val == 1:
        x[i] = x[i - 1] + (A[0] - x[i - 1]) / 2
        y[i] = y[i - 1] + (A[1] - y[i - 1]) / 2
    elif val == 2:
        x[i] = x[i - 1] + (B[0] - x[i - 1]) / 2
        y[i] = y[i - 1] + (B[1] - y[i - 1]) / 2
    else:
        x[i] = x[i - 1] + (C[0] - x[i - 1]) / 2
        y[i] = y[i - 1] + (C[1] - y[i - 1]) / 2
# plotting the graph
plt.title("Sierpinski triangle ($n = " + str(n) + "$ steps)")
plt.scatter(x, y, s=1, c = 'purple')


## Task 6. *Сделайте программу, получающую на вход текст, и выдающую этот же текст со следующими изменениями - буквы
# во всех словах кроме первой и последней перемешаны. Для простоты пока будем считать, что пунктуации нет.
# Пример: "По рзеузльаттам илссоевадний одонго анлигсйокго унвиертисета, не иеемт занчнеия, в каокм проякде рсапжоолены
# бкувы в солве. Галовне, чотбы преавя и пслонедяя бквуы блыи на мсете. осатьлыне бкувы мгоут селдовтаь в плоонм
# бсепордяке, все-рвано ткест чтаитсея без побрелм. Пичрионй эгото ялвятеся то, что мы не чиаетм кдаужю бкуву по
# отдльенотси, а все солво цлиеком." (10 баллов)

# пока не получилось, но, думаю, я сделаю


## Task 7. *Сгенерируйте и нарисуйте коврик Серпинского. Судя по всему придётся вырезать куски квадрата,
# а не генерировать точками (15 баллов)
# defining the number of steps
n = 100000
# creating two array for containing x and y coordinate of size equals to the number of size and filled up with 0's
x = np.zeros(n)
y = np.zeros(n)
# Choose 8 attracting points
A = np.array([1, 1])
B = np.array([-1, 1])
C = np.array([-1, -1])
D = np.array([1, -1])
E = np.array([(A[0]+B[0])/2, (A[1]+B[1])/2])
F = np.array([(C[0]+B[0])/2, (C[1]+B[1])/2])
G = np.array([(C[0]+D[0])/2, (C[1]+D[1])/2])
H = np.array([(A[0]+D[0])/2, (A[1]+D[1])/2])
# filling the coordinates with random variables
for i in range(1, n):
    val = random.randint(1, 8)
    if val == 1:
        x[i] = (x[i - 1] + 2 * A[0]) / 3
        y[i] = (y[i - 1] + 2 * A[1]) / 3
    elif val == 2:
        x[i] = (x[i - 1] + 2 * B[0]) / 3
        y[i] = (y[i - 1] + 2 * B[1]) / 3
    elif val == 3:
        x[i] = (x[i - 1] + 2 * C[0]) / 3
        y[i] = (y[i - 1] + 2 * C[1]) / 3
    elif val == 4:
        x[i] = (x[i - 1] + 2 * D[0]) / 3
        y[i] = (y[i - 1] + 2 * D[1]) / 3
    elif val == 5:
        x[i] = (x[i - 1] + 2 * E[0]) / 3
        y[i] = (y[i - 1] + 2 * E[1]) / 3
    elif val == 6:
        x[i] = (x[i - 1] + 2 * F[0]) / 3
        y[i] = (y[i - 1] + 2 * F[1]) / 3
    elif val == 7:
        x[i] = (x[i - 1] + 2 * G[0]) / 3
        y[i] = (y[i - 1] + 2 * G[1]) / 3
    else:
        x[i] = (x[i - 1] + 2 * H[0]) / 3
        y[i] = (y[i - 1] + 2 * H[1]) / 3
# plotting the graph
plt.title("Sierpinski carpet ($n = " + str(n) + "$ steps)")
plt.scatter(x, y, s=1, c = 'blue')