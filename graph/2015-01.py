# two vertices of the graph G , are separated by a set X Contained in V.
# if every path from v to w pass Through X, and viceversa, then every path from w to v pass Through X.
# find  an algorithm  that verify this condition.

# quindi devo trovare an algorithm che verifica se esiste un percorso tra u e v per X
from datastructure import Graph, Node, color

#giusto 
def notPassTroughX(G: Graph, X: list, u: Node, v: Node):
    # o coloriamo di nero i nodi che non devono passare per X o li eliminiamo da G
    for x in X:
        x.set_color(color.black)
    # ritorna true se esiste un percorso tra u e v e viceversa(posso anche controllare l'array delle distanze o colori)
    return not G.bfs(u, v) and G.bfs(u, v)
