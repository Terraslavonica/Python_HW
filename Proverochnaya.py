## 1. Сортировка пузырьком. Функция должна принимать на вход список и выдавать его отсортированным
def BSort(s):
    """
    Function which makes bubble sorting
    :param s: your list that should be sorted
    :return: sorted list
    """
    for i in range(len(s) - 1, 0, -1):
        for j in range(i):
            if s[j] > s[j + 1]:
                s[j], s[j+1] = s[j+1], s[j]
    return s

s = [111, 4, 46, 3, 27, 56, 1, 45, 21, 70, 61]
print(BSort(s))

a = [1, 4, 46, 3, 27, 56, 1, 45, 21, 70, 61, 0, -1000]
print(BSort(a))


##2. Поиск генов в строке ДНК
def genseq(DNA):
    string = DNA
    f = True
    genes = [] # в это вектор будем записывать гены
    while f:
        start = string.find('ATG') # ищем старт-кодон
        if start == -1: # если не нашли, то переходим на return
            break
        string = string[start + 3:] # отрежем старт-кодон, чтобы два последних нуклеотида в нем не совпали со стоп-кодоном 'TGA'
        # также это удобно при проверке триплетности
        fn = BSort([string.find('TAA'), string.find('TAG'), string.find('TGA')]) # отсортируем позиции возможных стопкодонов
        if fn == []: # если не нашли ни одного стоп-кодона, то переходим на return
            break
        stop = 0
        for i in fn:
            if i > 0 and i >= 9 and not (i % 3): # если ген достаточно длинный, то берем ближайший стоп-кодон и идем дальше
                genes.append('ATG' + string[0: i + 3])
                stop = i
                break
            if i > 0 and i < 12 and not (i % 3): # здесь отсекаем случаи коротких генов + проверяем, чтобы рамка считывания не сдвигалась, отрезаем
                string = string[i + 3:]
                break
        if stop == 0: # если не нашли отвечающий условиям стоп-кодон, ищем следующий старт-кодон
            continue
    return genes


string = 'ATGAAAAAAATGAAAAAAGAAAAATGAAAAAAAGGAAAAATGAAAAAGGGAAAAAAATAAACCCATGCCCCCCTGACCCCATGCCCCCCCCCCCCCCCTAAAAATG'
          ATGAAAAAAATGAAAAAAAAAAAATGAAAAAAAAAAAAAATGAAAAAGGGAAAAAAATAA
print(genseq(string))
