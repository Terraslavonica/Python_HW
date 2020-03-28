from itertools import *
import numpy as np
from Bio import SeqIO

# Task 1. Напишите по 3 примера использования map и filter на произвольных коллекциях -
# отпроцессируйте их элементы и отфильтруйте как вам угодно, для визуализации оберните результат в лист
# map
a = (1, 3, 100, -1, 60, -10.5) #1
a_map = map(lambda x: x * x, a)
list(a_map)

l = ['one', 'two', 'three', 'four'] #2
l_map = list(map(list, l))
list(l_map)

num1 = range(1, 10) #3
num2 = range(100, 200)
res = map(lambda x, y: y - x, num1, num2)
list(res)
# [99, 99, 99, 99, 99, 99, 99, 99, 99] Не заругался. Его не волнует, что в num2 есть еще значения?

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


# Task 2. Напишите генератор, осуществляющий считывание фасты и возвращающий по 1-ой оттранслированной последовательности
# input: путь до фасты, таблица кодонов - 'Standard' по умолчанию
# output: протеиновый Seq

def transseq(fromfile, table = 1):
    prot = []
    for record in SeqIO.parse(fromfile, "fasta"):
        coding_dna = record.seq
        prot.append(coding_dna.translate(table=table))
    yield prot

# Надеюсь, это то, что нужно...
transseq('seqs.fasta')
# <generator object transseq at 0x000001D42053A740>
list(transseq('seqs.fasta'))
# оч длинные там белки получаются

transseq("testHW12.fasta")
# <generator object transseq at 0x000001D42053A740>
list(transseq("testHW12.fasta")) # тут "белки" покороче
# [[Seq('MNHDF', ExtendedIUPACProtein()), Seq('MNHDFQAL', ExtendedIUPACProtein()), Seq('MNHXXX', ExtendedIUPACProtein()), Seq('MNHDFQAKKKKKK', ExtendedIUPACProtein())]]


# Task 3. Сгенерируйте 52-карточную колоду (состоящую из кортежей типа (ранг, масть) с помощью приблуд из itertools -
# в вашем распоряжении iterable с рангами (2..10, J..A) и мастями (H, C, S, D)
cards = list(product(("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "A", "K", "Q"), ("H", "C", "S", "D"))) # карты по порядку

nominal = list()
guys = ("J", "A", "K", "Q")
for i in (range(2, 11)):
    nominal.append(str(i))
for j in guys:
    nominal.append(j)
cards = list(product(nominal, ("H", "C", "S", "D"))) # карты по порядку 2

guys = ("J", "A", "K", "Q")
cards = list(product((chain((str(x) for x in range(2, 11)), guys)), ("H", "C", "S", "D"))) # карты по порядку 3


# Сгенерила колоду рандомно
carddeck = []
a = np.random.choice(range(0, 52), 52)
for i in a:
    carddeck.append(cards[i])
print(carddeck) # вот)


# Task 4. Сделайте функцию-генератор, генерирующую все ДНКовые последовательности до длины n (аккуратно, не вызывайте её с n > 8)
# list(generate(2))
# ['A', 'T', 'G', 'C', 'AA', 'AT', 'AG', 'AC', 'TA', 'TT', 'TG', 'TC',
# 'GA', 'GT', 'GG', 'GC', 'CA', 'CT', 'CG', 'CC']

def generate(n):
    '''
    Function generating all DNA sequences up to length n
    :param n: int - the maximum length of DNA sequence
    :return: generator of sequences
    '''
    nucleotides = ['A', 'T', 'G', 'C']
    iterable = []
    bl = ''
    for i in range(1, n+1):
        a = map(lambda x: bl.join(x), product(nucleotides, repeat=i))
        for k in a:
            iterable.append(k)
    yield iterable

list(generate(1))
list(generate(2))
list(generate(3))
list(generate(8))