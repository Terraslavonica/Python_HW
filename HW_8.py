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
    """
    Rewrite the content of one file to another file fully or partially
    :param iz: - str - path to file from which the content will be written
    :param v: - str - path to file in which the content will be written
    :param first: - int or None - line number from which the content start to rewrite
    :param last: - int or None - line number till which the content will be rewrite
    :return: the second file will contain the content of the first file fully or partially
    """
    with open(iz, 'r') as source, open(v, 'w') as destin:
        cont = source.readlines()
        n = len(cont)
        if not first and not last:
            for i in range(0, n):
                destin.write(cont[i])
        elif first and not last:
                for i in range(first, n):
                    destin.write(cont[i])
        elif not first and last:
                for i in range(0, last + 1):
                    destin.write(cont[i])
        else:
            for i in range(first, last + 1):
                destin.write(cont[i])

rewright('text1.txt', 'text2.txt')
rewright('text1.txt', 'text2.txt', first = 1)
rewright('text1.txt', 'text2.txt', last = 3)
rewright('text1.txt', 'text2.txt', 0, 12)

## Task 3. Посмотрите на либы для рисования графов, выберите понравившуюся и визуализируйте какой-нибудь граф (10 баллов)
import networkx as nx
G = nx.Graph()
G.add_nodes_from([1, 2, 3, 4, 5, 6, 7])
G.add_edges_from([(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 4), (4, 3), (4, 5), (4, 7), (5, 4), (5, 6), (6, 5), (6, 7), (7, 6), (7, 4)])
nx.draw(G, with_labels=True) # с именами верщин

import matplotlib.pyplot as plt
nx.draw_shell(G, nlist=[range(4, 8), range(4)], with_labels=True)

options = { # в options указаны цвета вершин и ребер, толщина ребер и размер вершин
    'node_color': 'green',
    'edge_color': 'red',
    'node_size': 200,
    'width': 1,
}
nx.draw_shell(G, **options, nlist=[range(4, 8), range(4)], with_labels=True)
plt.savefig("mygraph.png") # сохраним

# милота :)
K_3_5 = nx.complete_bipartite_graph(3, 5)
nx.draw(K_3_5)
lollipop = nx.lollipop_graph(100, 40)
nx.draw(lollipop)
tutte = nx.tutte_graph()
nx.draw(tutte)
petersen = nx.petersen_graph()
nx.draw(petersen)
maze = nx.sedgewick_maze_graph()
nx.draw(maze)
tet = nx.tetrahedral_graph()
nx.draw(tet)


## Task 4. Напишите функцию, вычисляющую число компонент связности в графе,
# переданном в формате списка связности (для этого можно использовать dfs) (15 баллов)
def search(vertex, graph, visited):
    """
    Function helper to move in graph
    :param vertex: hashable - current vertex
    :param graph: dict - "adjacency dict" in a form {vertex: [neighbours...]}
    :param visited: dict - dict with visited vertices in a form {vertex: True/False}
    :return:
    """
    # Mark vertex as visited
    visited[vertex] = True

    # Go to other vertex, adjacent to current, if they weren't visited before
    for neighbour in graph[vertex]:
        if not visited[neighbour]:
            search(neighbour, graph, visited)


def dfs(graph):
    """
    Function to apply depth-first search to a graph
    :param graph: dict - "adjacency dict" in a form {vertex: [neighbours...]}
    :return:
    """
    # Create dict of visited vertices
    visited = {v: False for v in graph}

    # Visit all reachable vertices from vertex for all vertices
    q = 0
    for v in graph:
        if not visited[v]:
            q += 1
            search(v, graph, visited)
    return q


graph = {1: [2, 3], 2: [1, 4, 5], 3: [1, 5], 4: [2], 5: [2, 3], 6: [7], 7: [6], 8: [], 9: [10], 10: [9]}
print(dfs(graph))

graph1 = {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
print(dfs(graph1))


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
