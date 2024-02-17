from operator import itemgetter
from read_database import get_nodes_and_edges

class DisjointSet(dict):
    def add(self, item):
        # Adiciona um novo item ao conjunto
        self[item] = item

    def find(self, item):
        # Encontra o representante (raiz) do conjunto ao qual 'item' pertence
        pai = self[item]
        while self[pai] != pai:
            pai = self[pai]
        # Compressão de caminho para otimizar futuras operações de busca
        self[item] = pai
        return pai

    def union(self, item1, item2):
        # Realiza a união, tornando um item o pai do outro
        self[item2] = self[item1]

def kruskal(nodes, edges):
    # Inicializa um conjunto disjunto (forest) e uma árvore geradora mínima (mst) vazia
    forest = DisjointSet()
    mst = []

    # Adiciona cada nó ao conjunto disjunto (forest)
    for n in nodes:
        forest.add(n)

    # Inicializa o tamanho da árvore geradora mínima (mst) como o número de nós - 1
    sz = len(nodes) - 1

    # Ordena as arestas com base em seus pesos em ordem crescente
    for e in sorted(edges, key=itemgetter(2)):
        n1, n2, _ = e
        # Encontra os conjuntos aos quais os nós pertencem
        t1 = forest.find(n1)
        t2 = forest.find(n2)
        # Se os nós estão em conjuntos diferentes, adiciona a aresta à árvore geradora mínima (mst)
        if t1 != t2:
            mst.append(e)
            sz -= 1
            # Se a árvore geradora mínima (mst) estiver completa, retorna-a
            if sz == 0:
                return mst
            # Realiza a união dos conjuntos dos dois nós
            forest.union(t1, t2)

# Teste
#recebendo os nós e arestas da base de dados
infos = get_nodes_and_edges()
nodes, edges = infos[0], infos[1]            

#criando uma lista apenas com as labels dos nós, para ser adicionada no grafo
formated_nodes = []
for node in nodes:
    formated_nodes.append(node['id'])

print(formated_nodes)
print(edges)
# nodes = list("ABCDEFG")
# edges = [("A", "B", 7), ("A", "D", 5),
#          ("B", "C", 8), ("B", "D", 9), ("B", "E", 7),
#          ("C", "E", 5),
#          ("D", "E", 15), ("D", "F", 6),
#          ("E", "F", 8), ("E", "G", 9),
#          ("F", "G", 11)]

print(kruskal(formated_nodes, edges))