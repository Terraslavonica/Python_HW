# Task 1
## из целых в дробные
i = 5
while i > 0:
    a = int(input('Введите целое число '))
    print('тип введенного числа:', type(a), '\n', 'преобразованное число:', float(a), 'его тип:', type(float(a)), '\n')
    i -= 1

## из дробных в целые
i = 5
while i > 0:
    a = float(input('Введите дробное число '))
    print('тип введенного числа:', type(a), '\n', 'преобразованное число:', int(a), 'его тип:', type(int(a)), '\n')
    i -= 1

## из целого в строку
i = 5
while i > 0:
    a = int(input('Введите целое число '))
    print('тип введенного числа:', type(a), '\n', 'преобразованное число:', str(a), 'его тип:', type(str(a)), '\n')
    i -= 1

## из дробного в строку
i = 5
while i > 0:
    a = float(input('Введите дробное число '))
    print('тип введенного числа:', type(a), '\n', 'преобразованное число:', str(a), 'его тип:', type(str(a)), '\n')
    i -= 1

## из строки в целое
i = 5
while i > 0:
    a = input('Введите число ')
    print('тип введенного числа:', type(a), '\n', 'преобразованное число:', int(float(a)),
          'его тип:', type(int(float(a))), '\n')
    i -= 1

## из строки в дробное
i = 5
while i > 0:
    a = input('Введите число ')
    print('тип введенного числа:', type(a), '\n', 'преобразованное число:', float(a), 'его тип:', type(float(a)), '\n')
    i -= 1


# Task 2. Три формулы
##1 Формула аннуитета. Позволяет вычислить размер ежемесячного платежа по кредиту,
# зная сумму кредита, годовую процентную ставку и срок кредита
K = float(input('Введите сумму кредита в рублях '))
P = float(input('Введите годовую процентную ставку, например, 10 '))
N = float(input('Введите срок кредита в годах '))
p = P/(12*100) # рассчитываем процентную ставку в долях и в расчете на месяц
n = N*12 #рассчитываем количество месяцев, т.к. аннуитетный платеж по кредиту, как правило, ежемесячный
A = (K*p*((1 + p)**n))/(((1 + p)**n) - 1)
S = A*n
print('Сумма ежемесячного платежа: ', A, ' рублей', '\n'+
      'Сумма выплат (тело кредита и проценты)', S, 'рублей')
'''
Пример:
Введите сумму кредита в рублях >? 1000
Введите годовую процентную ставку, например, 10 >? 12
Введите срок кредита в годах >? 1
Сумма ежемесячного платежа:  88.84878867834168  рублей 
Сумма выплат (тело кредита и проценты) 1066.1854641401 рублей
На первый взгляд парадоксально, что Сумма выплат не равна 1120 рублям, но это ок,
это потому, что проценты начисляются ежемесячно на непогашенную сумму кредита
'''

##2 Площадь трапеции через четыре ее стороны
a, b = input('Введите основания трапеции через пробел ').split()
c, d = input('Введите боковые стороны трапеции через пробел ').split()
a = float(a)
b = float(b)
c = float(c)
d = float(d)
S = ((a + b) / 2)*((c*c - (((b-a)**2 + c*c - d*d)/(2*b - 2*a))**2)**0.5)
print(S)
'''
Пример:
Введите основания трапеции через пробел >? 2 4
Введите боковые стороны трапеции через пробел >? 3 4
8.714212528966687
'''

##3 Сила притяжения мужду двумя телами с известной массой, расположенных на определенном расстоянии друг от друга
m1, m2 = input('Введите массы двух тел в кг через пробел ').split()
r = int(input('Введите расстояние между телами в м '))
m1 = int(m1)
m2 = int(m2)
F = 6.7385*10e-11 * m1 * m2 / (r*r)
print(F, 'H') # в Ньютонах
'''
Пример:
Введите массы двух тел в кг через пробел >? 100000 2000000
Введите расстояние между телами в м >? 1
134.77 H
'''


# Task 3. Таблица истинности
oper = input('введите операцию, таблицу истинности для которой Вы хотите получить ')
print('   ', oper+':')
if oper == 'not':
    print("T   ->", not True, "\n"+"F   ->", not False)
elif oper == 'or':
    print("T,T   ->", True or True, "\n"+"T,F   ->", True or False,
          "\n"+"F,T   ->", False or True, "\n"+"F,F   ->", False or False)
elif oper == 'xor':
    print("T,T   ->", not (True or True), "\n"+"T,F   ->", True or False,
          "\n"+"F,T   ->", False or True, '\n'+"F,F   ->", False and False)
elif oper == 'nor':
    print("T,T   ->", not (True or True), "\n"+"T,F   ->", not (True or False),
          "\n"+"F,T   ->", not (False or True), '\n'+"F,F   ->", not (False or False))
elif oper == 'and':
    print("T,T   ->", True and True, "\n"+"T,F   ->", True and False,
          "\n"+"F,T   ->", False and True, "\n"+"F,F   ->", False and False)
elif oper == 'nand':
    print("T,T   ->", not (True and True), "\n"+"T,F   ->", not (True and False),
          "\n"+"F,T   ->", not (False and True), '\n'+"F,F   ->", not (False and False))


# Task 4. Вариация старой задачки fizzbuzz - сделайте программу, на вход которой поступает целое число,
# если это число делится на 3 выводится fizz, если на 5 - buzz,
# а если на 15 - fizzbuzz. Если не делится нацело ни на одно из них, выведите это же число (8 баллов)

number = int(input('Введите целое число '))
if number % 3 == 0 and number % 5 != 0:
    print("fizz")
elif number % 3 != 0 and number % 5 == 0:
    print("buzz")
elif number % 15 == 0:
    print("fizzbuzz")
else:
    print(number)