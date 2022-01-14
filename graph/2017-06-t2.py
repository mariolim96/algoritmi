# dato G e tre vertici a, b, c,si verifichi che se esiste un percorso infinito che passa esattamente
# prima una volta per a,poi b,e infine c
from datastructure import Graph, Node, color


def algo(G: Graph, a: Node, b: Node, c: Node):
    G.init()
    c.visited = color.black
    G.dfs(a)
    if G.color[b] == color.BLACK:
        G.init()
        a.visited = color.black
        G.dfs(b)
        if G.color[c] == color.BLACK:
            G.init()
            a.visited = b.visited = color.black
            return (G.aciclicGraph(c)) #la funzione deve anche verificare che nel ciclo non ci sia anche c
