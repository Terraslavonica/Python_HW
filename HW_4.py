# Task 1. Список
spisok = []
spisok += [1, 2.3, 'Pikar', 'zeleniy', 'Pikaya']
print(spisok)
spisok.append([8, 88, 888])
spisochek = ['Stat', 'Python', 'Diskra', 'Proekt', 10, False]
spisok += spisochek
print(spisok)
del spisok[3]
print(spisok)
spisok.remove('Pikaya')
print(spisok)
spisok[1] = 10
print(spisok)

# проверяем, сколько чисел 10 в нашем списке
a = spisok.count(10)
print('таких элементов', a, 'штуки')

dlina = len(spisok)
print('длина:', dlina)


# Task 2. Кортеж
my_tuple = (1, 2.3, 'Pikar', 'zeleniy', 'Pikaya', [8, 88, 888], 'Stat', 'Python', 'Diskra', 'Proekt', 10, False)
print(my_tuple)
# проверяем, сколько чисел 10 в нашем кортеже
print(my_tuple.count(10))

dlina = len(my_tuple)
print(dlina)


# Task 3
friends = ['Asya', 'Nastya', 'Lesha', 'Masha', 'Olya']
for friend in friends:
    print("Hello, "+friend)
print("Hello everyone!")


# Task 4. Напишите программу, поэлементно складывающую две последовательные коллекции (заданных вами) одного размера
list1 = [1, 2, 3]
list2 = [-3, 3, 13]
list_sum = []
q = len(list1)
for i in range(q):
    sumi = list1[i]+list2[i]
    list_sum.append(sumi)
print(list_sum)



# Task 5. Создайте программу, принимающую 3 числа, соответствующих длинам сторон треугольника,
# и выводящую его тип (равнобедренный, разносторонний, равносторонний)
a = int(input('введите сторону a '))
b = int(input('введите сторону b '))
c = int(input('введите сторону c '))
if (a + b < c) or (a + c < b) or (b + c < a):
    print('эти значения не могут быть сторонами треугольника')
else:
    if a == b == c:
        print('равносторонний')
    elif (a == b) or (a == c) or (b == c):
        print('равнобедренный')
    else:
        print('разносторонний')



# Task 6. Разверните лист всеми известными вам способами
elements = [1, 2, ('fruit', 5)]
print(elements)

print(elements[::-1]) ##1

i = len(elements) -1 ##2
elem_inv = []
while i >= 0:
    elem_inv += [elements[i]]
    i -= 1
print(elem_inv)

elements.reverse() ##3
print(elements)


# Task 7. Теперь напишите программу, отбирающую из коллекции чисел только чётные, а затем считающая их сумму
interesting_numbers = (3, 2, 5, 7, 14, 26, 32, 31, 37, 6)
summa = 0
for elem in interesting_numbers:
    if elem % 2 == 0:
        summa += elem
print(summa)