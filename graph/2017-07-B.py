# dato G e tre vertici a,b e c verificare che:
# 1)a non raggiunge b,2)b non raggiunge c,3)c non raggiunge a
from datastructure import Graph, Node, Stack, color


def algo(G: Graph, a: Node, b: Node, c: Node):
    if G.is_adjacent(a, b) or G.is_adjacent(b, c) or G.is_adjacent(c, a):
        return False
    else:

        G.init()
        G.dfs(a)
        if b.visited == color.black:
            return True
        G.init()
        G.dfs(b)
        if a.visited == color.black:
            return True
        G.init()
        G.dfs(c)
        if a.visited == color.black:
            return True
        return Falsel
