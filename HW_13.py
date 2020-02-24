from Bio.Alphabet import generic_rna
from Bio.Seq import Seq

# Tesk 1. Сделайте небольшой класс, описывающий какую-то сущность на ваш выбор (организм/тип данных/что-то ещё).
# В классе должен быть конструктор и пара методов (10 баллов)

class MoneyBox: ## Можно я тут заюзаю мировую задачу со стеика? Мне понадобилось, наеврное, полчаса, чтобы эта простейшая задача решилась
    def __init__(self, capacity):
        self.count = 0
        self.capacity = capacity

    def can_add(self, v):
        if self.count + v <= self.capacity:
            return True
        else:
            return False

    def add(self, v):
        if self.can_add(v):
            self.count += v
        # return self.count

x = MoneyBox(5)
x.count
x.capacity
x.can_add(10)
x.can_add(2)
x.add(2)
x.add(10)
x.count

# Task 2. Напишите класс, описывающий РНК, у него должны быть
# конструктор - принимает последовательность РНК и создаёт объект с ней
# метод трансляции - возвращает строку, соответствующую белку из этой РНК по стандартному коду
# метод обратной транскрипции - возвращает строку, соответствующую ДНК из этой РНК
# подумайте, какие атрибуты должны быть заданы для объекта и класса
class RnaClass:
    def __init__(self, rnaseq):
        self.rnaseq = Seq(rnaseq, generic_rna)

    def tl(self, table = 1):
        '''
        Function making protein from RNA sequence
        :param table: The Genetic Code Table
        :return: protein sequence
        '''
        self.tl = self.rnaseq.translate(table=table)
        return self.tl

    def bts(self):
        '''
        Function making back translation, i.e. cDNA from RNA sequence
        :return: cDNA sequence
        '''
        self.bts = self.rnaseq.back_transcribe()
        return self.bts


x = RnaClass("AUGAUAGCAGUU")
x.rnaseq

# Нормально, что три записи ниже дают ожно и то же?
x.tl()
x.tl
RnaClass.tl(x)

x.bts()
x.bts

y = RnaClass('AGTACACTGGT')
y.tl()
y.tl
y.bts()
y.bts


# Task 3.  Напишите класс, унаследовавшись от сэтов, который будет содержать в себе только положительные числа при
# создании и не будет добавлять неположительные элементы (подсказка - методы конструктора и add) (10 баллов)


# Task 4. Создайте класс для сбора статистик по фастам. Входные параметры: # путь к фаста файлу
# Методы:
# подсчёт числа последовательностей в фаста файле
# построение гистограммы длин последовательностей
# подсчёт GC состава
# построение гистограммы частоты 4-меров
# переопределение метода для вывода информации при принте (достаточно текста с указанием путя к файлу)
# выполнение всех реализованных методов по подсчёту метрик
# можно придумать дополнительные метрики и реализовать их (5 * число_методов)