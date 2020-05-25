from Bio import SeqIO
import argparse

# Argparse part
parser = argparse.ArgumentParser(prog='my_trimmomatic', description='Awesome my own trimmomatic')
parser.add_argument('reads_input', type=str, metavar='reads', help='fastq file with reads')
parser.add_argument('-b', '--begin', default=0, type=int, metavar='INT',
                    help='number of nucleotides that should be clipped at the begining of the read')
parser.add_argument('-f', '--finish', default=0, type=int, metavar='INT',
                    help='number of nucleotides that should be clipped at the end of the read')
parser.add_argument('-q', '--qual_lim', default=30, type=int, metavar='INT', help='quality threshold')
parser.add_argument('-o', '-output', default='trim_out.fastq', type=str, metavar='fastq_name',
                    help='fastq file with trimmed reads')

args = parser.parse_args()
args = args.__dict__
# print(args)


## Сделайте небольшой аналог триммоматика, который может отрезать нуклеотиды в начале последовательностей, в конце,
# удалять фрагменты с концов со средним качеством ниже указанного (25 баллов)

def my_trimmer(fastq_file, begin=0, finish=0, limqual=30, trim_fastq_file='trim_out.fastq'):
    trim_rec = []  # list for trimmed records
    fastq = SeqIO.parse(fastq_file, "fastq")
    for record in fastq:
        rec_len = len(record)
        # ends clipping
        clip_record = record[begin:(rec_len-finish)]
        # clipping by quality
        start = 0
        clip_rec_len = len(clip_record)
        stop = clip_rec_len
        for i in range(clip_rec_len // 2 + 3):
            qual = clip_record.letter_annotations["phred_quality"][0:i + 1]
            if sum(qual) / len(qual) < limqual:
                start = i
        for j in range(clip_rec_len // 2 + 3):
            rev_record = clip_record[::-1]
            qual = rev_record.letter_annotations["phred_quality"][0:j + 1]
            if sum(qual) / len(qual) < limqual:
                stop = clip_rec_len - j
        trim_rec.append(clip_record[start:stop])
        SeqIO.write(trim_rec, trim_fastq_file, 'fastq')
    return f'результат записан в файл {trim_fastq_file}'

# my_trimmer('Eriparia_1_10K.fq', 30, 10, 10, 'new_trim.fastq')

result = my_trimmer(args['reads_input'], args['begin'], args['finish'], args['qual_lim'], args['o'])
print(result)
