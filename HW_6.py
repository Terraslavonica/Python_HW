## Task 1. *Сделайте функцию, принимающую лист и возвращающую выпрямленный лист (исходный не должен был измениться):
def flatten(List):

    def flat(List):
        Flat_list = []
        for i in range(0, len(List)):
            if type(List[i]) is list: ## исходя из задания внутри листа ведь могут быть тоже только листы? если нет, то нужно еще докручивать
                for j in range(0, len(List[i])):
                    Flat_list.append(List[i][j])
            else:
                Flat_list.append(List[i])
        return Flat_list

    Flat_list = flat(List)
    for k in range(0, len(Flat_list)):
        if type(Flat_list[k]) is list:
            a = True
            while a:
                Flat_list = flat(Flat_list)
                for k in range(0, len(Flat_list)):
                    if type(Flat_list[k]) is list:
                        a = True
                    else:
                        a = False
    return Flat_list


print(flatten([[1, [[1], 2], 3, [[4, 5, [[[6]]]]]]]))
## [1, 1, 2, 3, 4, 5, 6]
print(flatten([[[[[[[[[[[[[[[[[[[[['privet']]]]]]]]]]]]]]]]]]]]]))
## ['privet']
print(flatten([[[0.5, True], 1, [[1], 2], 3, [[4, 5, [[[6]]]]]]]))
## [0.5, True, 1, 1, 2, 3, 4, 5, 6]

## Task 2. Напишите функцию, принимающую число и вычисляющую число Фибоначчи с номером поданного числа
def fibo(n):
    a = [1, 1]
    for i in range(0, n):
        a.append(a[i] + a[i+1])
    return a[n-1]

fibo(1)
fibo(2)
fibo(7)
fibo(8)
fibo(100)


## В данных заданиях нельзя пользоваться функциями len, max, reversed, но можно переиспользовать написанные вами функции
## Тогда будем использовать счётчик количества элементов
def schetchik(spisok):
    i = 0
    for elem in spisok:
        i += 1
    return i

schetchik([100, 2, 3, 45, -2, 4])
# ответ 6


## Task 3. Напишите функцию, возвращающую максимум, который есть в списке чисел
def maximum(spisok):
    maxi = spisok[0]
    for i in spisok:
        if i > maxi:
            maxi = i
    return maxi

maximum([100, 2, 3, 45, -2, 4])


## Task 4. Функцию, возвращающую список в обратном порядке
def reverse(spisok):
    rev_sp = []
    i = schetchik(spisok) - 1
    while i >= 0:
        rev_sp.append(spisok[i])
        i -= 1
    return rev_sp

reverse([100, 2, 3, 45, -2, 4])

## Task 5. Функцию, вычисляющую среднее списка
def mean(spisok):
    n = schetchik(spisok)
    sumi = 0
    i = n - 1
    while i >= 0:
        sumi += spisok[i]
        i -= 1
    my_avg = sumi/n
    return my_avg

mean([100, 2, 3, 45, -2, 4, 1000000, - 6000, -1999])


## Task 6. Функцию, находящую самый частый элемент в списке, если их несколько, то все
def moda(spisok):
    dict = {}
    for element in spisok:
        dict[element] = dict.get(element, 0) + 1
    numb = list(dict.values())
    max_numb = maximum(numb)
    moda = []
    for key, val in dict.items():
        if val == max_numb:
            moda.append(key)
    return tuple(moda) ## обязательно выдавать кортэж как в примере? Чем не подходит просто список?

moda([100, 3, 100, 2, 45, 45, 45, 3, 45, 3, 3, -2, 4])
moda([1, 2, 3, 4, 5, 6, 7, 8, 9])


## Task 7. Функцию, берущую указанный элемент из коллекции
def get(collection, elem_pos):
    return collection[elem_pos]