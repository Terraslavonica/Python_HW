from Bio.Alphabet import generic_rna
from Bio.Seq import Seq
from numbers import Number
from Bio import SeqIO
import matplotlib.pyplot as plt

# Tesk 1. Сделайте небольшой класс, описывающий какую-то сущность на ваш выбор (организм/тип данных/что-то ещё).
# В классе должен быть конструктор и пара методов (10 баллов)

class MoneyBox: ## Можно я тут заюзаю мировую задачу со стеика? Мне понадобилось, наеврное, полчаса, чтобы эта простейшая задача решилась
    def __init__(self, capacity):
        """
        Class MoneyBox
        :param capacity: the volume of MoneyBox, which is empty at the beginning
        """
        self.count = 0
        self.capacity = capacity

    def can_add(self, v):
        """
        This function help to check if we can add to the MoneyBox v coins
        :param v: int - number of coins
        :return: bul - True if we can put v coins (have enough space in the MoneyBox), and False if not
        """
        if self.count + v <= self.capacity:
            return True
        else:
            return False # Здесь нужен else потому что нам нужно знать в явном виде, можем ли мы добавть сумму в скобках в копилку
                        # если мы уберем else, то ничего не будем получать при добавлении в копилку недопустимой суммы

    def add(self, v):
        """
        Add v coins to our MoneyBox if we have enough space in the MoneyBox
        :param v: int - number of coins
        :return: total number of coins in the MoneyBox
        """
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
        self.protseq = self.rnaseq.translate(table=table)
        return self.protseq

    def bts(self):
        '''
        Function making back translation, i.e. cDNA from RNA sequence
        :return: cDNA sequence
        '''
        self.back = self.rnaseq.back_transcribe()
        return self.back


x = RnaClass("AUGAUAGCAGUU")
x.rnaseq

x.tl()
RnaClass.tl(x)

x.bts()
x.bts

y = RnaClass('AGUACACUGGUU')
y.tl()
y.bts()



# Task 3.  Напишите класс, унаследовавшись от сэтов, который будет содержать в себе только положительные числа при
# создании и не будет добавлять неположительные элементы (подсказка - методы конструктора и add) (10 баллов)

class PositiveSet(set):

    def __init__(self, vals = ''):
        super().__init__()
        self.vals = vals
        for val in self.vals:
            if isinstance(val, Number) and val > 0:
                super().add(val)

    def add(self, other):
        if isinstance(other, Number) and other > 0:
            self.update([other])

d = PositiveSet([10,2,3])
print(d) # PositiveSet({3, 10, 2})
f = PositiveSet()
f.add(3)
f.add(-4)
f.add('may')
print(f) # PositiveSet({3})
# but!!!
f.update('may')
print(f) # PositiveSet({'m', 3, 'a', 'y'}) # как я поняла, так задумано. Если нет, переписать апдейт можно аналогично add



# Task 4. Создайте класс для сбора статистик по фастам. Входные параметры: # путь к фаста файлу
# Методы:
# подсчёт числа последовательностей в фаста файле
# построение гистограммы длин последовательностей
# подсчёт GC состава
# построение гистограммы частоты 4-меров
# переопределение метода для вывода информации при принте (достаточно текста с указанием путя к файлу)
# выполнение всех реализованных методов по подсчёту метрик
# можно придумать дополнительные метрики и реализовать их (5 * число_методов)

class FastaStat:
    def __init__(self, inp):
        """
        Way to fasta
        :param inp: the way to fasta file
        """
        self.way = inp

    def seqnumber(self):
        """
        Count the sequence number in fasta file
        :return: number of sequens
        """
        b = str(self.way)
        seqn = len(list(SeqIO.parse(b, "fasta")))
        return seqn

    def gcpersent(self):
        b = str(self.way)
        seqlen = []
        gclen = []
        for record in SeqIO.parse(b, "fasta"):
            string = record.seq
            seqlen.append(len(string))
            gc = string.count("C") + string.count("G")
            gclen.append(gc)
        N = sum(seqlen)
        n = sum(gclen)
        gc = round((n / N) * 100, 2)
        otvet = str('gc% = {}'.format(gc))
        return otvet

    def lengist(self):
        """
        Function that receives path to fasta, and shows the distribution of the lengths of sequences in it
        :return: histogram of the distribution of the lengths of sequences in fasta
        """
        b = str(self.way)
        dlinyi = []
        for record in SeqIO.parse(b, "fasta"):
            dlinyi.append(len(record.seq))
        gr = plt.hist(dlinyi, bins=40)
        plt.title('distribution of length')
        plt.xlabel('length')
        plt.ylabel('number')
        return gr

    def fourmers(self):
        b = str(self.way)
        fourm = []
        for record in SeqIO.parse(b, "fasta"):
            string = record.seq
            for i in range(0, len(string) - 3):
                fourm.append(string[i:i + 4])
        fourdict = {}
        for element in fourm:
            fourdict[element] = fourdict.get(element, 0) + 1
        freq = []
        for value in fourdict.values():
            freq.append(value)
        four = plt.hist(freq, bins=70)
        plt.title('distribution of 4-mers')
        plt.xlabel('frequency')
        plt.ylabel('number of 4-mers')
        return four

    def __str__(self):
        return (f'It is my awesome fasta file \'{self.way}\'')

    def all(self):
        chislo = self.seqnumber()
        gcsostav = self. gcpersent()
        fig1 = self.lengist()
        fig2 = self.fourmers()
        return fig1, fig2, chislo, gcsostav


a = FastaStat("seqs.fasta")
a.way # seqs.fasta
a.seqnumber()
a.gcpersent()
print(a) # It is my awesome fasta file 'seqs.fasta'
a.lengist()
a.fourmers()
a.all()