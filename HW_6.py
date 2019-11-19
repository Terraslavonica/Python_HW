## Task 1. *Сделайте функцию, принимающую лист и возвращающую выпрямленный лист (исходный не должен был измениться):
def flatten(List):
    """
    Function which make the List flat
    :param List: list - your list
    :return: flat List
    """
    if List == []:
        return List
    if type(List[0]) is list:
        return flatten(List[0]) + flatten(List[1:])
    return List[:1] + flatten(List[1:])

print(flatten([[1, [[1], 2], 3, [[4, 5, [[[6]]]]]]]))
## [1, 1, 2, 3, 4, 5, 6]
print(flatten([[[[[[[[[[[[[[[[[[[[['privet']]]]]]]]]]]]]]]]]]]]]))
## ['privet']
print(flatten([[[0.5, True], 1, [[1], 2], 3, [[4, 5, [[[6]]]]]]]))
## [0.5, True, 1, 1, 2, 3, 4, 5, 6]
print(flatten([1, [1, 2], [[[[3]]]], [[4, 5, [6.5, True]]]]))
## [1, 1, 2, 3, 4, 5, 6.5, True]

## Task 2. Напишите функцию, принимающую число и вычисляющую число Фибоначчи с номером поданного числа
def fibo(n):
    """
    Function that compute the nth Fibonacci number
    :param n: int - number
    :return: nth Fibonacci number
    """
    a = [1, 1]
    for i in range(0, n):
        a.append(a[i] + a[i+1])
    return a[n-1]

print(fibo(1))
print(fibo(2))
print(fibo(7))
print(fibo(8))
print(fibo(100)) # Работает быстро

def fibo2(n):
    """
    Function that compute the nth Fibonacci number
    :param n: int - number
    :return: nth Fibonacci number
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo2(n-1) + fibo2(n-2)

print(fibo2(1))
print(fibo2(8))
print(fibo2(100)) # Этот вариант функции чудовищно медленно работает! Это он так и не посчитал, пришлось убить

## В данных заданиях нельзя пользоваться функциями len, max, reversed, но можно переиспользовать написанные вами функции
## Тогда будем использовать счётчик количества элементов
def schetchik(spisok):
    """
    Calculate the number of elements in the list
    :param spisok: list - your list
    :return: the lenght of your list
    """
    i = 0
    for elem in spisok:
        i += 1
    return i

print(schetchik([100, 2, 3, 45, -2, 4]))
# ответ 6


## Task 3. Напишите функцию, возвращающую максимум, который есть в списке чисел
def maximum(spisok):
    """
    Find maximal element in the list
    :param spisok: list - your list
    :return: maximal element in the list
    """
    maxi = spisok[0]
    for i in spisok:
        if i > maxi:
            maxi = i
    return maxi

print(maximum([100, 2, 3, 45, -2, 4]))


## Task 4. Функцию, возвращающую список в обратном порядке
def reverse(spisok):
    """
    Give the reversed list
    :param spisok: list - your list
    :return: reversed list
    """
    rev_sp = []
    i = schetchik(spisok) - 1
    while i >= 0:
        rev_sp.append(spisok[i])
        i -= 1
    return rev_sp

print(reverse([100, 2, 3, 45, -2, 4]))

## Task 5. Функцию, вычисляющую среднее списка
def mean(spisok):
    """
    Compute the average of the elements in your list
    :param spisok: list - your list
    :return: average value of all elements in the list
    """
    n = schetchik(spisok)
    sumi = 0
    i = n - 1
    while i >= 0:
        sumi += spisok[i]
        i -= 1
    my_avg = sumi/n
    return my_avg

print(mean([100, 2, 3, 45, -2, 4, 1000000, - 6000, -1999]))


## Task 6. Функцию, находящую самый частый элемент в списке, если их несколько, то все
def moda(spisok):
    """
    Find the most frequent element in your list or all of them
    :param spisok: list - your list
    :return: the most frequent element in your list or all of them
    """
    dict = {}
    for element in spisok:
        dict[element] = dict.get(element, 0) + 1
    numb = list(dict.values())
    max_numb = maximum(numb)
    moda = []
    for key, val in dict.items():
        if val == max_numb:
            moda.append(key)
    return tuple(moda)

print(moda([100, 3, 100, 2, 45, 45, 45, 3, 45, 3, 3, -2, 4]))
print(moda([1, 2, 3, 4, 5, 6, 7, 8, 9]))


## Task 7. Функцию, берущую указанный элемент из коллекции
def get(collection, elem_pos):
    """
    Return the element of your collection with position elem_pos
    :param collection: dict, str, list, tuple - your collection
    :param elem_pos: the position of the element that you need to return (starts at 0)
                     (for str, list, tuple) or key for the dict
    :return: Return the element with position elem_pos
    """
    return collection[elem_pos]

s = (1, 2, 3, 4)
print(get(s, 2))

t = [1, 2, 3, 4]
print(get(t, 1))

st = "sdhfgsufhlk"
print(get(st, 7))

dict = {1:"one", 2:"two", 3:"three"}
print(get(dict, 1))
