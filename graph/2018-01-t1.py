# dato G e tre vertici s,v,w si vuole verificare  se esiste un percorso in G che parte da s passa per v  ma non per u
from datastructure import Graph, Node, color


def algo(G: Graph, s: Node, v: Node, u: Node):
    u.visited = color.black

    G.dfs(s)
    if v.color == color.black:
        return True
    return False
