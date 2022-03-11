# dato G e A[] contenente vertice di G e due vertici u e v,
# scrivere un grafo che verifichi in tempo lineare l'insieme di vertici A'C A contenente tutti i vertici di G che soddisfano questa condizione
# a belong to A' se e solo se  esiste un percorso TT di G che parte da u e arriva a v e passa per a
# TT :u->a->v

# soluzione:
# 1) trovare tutti i percorsi di G che partono da u e arrivano ai vertici di A
# 2) trasposta di G
# 3) trovare tutti i percorsi di G' che partono da v e arrivano ai vertici di A
# 4) verificare che col1 e col2  dei vertici di a siono uguali a aggiungerli ad A'
from datastructure import Graph, Node

# giusto


def algo(G: Graph, A: list, u: Node, v: Node):
    col1 = {}
    col2 = {}
    G.init()
    G.dfs(u, col1)
    Gt = G.traspose()
    A_prime = []
    Gt.init()
    for vertex in Gt.nodeList:
        if v.name == vertex.name:
            Gt.dfs(vertex, col2)
            break
    for v in A:
        if str(v) in col1 and str(v) in col2 and col1[str(v)] == col2[str(v)]:
            A_prime.append(v)
    return A_prime


if __name__ == "__main__":
    node1 = Node("1")
    node2 = Node("2")
    node3 = Node("3")
    node4 = Node("4")
    node5 = Node("5")
    node6 = Node("6")
    node1.append(node2)
    node1.append(node3)
    node2.append(node4)
    node2.append(node5)
    node3.append(node6)
    A = [node2, node3, node4]
    G = Graph([node1, node2, node3, node4, node5, node6])
    print(algo(G, A, node1, node6))
