from Bio import SeqIO
from Bio.Seq import Seq
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from graphviz import Graph
import networkx as nx
import operator
import argparse


# Argparse part
parser = argparse.ArgumentParser(prog='my_trimmomatic', description='Awesome my own trimmomatic')
parser.add_argument('reads_input', type=str, metavar='reads', help='fastq file with reads')
parser.add_argument('-q', '--qual_lim', default = 30, type=int, metavar='INT', help='quality threshold')
parser.add_argument('-o','-output', default = 'trim_out.fastq', type=str, metavar='fastq_name', help='fastq file with trimmed reads')

args = parser.parse_args()
args = args.__dict__
# print(args)


## Сделайте небольшой аналог триммоматика, который может отрезать нуклеотиды в начале последовательностей, в конце,
# удалять фрагменты с концов со средним качеством ниже указанного (25 баллов)

def my_trimmer(fastq_file, limqual = 30, trim_fastq_file='trim_out.fastq'):
    trim_rec = [] # list for trimmed records
    fastq = SeqIO.parse(fastq_file, "fastq")
    for record in fastq:
        rec_len = len(record)
        start = 0
        stop = rec_len
        for i in range(rec_len//2 + 3):
            qual = record.letter_annotations["phred_quality"][0:i+1]
            if sum(qual)/len(qual) < limqual:
                start = i
        for j in range(rec_len//2 + 3):
            rev_record = record[::-1]
            qual = rev_record.letter_annotations["phred_quality"][0:j+1]
            if sum(qual)/len(qual) < limqual:
                stop = rec_len - j
        trim_rec.append(record[start:stop])
        SeqIO.write(trim_rec, trim_fastq_file, 'fastq')
    return f'результат записан в файл {trim_fastq_file}'

result = my_trimmer(args['reads_input'], args['qual_lim'], args['o'])
print(result)