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
def genes(DNA):
    import re
    res = []
    f = True
    while f:
        gene = re.findall('(ATG(...)+?(TAG|TAA|TGA))', DNA)
        if gene and len(gene[0][0]) >= 15: # and not (len(gene[0][0]) % 3) это уже выполнено у re
            res.append(gene[0][0])
        n = DNA.find('ATG')
        DNA = DNA[n + 3:] # обрезаем первый старт-кодон, чтобы найти более короткий ген, если есть старт-кодон внутри предыдущего гена
        if DNA.find('ATG') == -1:
            f = False
    return res

def genseq(DNA):
    DNA = DNA.upper()
    res1 = genes(DNA)
    DNA = DNA.translate(str.maketrans('ATGC', 'TACG'))[::-1]
    res2 = genes(DNA)
    return (res1+res2)

DNA = 'atgAAAAAAATGAAAAAAGAAAAATGACATTTTTAGGGGGGGGGGGGGGGCAT'
genseq(DNA)

DNA = 'atgAAAAAAATGAAAAAAGAAAAATGAAAAAAAGGAAAAATGAAAAAGGGAAAAAAATAAACCCATGCCCCCCTGACCCCATGCCCCCCCCCCCCCCCTAAAAATG'
print(genseq(DNA))

DNA = 'ATGAAAAAAATGAAAAAAGAAAAATGAAAAAAAGGAAAAATGAAAAAGGGAAAAAAATAAACCCATGCCCCCCTGACCCCATGCCCCCCCCCCCCCCCTAAAAATG'
print(genseq(DNA))

seq = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"
print(genseq(seq))
