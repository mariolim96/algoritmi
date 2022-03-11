# dato un grafo G e due vertici uv e un insieme A C V
# scrivere un algoritmo che dato in ingresso il grafo G e i due vertici uv
# calcola l'insieme Z tali che :
# 1) z E A  ossia Z C A
# 2) ogni percorso che parte da u e raggiunge v non passa per z

from .datastructure import Stack, Graph, Node, color
# u->A
# Gt : z->A
# prendere tutti i bianchi


def algo(G: Graph, A: set, u: Node, v: Node):
    Z = A
    Gt = G.transpose()
    G.init()
    Gt.init()
    col1 = col2 = {}
    G.dfs(u, col1)
    Gt.dfs(v, col2)
    for z in Z:
        if col1[z] == color.BLACK and col2[z] == color.BLACK:
            Z.delete(z)
    return Z
