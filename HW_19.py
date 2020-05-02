from Bio import SeqIO
from Bio.Seq import Seq
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO


# Task 1. Напишите наивный сборщик

def naiveassembler(fastq_input, fasta_output, threshold=6):
    seqs = list(SeqIO.parse(fastq_input, 'fasta'))
    new_seqs = seqs
    threshold = threshold
    score = {0:100}
    while (len(new_seqs) != 1) and (max(score.values()) >= threshold):
        score = {}
        a = new_seqs[0].seq
        for j in range(1, len(new_seqs)):
            b = new_seqs[j].seq
            aln = pairwise2.align.localms(a, b, 1, -1, -1, -1)
            if aln:
                aln = aln[0]
                score[j] = aln[2]
            else:
                score[j] = 0
        for k in sorted(score, key=score.get, reverse=True):
            if score[k] >= threshold:
                pair_pos = k
                c = new_seqs[pair_pos].seq
                aln_true = pairwise2.align.localms(a, c, 1, -1, -1, -1)[0]
                fragment = aln_true[0][aln_true[3]:aln_true[4]]
                flag_len = aln_true[4] - aln_true[3]
                if (a.endswith(fragment) and c.startswith(fragment)):
                    new_seqs.pop(pair_pos)
                    new_seqs.pop(0)
                    new_seqs.append(SeqRecord(a + c[flag_len:]))
                    break
                elif (c.endswith(fragment) and a.startswith(fragment)):
                    new_seqs.pop(pair_pos)
                    new_seqs.pop(0)
                    new_seqs.append(SeqRecord(c + a[flag_len:]))
                    break
            else:
                temp = new_seqs[0]
                new_seqs.pop(0)
                new_seqs.append(temp)
    SeqIO.write(new_seqs, fasta_output, 'fasta')

naiveassembler('ATGTAGCTCC.fasta', 'output_ATGTAGCTCC.fasta', 2)


