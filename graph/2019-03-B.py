
# Si scriva un algoritmo che, dati in ingresso unicamente G, B, u, v e k, calcoli in tempo lineare
# sulla dimensione di G, l’insieme dei vertici B’ ⊆ B contenente tutti e soli i vertici di A che
# soddisfano entrambe le seguenti condizioni:
# ● b è raggiungibile da v senza passare da u
# ● b raggiunge u con un percorso di lunghezza < k

from datastructure import Graph, Node, color, Stack

# giusta


def algo(G: Graph, B, u: Node, v: Node, k):
    G.init()
    u.visited = color.BLACK
    G.dfs(v)
    B_prime = set()
    B_prime1 = set()
    for b in B:
        if b.visited == color.BLACK:
            B_prime.add(b)
    G.init()
    Gt = G.transpose()
    Gt.bfs(u)
    for b in B:
        if b.distance < k:
            B_prime1.add(b)
    return B_prime.intersection(B_prime1)
