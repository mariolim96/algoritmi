# dato G e un vertice V e due insieme B,C c V
# scrivere un algoritmo che colleziona in una lista
# L tutti i vertici v tc
# 1) v E B e puo raggiunger s tramite un percorso
# esiste un percorso che parte da s a v ma non passa
#  per nessun vertice di C
from datastructure import Stack, Graph, Node, color


def algo(G: Graph, B: set, C: set, s: Node):
    G.init()
    Gt = G.transpose()
    col1 = col2 = {}
    Gt.dfsColor(s, col1)
    L = set()
    for v in C:
        col2[v] = color.BLACK
    G.dfsColor(s, col2)
    for v in B:
        if col1[v] == color.BLACK and col2[v] == color.BLACK:
            L.add(v)
    return L
