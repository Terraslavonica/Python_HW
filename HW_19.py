from Bio import SeqIO
from Bio.Seq import Seq
from Bio import pairwise2
from Bio.pairwise2 import format_alignment
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from graphviz import Graph
import networkx as nx
import operator


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
# Пишет в файл следующее
# ><unknown id> <unknown description>
# ATGTAGCTCC



# Task 2. de Bruijn graph-based assembler

# Засунем все функции ниже в одну функцию
def de_bruijn_assembler(reads_input, k=10):
    reads_input = reads_input
    k = k
    kmers = kmersep(reads_input, k)  # разбиваем все риды на k-vths
    de_bruijn_graph, edges_coverage, node_coverage = construct_de_bruijn_graph(kmers)  # строим граф и считаем покрытие
    G = nx.Graph()
    my_graph = []
    for i in de_bruijn_graph.items():  # берем граф, который выдеат функция construct_de_bruijn_graph(kmers)
        my_graph.append(i)
    G.add_edges_from(my_graph)
    components = dfs(G)
    if components != 1:
        print("Мы в такое не умеем еще!")
    else:
        final_seq = graph_way(de_bruijn_graph, node_coverage)
    return final_seq

de_bruijn_assembler('ATGTAGCTCC.fasta', 4)


def kmersep(reads_input, k=10):
    seqs = list(SeqIO.parse(reads_input, 'fasta'))
    k = k
    kmers = []
    for sequense in seqs:
        a = sequense.seq
        for i in range(0, len(a) - k + 1):
            kmers.append(a[i:i + k])
    return kmers

kmers = kmersep('ATGTAGCTCC.fasta', 4)


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
            if k1mer1[1:m] == k1mer2[0:m-1]:
                edge = k1mer1 + k1mer2[-1]
                edges_coverage[edge] = (node_coverage[k1mer1] + node_coverage[k1mer2]) / 2
                if de_bruijn_graph.get(k1mer1) == None:
                    de_bruijn_graph[k1mer1] = k1mer2
                else:
                    de_bruijn_graph[k1mer1] = [de_bruijn_graph[k1mer1], k1mer2]
    return de_bruijn_graph, edges_coverage, node_coverage

de_bruijn_graph, edges_coverage, node_coverage = construct_de_bruijn_graph(kmers)

# Проверка числа компонент связности в графе
def search(vertex, graph, visited):
    """
    Function helper to move in graph
    :param vertex: hashable - current vertex
    :param graph: dict - "adjacency dict" in a form {vertex: [neighbours...]}
    :param visited: dict - dict with visited vertices in a form {vertex: True/False}
    :return:
    """
    # Mark vertex as visited
    visited[vertex] = True

    # Go to other vertex, adjacent to current, if they weren't visited before
    for neighbour in graph[vertex]:
        if not visited[neighbour]:
            search(neighbour, graph, visited)


def dfs(graph):
    """
    Function to apply depth-first search to a graph
    :param graph: dict - "adjacency dict" in a form {vertex: [neighbours...]}
    :return:
    """
    # Create dict of visited vertices
    visited = {v: False for v in graph}

    # Visit all reachable vertices from vertex for all vertices
    q = 0
    for v in graph:
        if not visited[v]:
            q += 1
            search(v, graph, visited)
    return q

dfs(G) # 1

# Случай сборки для 1 компонента связности
def graph_way(de_bruijn_graph, node_coverage):
    # Выстраиваем узлы в правильном порядке
    # Пока присваиваем всем узлам нулевой порядок
    order = {}
    for i in de_bruijn_graph.keys():
        order[i] = 0
    # Ищем по минимальному покрытию стартовый и финальный узел и присваиваем им соответствующие порялки
    edges_coverage_sorted = sorted(node_coverage.items(), key=operator.itemgetter(1))
    cov_min = edges_coverage_sorted[0][1]
    for i in range(len(edges_coverage_sorted)):
        if edges_coverage_sorted[i][1] == cov_min: # и стартовый и финальный узлы имеют минимальное покрытие
            if de_bruijn_graph.get(edges_coverage_sorted[i][0]) != None: # стартовый  узел есть в графе среди ключей (из него выходит стрелка)
                potential_start_node = edges_coverage_sorted[i][0]
            else:
                potential_finish_node = edges_coverage_sorted[i][0] # финального узла нет в графе среди ключей (из него не выходит стрелка)
    nodes_number = len(node_coverage.keys())
    # присваиваем порядки первому и последнему узлу
    order[potential_start_node] = 1
    order[potential_finish_node] = nodes_number
    # присвиваем порядки всем остальным узлам
    while min(order.values()) == 0:
        for i in de_bruijn_graph.keys():
            if order[i] != 0:
                his_val = de_bruijn_graph[i]
                order[his_val] = order[i]+1
    # собираем последовательность по порядку узлов
    order_sorted = sorted(order.items(), key=operator.itemgetter(1))
    final_seq = order_sorted[0][0]
    for k in range(1, len(order_sorted)):
        final_seq += order_sorted[k][0][-1]
    return final_seq

graph_way(de_bruijn_graph, node_coverage)
# Seq('ATGTAGCTCTCC', SingleLetterAlphabet()) Собирает как надо :)



## Task 3. Сравнить результаты работы сборщиков
# Собирают одинаково хорошо простейший случай


# Task 4. Graph visualization
G = nx.Graph()
my_graph = []
for i in de_bruijn_graph.items(): # берем граф, который выдеат функция construct_de_bruijn_graph(kmers)
    my_graph.append(i)
G.add_edges_from(my_graph)
nx.draw(G, with_labels=True)
