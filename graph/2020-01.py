import sys
from datastructure import Node, color, Queue, Graph
# dato un grafo G={V,E} e un insieme di di vertici X contenuti in V e due vertici u,v E(V):
# 1)ogni percorso che parte da v e termina in u passa necessariamente per un vertice X
# 2)ogni percorso che parte da u e termina in v passa necessariamente per un vertice X
# verifiche che le seguenti condizioni sono soddisfatte:

# soluzione:
# 1) devo trovare almeno un percorso che parte da v a u e non passa per un vertice X
# 2)devo trovare almeno un percorso che parte da v a u e non passa per un vertice X

#giusto
def notPassTroughX(G: Graph, X: list, u: Node, v: Node):
    # si puo risolvere in problema anche eliminando tutte i vertici di X
    for x in X:
        x.set_color(color.black)
    # ritorna true se esiste un percorso tra u e v e viceversa
    return not G.bfs(v, u) and G.bfs(u, v)


def main():
    # definizione variabili
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    G = Graph(nodeList=[node1, node2, node3, node4, node5])
    X = [node1, node2, node3, node5]
    u = node1
    v = node5
