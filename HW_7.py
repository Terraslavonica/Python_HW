## Task 1. Создайте 3 тэмплэйта (возьмите .format() или f-строки), используя побольше возможностей (padding, округление)
# и заполните их пару раз (6 баллов)
## 1.1
cat = "Котауси"
mouse = "Мауси"
eyes = "глазауси"
teeth = "зубауси"

print(f'''Жила-была мышка {mouse}
И вдруг увидала {cat}.
У {cat} злые {eyes}
И злые-презлые {teeth}.

Подбежала {cat} к {mouse}
И замахала хвостауси:
"Ах, {mouse}, {mouse}, {mouse},
Подойди ко мне, милая {mouse}!
Я спою тебе песенку, {mouse},
Чудесную песенку, {mouse}!"

Но ответила умная {mouse}:
"Ты меня не обманешь, {cat}!
Вижу злые твои {eyes}
И злые-презлые {teeth}!"
Так ответила умная {mouse} -
И скорее бегом от {cat}.''')

## 1.2
print('''Жила-была мышка {0}
И вдруг увидала {1}.
У {1} злые {3}
И злые-презлые {2}.

Подбежала {1} к {0}
И замахала хвостауси:
"Ах, {0}, {0}, {0},
Подойди ко мне, милая {0}!
Я спою тебе песенку, {0},
Чудесную песенку, {0}!"

Но ответила умная {0}:
"Ты меня не обманешь, {1}!
Вижу злые твои {3}
И злые-презлые {2}!"
Так ответила умная {0} -
И скорее бегом от {1}.'''.format("Мауси", "Котауси", "зубауси", "глазауси"))

##2.1
numb = 'Euler'
e = 2.7182818284590452353602
pi = 3.14159265358979323846
print(f'The {numb} number is denoted by the Latin letter e and is {e:.3}, while pi is equal to {pi:.3}')

##2.2
print('The %s number is denoted by the Latin letter e and is %.2f, while pi is equal to %.2f' % ('Euler', 2.7182, 3.1415))

##3.1
print('''There are three ways to pad text on a sheet:
{:>20}
{:20}
{:^20}
'''.format('one', 'two', 'three'))

##3.2
print('''There are two ways to pad text on a sheet with %%:
%40s
%-40s
''' % ('one', 'two'))

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
# [5, 6, 7, 8, 6, 7, 8, 9, 7, 8, 9, 10, 8, 9, 10, 11]

# строки, представляющие переходы из одних нуклеотидов в другие 'A->T', 'A->C', 'A->G', 'T->A', ...
v = ["A", "T", "G", "C"]
my_str = [i + '->'+ j for i in v for j in v if i!=j]
print(my_str)

# вложенные списки, представляющие матрицу 3 на 3, заполненную от 0 до 9
matrix = [[i+j for i in range(1, 4)] for j in range(0, 7, 3)]
print(matrix)


## Task 4. Имплементируйте линейный поиск (принимает на вход элемент и список, возвращает индекс с этим элементом) (10 баллов)
def lin_search(elem, s):
    """
    Linear search function
    :param elem: float (or int) - the element that we look for
    :param s: list - the list in which we look for the element
    :return: index of the element
    """
    for i, e in enumerate(s):
        if e == elem:
            return i

s = [1, 3, 4, 5, 6, 7, 8, 6.1, 6.1]
print(lin_search(6.1, s))


## Task 5. *Имплементируйте бинарный поиск (принимает на вход элемент и отсортированный список,
# возвращает индекс с этим элементом) (15 баллов)
def bin_search(elem, s):
    """
    Binary search function
    :param elem: float - the element that we look for
    :param s: list - sorted list in which we look for the element
    :return: index of the element
    """
    first = 0
    last = len(s) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if s[midpoint] == elem:
            return midpoint
        elif elem <= s[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1

s = [1, 3, 4, 5, 6, 7, 8, 90, 150.4, 200, 1000]
print(bin_search(1000, s))
print(bin_search(2, s))