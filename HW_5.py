# Task 1.
## Создайте пустой сэт, добавьте к нему несколько элементов разных типов,
my_set = set()
my_set.add(2)
my_set.add(5.0)
my_set.add(2)
my_set.add(True)
my_set.add('kuku')
my_set

# а также проведите сэтовые операции над парой сэтов:
your_set = {False, 2, 5.0, 'kuku', 'sinhrofazotron'}
le_troisieme = {'blanc', 'verte', 'kuku', 1, 0, 1.0}
your_set.update(my_set)  # объединение
your_set
your_set.intersection_update(le_troisieme) # пересечение
your_set
le_troisieme.difference_update(my_set) # вычитание
le_troisieme

s = {1, 2, 3, 4, 5}
s.symmetric_difference({4,5,6,7,8,0, True}) # симметричное вычитание
s
2 in s # проверку на вхождение одного сэта в другой
{2, 3}.issubset(s)

# Task 2.
## Создайте пустой словарь,
slovar = {}
# заполните его элементами,
slovar['green'] = 'vert'
slovar['red'] = 'rouge'
slovar['white'] = 'blanc'
slovar['blue'] = 'blue'
slovar['black'] = 'noir'
slovar['five'] = 5
slovar
# удалите часть элементов,
slovar.pop('black')
del slovar['white']
slovar
# обратитесь к нескольким элементам и сделайте с ними какое-нибудь действие
slovar['green'] = [slovar['green'], 'verde']
slovar['red'] += ' and vermelho'
slovar['five'] *= 2
slovar

# Task 3.
## Проитерируйтесь по заданному вами словарю и выведите его ключи и элементы (какой способ кажется вам лучшим?) (5 баллов * число способов)
for k in slovar:
    print (k, '-', slovar[k]) # мой любимый способ, удовлетворяет принцыпу бритвы Оккама

for k in slovar.keys():
    print (k, '-', slovar[k])

for k,v in slovar.items():
    print (k, '-', v)

# Task 4.
## Создайте программу, принимающую на вход строку и выводящую, начинается ли строка с заглавной буквы
my_str = "There's a fire starting in my heart. Reaching a fever pitch and it's bringing me out the dark!!!"
my_str[0].isupper()
# число букв в строке
len(my_str)
# заканчивается ли она на '!!'
my_str[-2:] == "!!"
# число встречаний строки 'fire'
my_str.count('fire')
# эту же строку, где все буквы большие
my_str.upper()
# маленькие
my_str.lower()
# все слова начинаются с большой буквы
my_str.title()

# Task 5.
# Напишите программу, принимающую на вход строку и выводящую с чего эта строка начинается (цифра, буква, пробел) (5 баллов)
my_str = "There's a fire starting in my heart. Reaching a fever pitch and it's bringing me out the dark!!!"
if my_str[1].isalpha():
    print('Start by letter')
elif my_str[1].isdigit():
    print('Statr by digit')
elif my_str[1].isspace():
    print('Start by space')

# Task 6.
# Сконвертируйте список, кортеж, сэт и строку друг в друга всеми возможными способами (строка -> лист, строка -> кортеж, ...) (6 баллов)
stroka = 'lavieestbelle' ## строка -> сэт (множество)
set(stroka)

stroka = 'lavieestbelle' ## строка -> список
list(stroka)

stroka = 'lavieestbelle' ## строка -> кортеж
tuple(stroka)

my_list = ['Kate', 'Masha', 'Nastya', 'Pasha', 'Sascha'] ## список -> строка
str(my_list)

my_list = ['Kate', 'Masha', 'Nastya', 'Pasha', 'Sascha'] ## список -> кортеж
tuple(my_list)

my_list = ['Kate', 'Masha', 'Nastya', 'Pasha', 'Sascha'] ## список -> сэт (множество)
set(my_list)

korteg = ('un', 'deux', 'trois', 'quatre', 'cinq') ## кореж -> список
list(korteg)

korteg = ('un', 'deux', 'trois', 'quatre', 'cinq') ## кореж -> строку
str(korteg)

korteg = ('un', 'deux', 'trois', 'quatre', 'cinq') ## кореж -> сэт (множество)
set(korteg) ## не умеет считать по-французски даже до пяти, выдает числа в самом дурацком порядке :Р

mnogestvo = {'un', 'deux', 'trois', 'quatre', 'cinq', 'Un', 'Deux', 'Trois', 'Quatre', 'Cinq'} ## сэт -> список
list(mnogestvo)

mnogestvo = {'un', 'deux', 'trois', 'quatre', 'cinq', 'Un', 'Deux', 'Trois', 'Quatre', 'Cinq'} ## сэт -> строка
str(mnogestvo)

mnogestvo = {'un', 'deux', 'trois', 'quatre', 'cinq', 'Un', 'Deux', 'Trois', 'Quatre', 'Cinq'} ## сэт -> кортеж
tuple(mnogestvo)


# Task 7.
# Разверните строку всеми известными вам способами
s = 'agatacaca'

s[::-1] ##1

i = len(s) - 1 ##2
s_inv = str()
while i >= 0:
    s_inv += s[i]
    i -= 1
print(s_inv)


# Task 8.
# Напишите реверскомплементатор (чем больше способов, тем лучше), на вход подаётся строка ДНК,
# нужно чтобы выводился реверскомплемент заглавными буквами
DNA = 'AGCATTCGAGCATCCTAGCGG'
DNA.translate(str.maketrans('ATGC', 'UACG'))