import logging
import argparse
from Bio import SeqIO
import networkx as nx
import operator


# Logging part
logging.basicConfig(filename='de_bruijn_assembling.log', filemode='w', format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S', level=logging.DEBUG)
logger = logging.getLogger(__name__)


# Argparse part
parser = argparse.ArgumentParser(prog='de_bruijn_assembler', description='Awesome de Bruijn assembler', epilog='Congratulations, you have a great sense of humor, since you use my program')
parser.add_argument('-i','--reads_input', required=True, type=str, metavar='fasta_name', help='fasta file with reads')
parser.add_argument('-k', default = 5, type=int, metavar='INT', help='leanght of k-mer')
parser.add_argument('-o','-output_contigs', default = 'out_assem.txt', type=str, metavar='txt_name', help='txt file with contigs')

args = parser.parse_args()
args = args.__dict__


# Assembler
# Разделим риды на k-меры
def kmersep(reads_input, k=5):
    seqs = list(SeqIO.parse(reads_input, 'fasta'))
    k = k
    kmers = []
    for sequense in seqs:
        a = sequense.seq
        for i in range(0, len(a) - k + 1):
            kmers.append(a[i:i + k])
    return kmers


def construct_de_bruijn_graph(kmers):
    flag = 0 # если 0, то петель в графе нет, если 1, то в графе петля, дальше сборка невозможна
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
    de_bruijn_graph_nodes = list(node_coverage.keys()) # на этом этапе уичтожаются лишние узлы, это по сути эквивалентно
                                             # дедупликации, хотя можно написать ее и отдельно, может быть допишу
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
                    flag = 1 #"В графе возникла петля, необходимо выбрать большее k"
                    # de_bruijn_graph[k1mer1] = [de_bruijn_graph[k1mer1], k1mer2]
    return de_bruijn_graph, edges_coverage, node_coverage, flag


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


# Случай сборки для 1 компонента связности
def graph_way(de_bruijn_graph, node_coverage):
    # Выстраиваем узлы в правильном порядке
    # Пока присваиваем всем узлам нулевой порядок
    order = {}
    for i in de_bruijn_graph.keys():
        order[i] = 0
    # Ищем по минимальному покрытию стартовый и финальный узел и присваиваем им соответствующие порялки
    edges_coverage_sorted = sorted(node_coverage.items(), key=operator.itemgetter(1))
    # и стартовый и финальный узлы имеют минимальное покрытие
    potential_start_node = str()
    potential_finish_node = str()
    for i in range(0,2):
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


# Соберем сборщик из функций выше
def de_bruijn_assembler(reads_input, k=10, output='out_assem.txt'):
    # Считаем минимальную длину рида, k не должно ее превышать
    seqs = list(SeqIO.parse(reads_input, 'fasta'))
    read_lenght = []
    for s in seqs:
        read_lenght.append(len(s.seq))
    min_read_len = min(read_lenght)

    flag = 1
    k = k - 2 # нужно, чтобы войти в петлю
    while flag == 1:
        k = k + 2 # будем прибвлять к k по 2 нуклеотида, пока не получим граф без петель
        logger.debug('Assembling process with k = %s', k)
        if k <= min_read_len:
            kmers = kmersep(reads_input, k)  # разбиваем все риды на k-меры
            logger.debug('break the reads into k-mers')
            de_bruijn_graph, edges_coverage, node_coverage, flag = construct_de_bruijn_graph(kmers) # строим граф и считаем покрытие
            logger.debug('build the graph')
            if flag == 1:
                logger.debug('too short k-mer, just increase k-mer by 2')
                continue
            else:
                break
        else:
            logger.debug("can't be assembled, too short reads")
            return "Нельзя собрать, удалите слишком короткие риды" # когда k уже длинее ридов, а в графе все равно петли
    G = nx.Graph()
    logger.debug('check the number of components in graph')
    my_graph = []
    for i in de_bruijn_graph.items():
        my_graph.append(i)
    G.add_edges_from(my_graph)
    components = dfs(G)
    if components != 1:
        logger.debug("can't be assembled, more than one component in grapth")
        return "В графе больше 1 компоненты. Мы в такое не умеем еще!"
    else:
        final_seq = graph_way(de_bruijn_graph, node_coverage)
    with open(output, 'w') as file:
        file.write(f'{final_seq}')
        logger.debug(f'writhe the assembled string in file {output}')
    return k, final_seq

logger.info(f"Starting work with {args['reads_input']}...")

k, final_seq = de_bruijn_assembler(args['reads_input'], args['k'], args['o'])
print(k, final_seq)

logger.info("Job's done!")