# dato un grafo G e B contenuto in V si vuole verificare se nell'insieme V\B
# possono essere partizionati due insiemi disgiunti V1 e V2 tale che :
# tale che V1 puo raggiungere qualche vertice di B e tutti i vertici di V2 sono raggiungibili da B
# ritorno i due insiemi V1 e V2

from datastructure import Graph, Node, color
# in pratica qualche v -> B,


def algoritmo(G: Graph, B):
    V1 = set()
    V2 = set()
    color1 = []
    color2 = []
    Bt = B
    w = Node("fake")
    for v in B:
        w.add_edge(v)
    G.init()
    G.dfsColor(w, color1)
    Gt = G.traspose()
    Gt.init()
    Gt.modifyArray(Bt)  # helper function
    Gt.dfsColor(w, color2)
    for v in G.nodeList:
        if v not in B:
            if color1[v.name] == color.black and color2[v.name] == color.black:
                return False
            elif color1[v.name] == color.black:
                V2.add(v)
            elif color2[v.name] == color.black:
                V1.add(v)
    print(V1, V2)
