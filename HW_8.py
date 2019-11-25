## Task 1. Создайте пару файлов (наполненных каким-то кодом), один из которых импортируется в другом,
# удостоверьтесь, что при импорте выполняется импортируемый файл (5 баллов)
"""
Завела File_1.py c таким кодом
print('Hi from File_1')
def myfun():
    return 42

Потом File_2.py c кодом
import File_1
print("Hi")
print(File_1.myfun())
"""

import File_2
"""
Hi from File_1
Hi
42
"""
print(File_2.File_1.myfun())
## 42

from File_2 import *
"""
Hi from File_1
Hi
42
"""
print(File_1.myfun())
## 42



## Task 2. Создайте функцию, которая получает на вход путь к файлу, который нужно считать,
# путь к файлу, куда будет идти сохранение, и номера строк с которой и до какой нужно переписать
# содержимое из одного файла в другой (то есть она выдирает часть текста из одного файла в другой),
# если номера строк не были переданы - копирует содержимое файла целиком (10 баллов)
def rewright(iz, v, first = None, last = None):
    with open(iz, 'r') as source, open(v, 'w') as destin:
        cont = source.readlines()
        n = len(cont)
        if first >= 0 and last:
            for i in range(first, last + 1):
                destin.write(cont[i])
        elif first and not last:
            for i in range(first, n):
                destin.write(cont[i])
        elif not first and last:
            for i in range(0, last + 1):
                destin.write(cont[i])
        else:
            for i in range(0, n):
                destin.write(cont[i])

rewright('text1.txt', 'text2.txt', first = 1)
rewright('text1.txt', 'text2.txt', 0, 12)
# обе работают) Файлы txt тоже на гитхаб положить?

## Task 3. Посмотрите на либы для рисования графов, выберите понравившуюся и визуализируйте какой-нибудь граф (10 баллов)
import networkx
import pytest
import matplotlib.pyplot

G = {1: [2, 3], 2: [1, 4, 5], 3: [1, 5], 4: [2], 5: [2, 3]}
NN = networkx.DiGraph()
NN.add_edge([2, 3])
networkx.draw(NN, G) # Пока ничего не пашет
matplotlib.pyplot.subplot(121)

## Task 4. Напишите функцию, вычисляющую число компонент связности в графе,
# переданном в формате списка связности (для этого можно использовать dfs) (15 баллов)


## Task 5. Установите модуль biopython

"""
Я сделяль)))))))))
C:\Users\Ekaterina\AppData\Local\Programs\Python\Python38\Scripts\pip install biopython
Requirement already satisfied: biopython in c:\users\ekaterina\appdata\local\programs\python\python38\lib\site-packages (1.75)
Requirement already satisfied: numpy in c:\users\ekaterina\appdata\local\programs\python\python38\lib\site-packages (from biopython) (1.17.4)
WARNING: You are using pip version 19.2.3, however version 19.3.1 is available.
You should consider upgrading via the 'python -m pip install --upgrade pip' command.

py -m pip install --upgrade pip
Collecting pip
  Downloading https://files.pythonhosted.org/packages/00/b6/9cfa56b4081ad13874b0c6f96af8ce16cfbc1cb06bedf8e9164ce5551ec1/pip-19.3.1-py2.py3-none-any.whl (1.4MB)
     |████████████████████████████████| 1.4MB 819kB/s
Installing collected packages: pip
  Found existing installation: pip 19.2.3
    Uninstalling pip-19.2.3:
      Successfully uninstalled pip-19.2.3
Successfully installed pip-19.3.1
"""
