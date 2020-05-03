from Bio import SeqIO


# Task 1. Сделайте функцию, конвертирующую переданный fastq файл в fasta,
# отбирая только последовательности длиннее заданного числа, по умолчанию 50, input путь к fastq файлу путь к файлу,
# куда будет записана fasta минимальная длина последовательности
def fastqtofasta(input, output, lenmin = 50):
    """
    Function that makes fasta-file from fastq-file
    :param input: str - path to fastq-file
    :param output: str - path to fasta-file
    :param lenmin: int - the length of the sequence, lines longer than lenmin will be written to fasta-file
    :return: fasta-file made from fastq-file
    """
    seqs = list(SeqIO.parse(input, 'fastq'))
    rez = list()
    for i in seqs:
        if len(i.seq) > lenmin:
            rez.append(i)
        SeqIO.write(rez, output, 'fasta')

fastqtofasta('sample.fastq', 'subsample_2.fasta', 5)

# Task 2. Напишите функцию, выполняющую глобальное выравнивание 2-ух последовательностей input путь к фаста файлу
# с 2-мя последовательностями скор за мэтч скор за мисмэтч скор за гэп, output кортеж из скора и строки выравнивания

def zeros(rows, cols):
    """
    A function for making a zero-matrix
    :param rows: int - number of rows
    :param cols: int - number of columns
    :return: zero-matrix
    """
    # Define an empty list
    empty = []
    # Generate the matrix of zeros
    for x in range(rows):
        empty.append([0 for y in range(cols)])
    # Return the matrix of zeros
    return empty

zeros(2,3) # [[0, 0, 0], [0, 0, 0]] работает :)

def nwal(seqs, gap, match, mismatch):
    """
    Function that makes Needleman-Wunsch alignment
    :param seqs: str - path to the fasta-file with two strings that should be aligned
    :param gap: float - penalty for the gap
    :param match: float - award for the match
    :param mismatch: float - penalty for the mismatch
    :return: tuple with score and two aligned strings
    """

    # A function for determining the score between any two bases in alignment
    def match_score(a, b):
        if a == b:
            return match
        else:
            return mismatch

    record = list(SeqIO.parse(seqs, "fasta"))
    seq1 = str(record[0].seq)
    seq2 = str(record[1].seq)

    n = len(seq1)
    m = len(seq2)

    # Generate the matrix of zeros
    score = zeros(m + 1, n + 1)

    # Calculate score table

    # Fill out first column
    for i in range(0, m + 1):
        score[i][0] = gap * i

    # Fill out first row
    for j in range(0, n + 1):
        score[0][j] = gap * j

    # Fill out all other values in the score matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            # Calculate the score by checking the top, left, and diagonal cells
            matched = score[i - 1][j - 1] + match_score(seq1[j - 1], seq2[i - 1])
            delete = score[i - 1][j] + gap
            insert = score[i][j - 1] + gap
            # Record the maximum score from the three possible scores calculated above
            score[i][j] = max(matched, delete, insert)

    # Traceback and compute the alignment

    # Create variables to store alignment
    align1 = ""
    align2 = ""

    # Start from the bottom right cell in matrix
    i = m
    j = n

    # We'll use i and j to keep track of where we are in the matrix, just like above
    while i > 0 and j > 0:  # end touching the top or the left edge
        score_current = score[i][j]
        score_diagonal = score[i - 1][j - 1]
        score_up = score[i][j - 1]
        score_left = score[i - 1][j]

        # Check to figure out which cell the current score was calculated from,
        # then update i and j to correspond to that cell.
        if score_current == score_diagonal + match_score(seq1[j - 1], seq2[i - 1]):
            align1 += seq1[j - 1]
            align2 += seq2[i - 1]
            i -= 1
            j -= 1
        elif score_current == score_up + gap:
            align1 += seq1[j - 1]
            align2 += '-'
            j -= 1
        elif score_current == score_left + gap:
            align1 += '-'
            align2 += seq2[i - 1]
            i -= 1

    # Finish tracing up to the top left cell
    while j > 0:
        align1 += seq1[j - 1]
        align2 += '-'
        score_current += gap
        j -= 1
    while i > 0:
        align1 += '-'
        align2 += seq2[i - 1]
        score_current += gap
        i -= 1

    # Since we traversed the score matrix from the bottom right, our two sequences will be reversed.
    # These two lines reverse the order of the characters in each sequence.
    align1 = align1[::-1]
    align2 = align2[::-1]

    rez = (score_current, align1 + "\n" + align2)

    return rez

print(*nwal('test.fasta', -1, 1, -1), sep='\n') # (1, 'CAT\nCAR')
print(*nwal('test1.fasta', -1, 0, -1), sep='\n') # (0, 'CATCATCARACT\nCARDOGC--A-T')
print(*nwal('subsample_2.fasta', -1, 0, -2), sep='\n')
# 0 за гэп - ну туповато получается, мисметчи как результат мутации вполне вероятны, даже больше, чем инделы, при последних же рамка считывания едет :)
print(*nwal('test.fasta', 0, 1, -1), sep='\n') # (1, 'CA-T\nCAR-')
print(*nwal('test1.fasta', 0, 0, -1), sep='\n') # (0, '------CATCATCARACT\nCARDOG------C--A-T')
print(*nwal('subsample_2.fasta', 0, 0, -2), sep='\n')

# Task 3. *Напишите функцию, выполняющую локальное выравнивание 2-ух последовательностей input путь к фаста файлу
# с 2-мя последовательностями скор за мэтч скор за мисмэтч скор за гэп output кортеж из скора и строки выравнивания