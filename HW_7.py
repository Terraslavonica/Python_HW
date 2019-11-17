## Task 1. Создайте 3 тэмплэйта (возьмите .format() или f-строки), используя побольше возможностей (padding, округление)
# и заполните их пару раз (6 баллов)


## Task 2. Сделайте несколько распаковок произвольных списков/кортежей в переменные (3 балла)
my_french_set = ['Paris', 'Lion', 'Nantes', 'Versailles', 'Annecy']
ville1, ville2, ville3, ville4, ville5 = my_french_set
print(ville1, ville2, ville3, ville4, ville5)

la_première, *moyenne, la_dernière = my_french_set
print(la_première)
print(*moyenne)
print(moyenne)
print(la_dernière)

from collections import namedtuple
Villes = namedtuple("Villes", "ville1 ville2 ville3 ville4 ville5")
n_villes  = Villes(*my_french_set)
print(*n_villes)
print(n_villes)
print(n_villes.ville1, n_villes.ville2, n_villes.ville3, n_villes.ville4, n_villes.ville5)

my_french_tuple = ('les escargots', 'les cuisses de grenouilles', 'les croissants', 'la crème brûlée')
plat1, plat2, plat3, plat4 = my_french_tuple
print(plat1, plat2, plat3, plat4)

le_premier, *moyen, le_dernier = my_french_tuple
print(le_premier)
print(moyen)
print(le_dernier)

Plat = namedtuple("Plat", "plat1 plat2 plat3 plat4")
n_plats = Plat(*my_french_tuple)
print(*n_plats)
print(n_plats)
print(n_plats.plat1, n_plats.plat2, n_plats.plat3, n_plats.plat4)

## Task 3. Напишите следующие comprehension'ы:
au_carre = [x*x for x in range(11)]  # квадраты чисел от 0 до 10
print(au_carre)

# суммы 2-ух чисел, взятых из последовательностей от 0 до 3 и от 5 до 8
somme_de_deux = [x+y for y in range(5, 9) for x in range(0, 4)]
print(somme_de_deux)
# [5, 6, 7, 8, 6, 7, 8, 9, 7, 8, 9, 10, 8, 9, 10, 11] ## Это ведь не то, что нужно? Нужно [5, 7, 9, 11] ??

# Тогда так
x = range(5, 9)
y = range(0, 4)
somme_de_deux = [x + y for x, y in zip(x, y)]
print(somme_de_deux)

# строки, представляющие переходы из одних нуклеотидов в другие 'A->T', 'A->C', 'A->G', 'T->A', ...
v = ["A", "T", "G", "C"]
my_str = [print(i + '->'+ j) for i in v for j in v if i!=j]

# вложенные списки, представляющие матрицу 3 на 3, заполненную от 0 до 9
matrix = [[i+j for i in range(1, 4)] for j in range(0, 7, 3)]
print(matrix)


## Task 4. Имплементируйте линейный поиск (принимает на вход элемент и список, возвращает индекс с этим элементом) (10 баллов)
# возвращает индекс с этим элементом... Што, простите? Имеется в виду "возвращает индекс этого элемента" или "возвращает элемент и его индекс"
def lin_serch(elem, s):
    for i, e in enumerate(s):
        if e == elem:
            return(i)
            break

s = [1,3,4,5,6,7,8,6]
print(lin_serch(6, s))
# тут достаточно индекса первого вхождения?

## Task 5. *Имплементируйте бинарный поиск (принимает на вход элемент и отсортированный список,
# возвращает индекс с этим элементом) (15 баллов)