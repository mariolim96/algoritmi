# dato G e un array A C V di G e un vertice v,
# calcoli Z C V che rispetta la condizione :
# z E Z <==> esiste un percorso tra z e v che passa per qualche A,
# ossia z->A->v
from datastructure import Graph, Node, color

# fatta bene
# faccio partire una dfs che parte da v e trovo tutti i nodi di a che raggiunge
# a questo punto creo un vertice W e aggiungo i nodi black di A
# faccio partire una seconda dfs  che parte da W e trova tutti i nodi z


def algo(G: Graph, A: list, v: Node, z: Node):
    color1 = {}
    color2 = {}
    Gt = G.transpose()
    At = Gt.modifyArray(A)
    w = Node("fake")
    Gt.init()
    Gt.dfsColor(v, color1)
    for i in At:
        # qua trovo tutti i nodi aEA che raggiungono v
        if i.visited == color.black:
            w.adjacenciesList.append(i)
    G.init()
    G.dfsColor(z, color2)  # verifico se esiste un nodo di a che raggiunge z
    Z = set()
    for k in A:
        if color2[k.name] == color.black:
            Z.add(k)
    return Z


if __name__ == "__main__":
    node1 = Node("1")
    node2 = Node("2")
    node3 = Node("3")
    node4 = Node("4")
    node5 = Node("5")
    node6 = Node("6")
    node7 = Node("7")
    node8 = Node("8")
    node1.append(node2)
    node1.append(node3)
    node2.append(node4)
    node2.append(node5)
    node3.append(node6)
    node5.append(node3)
    node5.append(node7)
    node6.append(node8)
    A = [node3, node4, node5, node6]
    G = Graph()
    G.addNode("a")
