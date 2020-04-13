import re
import matplotlib.pyplot as plt

## В этих заданиях нужно пользоваться только регэкспами (без питоновских сплитов и других методов)

# Task 1. Распарсите файл references и запишите оттуда все ftp ссылки в файл ftps (5 баллов)
pat = re.compile('ftp[\.a-zA-Z0-9_#\/@:]+')  # ftp://[user[:password]@]host[:port]/url-path
with open('references.txt', 'r') as file, open('ftps.txt', 'w') as sklad:
        for string in file:
            sklad.write('\n'.join(pat.findall(string)))


# Займёмся парсингом рассказа в файле 2430AD!

## 2  Для начала извлеките оттуда все числа (3 балла)
pat = re.compile('\d+\.?\d+')
with open('2430AD.txt', 'r') as file:
    for string in file:
        if pat.findall(string):
            print(pat.findall(string)) # куда извлечь - не сказано, так что так


## 3 Теперь выберите из текста все слова, в которых есть буква a, регистр при этом не важен (5 баллов)
pat2 = re.compile(r'\w*a\w*', re.I)
with open('2430AD.txt', 'r') as file:
    for string in file:
        if pat2.findall(string):
            print(pat2.findall(string))

## 4 Далее извлеките все восклицательные предложения (10 баллов)
pat3 = re.compile(r'[A-Z].[^.]+?!')
with open('2430AD.txt', 'r') as story:
    for i in story:
        if pat3.findall(i):
            print(pat3.findall(i))

'''
['Yes!']
['Literally!']
['There was once a time!', 'Centuries ago!']
['Think, Cranwitz!']
['If we succeed!']
'''

## 5 А теперь построим гистограмму распределения длин уникальных слов (без учёта регистра, длина от 1) в тексте (15 баллов)

pat4 = re.compile(r'[a-zA-Z\']+')
ans = []
with open('2430AD.txt', 'r') as story:
    for i in story:
        if pat4.findall(i):
            ans.extend(pat4.findall(i))

ans_low = []
for i in ans:
    ans_low.append(i.lower()) # список всех слов без учета регистра

len(ans_low) # 2890

wordset = set(ans_low) # сет из слов, т.е. в нем только уникальные слова
len(wordset) # 933

wordlen = []
for elem in wordset:
    wordlen.append(len(elem))

plt.hist(wordlen, bins=30)
plt.title("distribution of words' lenght")
plt.xlabel('lenght')
plt.ylabel('number of words with that lenght')
plt.show()
# очень красиво :))))



# Task 6. Ну и, куда же без этого - паттерн для поиска email адресов) (10 баллов)
pattern = re.compile(r'[a-zA-Z0-9_\.-]+@[a-z\.]*\.[a-z]*')
emails = str('Terra8908@yandex.ru, e.u.yakovleva@gmail.com, akjd-470@mail.eu, eyakovleva@econ.msu.ru, Hellow world')
pattern.findall(emails)
# ['Terra8908@yandex.ru', 'e.u.yakovleva@gmail.com', 'akjd-470@mail.eu', 'eyakovleva@econ.msu.ru']