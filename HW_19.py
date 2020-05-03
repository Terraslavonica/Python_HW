from Bio import SeqIO
from Bio.Seq import Seq
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from graphviz import Graph
import networkx as nx


# Task 1. Напишите наивный сборщик

def naiveassembler(reads_input, fasta_output, threshold=6):
    seqs = list(SeqIO.parse(reads_input, 'fasta'))
    new_seqs = seqs
    threshold = threshold
    score = {0: 100}
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




# Task 2. de Bruijn graph-based assembler

def kmersep(reads_input, k=10):
    seqs = list(SeqIO.parse(reads_input, 'fasta'))
    k = k
    kmers = []
    for sequense in seqs:
        a = sequense.seq
        for i in range(0, len(a) - k + 1):
            kmers.append(a[i:i + k])
    return kmers


b = kmersep('ATGTAGCTCC.fasta', 4)
#
# for i in b:
#     print(i)

def construct_de_bruijn_graph(kmers):
    # Construct de bruijn graph edges
    de_bruin_graph_edges = set()
    for kmer in kmers:
        de_bruin_graph_edges.add(kmer)

    # Construct de bruijn graph nodes
    k = len(kmers[0])
    de_bruijn_graph_nodes = []
    for edge in kmers:
        de_bruijn_graph_nodes.append(edge[0: k - 1])
        de_bruijn_graph_nodes.append(edge[1: k])
    node_coverage = {}
    for node in de_bruijn_graph_nodes:
        node_coverage[node] = node_coverage.get(node, 0) + 1
    de_bruijn_graph_nodes = list(node_coverage.keys())

    # Construct de bruijn graph edge nodes corresponding to k-1 mers
    m = k - 1
    de_bruijn_graph = {}
    edges_coverage = {}
    for k1mer1 in de_bruijn_graph_nodes:
        for k1mer2 in de_bruijn_graph_nodes:
            if k1mer1[1:m] == k1mer2[0:m - 1]:
                edge = k1mer1 + k1mer2[-1]
                edges_coverage[edge] = (node_coverage[k1mer1] + node_coverage[k1mer2]) / 2
                if de_bruijn_graph.get(k1mer1) == None:
                    de_bruijn_graph[k1mer1] = k1mer2
                else:
                    de_bruijn_graph[k1mer1] = [de_bruijn_graph[k1mer1], k1mer2]
    return de_bruijn_graph, edges_coverage

res = construct_de_bruijn_graph(b)
res[0]
res[1]

# Graph visualization
G = nx.Graph()
my_graph = []
for i in res[0].items():
    my_graph.append(i)
G.add_edges_from(my_graph)
nx.draw(G, with_labels=True)


