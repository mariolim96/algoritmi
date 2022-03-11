

# nessuna soluzione al momento
from datastructure import Graph, Node, Stack, color

# In which case, some nodes z can be in the same connected component as u and v, yet not part
#  of any path from u to v. That is, there is a path from u to z, and a path from z to v, and
# concatenating those two paths is of course a walk from u to v, but it is not a path
# https://link.springer.com/chapter/10.1007/978-3-540-24749-4_31
# controllo

# buono


def ALGO(G: Graph, A, u, v):
    G.init()
    c1 = c2 = {}
    Z = set()
    DFS_MOD(G, u, c1)
    # trovo tutti i vertici raggiungibili da u
    G_prime = G.traspose()
    DFS_MOD(G_prime, v, c2)
    # trovo tutti i vertici che raggiungono v nel grafo di partenza
    Z = []
    for v in A:
        # allora questo vertice non si trova su un percorso da u a v
    IF(c1[v]=color.white or c2[v]=color.white):
        Z = add(Z, v)



def algo1(G: Graph, u: Node, v: Node):

    # now u and v are in the same strongly connected component
    L = Stack()
    L = dfs(G, L)
    Gt = G.traspose()
    scc = []
    scc = sccdfs(Gt, L)
    # now i finded all z in the same strongly connected component as u and v
    sccu = scc[u]
    z = []
    for v in scc:
        if v != sccu:
            z.append(v)
    return z

