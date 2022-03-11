# dato un grafo G e un array di colori C,verificare
# se esiste un cammino da u a v che rispetta le seguenti condizioni:
# 1. c[u] =! c[v]
# 2. esite un cammino da u a v
# 3. esiste un cammino da v a u

# u e v devono essere mutualmente raggiungibili quindi esiste una componente connessa fra di loro
# quindi basterebbe vedere se sono nella stessa cfc e poi vedere se i colori di u e v sono diversi

from datastructure import Stack, Graph, Node
from datastructure import Graph, Node, Stack, color
Gt = GrafoTrasposto(g)

# For each v in V {
#     if(c[v] == b){
#         dfsvisit(v,C[v])
#     }
# }
# ......


# dfsvisit(v,col){
#     c[v] = g
#     for each y in ADj[v]{
#         if c[y] == b{
#             if C[y] != col{
#                 if(dfsvisit2(Gt, v, y))   //se trova il percorso da v a y in GT return true
#                 return true
#             }
#             dfsvisti(y)
#             }
#     }
# }

def dfs(G, source: Node, arrive: Node, colors):
    if source == arrive:
        return True
    for node in source.adjacenciesList:
        if node.visited == color.white:
            node.predecessor = source.name
            L = G.dfs(node, colors)
            colors[node.name] = color.black
    return False


def algo(G: Graph, C: dict, u: Node, v: Node):
    L = Stack()
    L = G.dfs1(L)
    Gt = G.traspose()
    Gt.cfcDfs(L)

    # controllo dizionaro e ritorno
    return Gt.cfc[u.name][0] == Gt.cfc[v.name][0]
