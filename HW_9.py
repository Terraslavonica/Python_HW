# Task 1. Сделайте функцию, конвертирующую переданный fastq файл в fasta,
# отбирая только последовательности длиннее заданного числа, по умолчанию 50, input путь к fastq файлу путь к файлу,
# куда будет записана fasta минимальная длина последовательности
def fastqtofasta(iz, v, lenmin = 50):
    """
    Function that makes fasta-file from fastq-file
    :param iz: str - path to fastq-file
    :param v: str - path to fasta-file
    :param lenmin: int - the length of the sequence, lines longer than lenmin will be written to fasta-file
    :return: fasta-file made from fastq-file
    """
    from Bio import SeqIO
    seqs = list(SeqIO.parse(iz, 'fastq'))
    rez = list()
    for i in seqs:
        if len(i.seq) > lenmin:
            rez.append(i)
        SeqIO.write(rez, v, 'fasta')

fastqtofasta('sample.fastq', 'subsample_2.fasta')

# Task 2. Напишите функцию, выполняющую глобальное выравнивание 2-ух последовательностей input путь к фаста файлу
# с 2-мя последовательностями скор за мэтч скор за мисмэтч скор за гэп, output кортеж из скора и строки выравнивания



# Task 3. *Напишите функцию, выполняющую локальное выравнивание 2-ух последовательностей input путь к фаста файлу
# с 2-мя последовательностями скор за мэтч скор за мисмэтч скор за гэп output кортеж из скора и строки выравнивания

