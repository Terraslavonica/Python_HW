# Task 1. Напишите по 3 примера использования map и filter на произвольных коллекциях -
# отпроцессируйте их элементы и отфильтруйте как вам угодно, для визуализации оберните результат в лист
# map
a = (1, 3, 100, -1, 60, -10.5) #1
a_map = map(lambda x: x*x, a)
list(a_map)

l = ['one', 'two', 'three', 'four'] #2
l_map = list(map(list, l))
list(l_map)

num1 = range(1, 10) #3
num2 = range(100, 200)
res = map(lambda x, y: y - x, num1, num2)
list(res)
# [99, 99, 99, 99, 99, 99, 99, 99, 99] Почему не заругался? Его не волнует, что в num2 есть еще значения?

# filter
stroka = ['privet','','poka','dobroe ytro','!', ' ', ''] #1
ss = filter(None, stroka)
list(ss)

sch = [1, -4, 6, 8, -10, 1.5, -1.8, -100] #2

def my_abs(x):
    if x > 0:
        return 1
    else:
        return 0

b = filter(my_abs, sch)
list(b)

string = [-1, '', 0, 'privet', 1, ' ', 0, '!', 0, '0', 1, 0, -1] #3
my_result = filter(None, string)
list(my_result)

# Напишите генератор, осуществляющий считывание фасты и возвращающий по 1-ой оттранслированной последовательности
# input
# путь до фасты
# таблица кодонов - 'Standard' по умолчанию
# output
# протеиновый Seq
# (12 баллов)
#
# Сгенерируйте 52-карточную колоду (состоящую из кортежей типа (ранг, масть) с помощью приблуд из itertools - в вашем распоряжении iterable с рангами (2..10, J..A) и мастями (H, C, S, D) (10 баллов)
# Сделайте функцию-генератор, генерирующую все ДНКовые последовательности до длины n (аккуратно, не вызывайте её с n > 8)
# list(generate(2))
# ['A', 'T', 'G', 'C', 'AA', 'AT', 'AG', 'AC', 'TA', 'TT', 'TG', 'TC',
# 'GA', 'GT', 'GG', 'GC', 'CA', 'CT', 'CG', 'CC']
# (15 баллов)