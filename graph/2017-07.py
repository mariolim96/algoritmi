# dato in grafo G e tre vertici a,b,c , si verifica che ogni percorso
# infinito che parte da a e passa per b passa necessariamente anche dal vertice c.
# il vertice c compare prima di b
from datastructure import Graph, Node, color

# esiste un percorso infinito da a passando per b e non dal vertice c?


def algo(G: Graph, a, b, c):

    G.init()
    c.visited = color.black
    G.dfs(a)
    if b.visited == color.black:
        G.init()
        c.visited = color.black
        return G.aciclicGraph(b)
