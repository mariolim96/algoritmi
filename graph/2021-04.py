# Dato un grafo G e un sottoinsieme di vertici A, scrivere un algoritmo efficiente che stampi,
# se esistono, due insiemi B,C sottoinsiemi di V tali che:
# 1. B intersecato C è un sottoinsieme di A
# 2. Ogni vertice di B ha un percorso che raggiunge almeno un vertice di A
# 3. Ogni vertice di C è raggiungibile da almeno un vertice di A

#dovrebbe essere giusto
from datastructure import Graph, color


def algo(G, A):
    B = set()
    C = set()

    Gt = G.traspose()
    Gt.init()
    for v in A:
        if (v.visited == color.white):
            Gt.dfs_visit(v)
    for v in Gt.nodeList:
        if v.visited == color.black:
            B.add(v)
    G.init()
    for v in A:
        if (v.visited == color.white):
            G.dfs_visit(v)
    for v in Gt.nodeList:
        if v.visited == color.black:
            C.add(v)
    for v in Gt.nodeList:
        if B.has(v) and C.has(v) and v not in A:
            return False

    return True
