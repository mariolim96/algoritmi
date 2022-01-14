# dato G e due insiemi A e B Contenuti in V  e un intero k
# si vuole verificare se esiste un percorso  che parte da un vertice di A
# e arriva a un vertice di B ha lunghezza >= k
from datastructure import Graph, Node, color


def algo(G: Graph, A: set, B: set, k: int) -> bool:
    w = Node("fakevertex")
    for v in A:
        w.append(v)
    G.init()
    G.bfs(w)
    for v in B:
        if v.distance >= k:
            return True
    return False
