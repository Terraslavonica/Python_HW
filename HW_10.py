## В этих заданиях прикладывайте к коду свои рисунки) Нужно чтобы на рисунках были заголовки, подписи к осям, возможно что-то ещё по желанию)
## Task 1. Нарисуйте line plot по небольшому набору данных (можно задать от руки) (5 баллов)
import matplotlib.pyplot as plt
xs = range(-100, 100)
ys = [((x ** 5) - (x ** 4) + (x ** 2) + x + 10) for x in xs]
plt.plot(xs, ys)
plt.title('Nice function')
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.grid(True)
plt.savefig('Task1.png')

type(ys)

# Task 2. Сделайте программу, принимающую путь к fasta, и выводящую распределение длин последовательностей в ней (10 баллов)
def fastadist(iz):
    with open iz as fasta:



## Task 3. Нарисуйте свой любимый график (не обязательно на основе многих данных -
# генерацию данных разберём на следующем занятии) (15 баллов)
# Я люблю ящики с усами :)
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(10)
collectn_1 = np.random.normal(100, 10, 200)
collectn_2 = np.random.normal(80, 30, 200)
collectn_3 = np.random.normal(90, 20, 200)
collectn_4 = np.random.normal(70, 25, 200)
data_to_plot = [collectn_1, collectn_2, collectn_3, collectn_4]

fig1, ax1 = plt.subplots()
ax1.set_title('My favourite Plot')
ax1.boxplot(data_to_plot)
ax1.set_xlabel('ось x')
ax1.set_ylabel('ось y')

## Task 4.*Уникальный квест - выберите тип визуализации, который вам нравится, разберитесь как создавать такие визуализации,
# кастомизировать их и расскажите всем как!) Нужна небольшая презенташка с кодом и полученными графиками (15 баллов)
# Сделала