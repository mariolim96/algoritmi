from datastructure import Node, Stack, color, Graph
# esercizio con cfc
from collections import deque


def verifyX(G: Graph, X: list):
    L = Stack()
    L = dfs1(G, L)
    Gt = G.traspose()
    cfcDfs(Gt, L)
    v = X[0]
    valcfc = G.cfc[v.name]
    print(Gt.cfc)
    for v in X[1:]:
        if Gt.cfc[v.name] != valcfc:
            return False
    return True


def dfs1(G: Graph, L: Stack):
    for v in G.nodeList:
        if v.visited == color.white:
            v.visited = color.grey
            L = dfs1_visit(G, v, L)
    return L


def dfs1_visit(G: Graph, v: Node, L):
    v.visited = color.grey
    for w in v.adjacenciesList:
        if w.visited == color.white:
            L = dfs1_visit(G, w, L)
    v.visited = color.black
    L.push(v)
    return L

# trasose of a graph


def traspose(G):
    Gt = Graph()
    for v in G.nodeList:
        Gt.insertNewNode(v.name)
    for v in G.nodeList:
        for w in v.adjacenciesList:
            # ww = Gt.findVertex(w.name)
            # vv = Gt.findVertex(v.name)
            if w is not None and v is not None:
                Gt.edge(w, v)
    return Gt


def cfcDfs(G, L):
    for node in G.nodeList:
        node.visited = color.white
        node.predecessor = None
        node.start = None
        node.finish = None
    cfc = 0
    while not L.isEmpty():
        v = G.findVertex(L.pop().name)
        if(v.visited == color.white):
            cfcDfs_visit(G, v, cfc)
            cfc += 1


def cfcDfs_visit(G, v, cfc):
    v.visited = color.grey
    G.cfc[v.name].append(cfc)
    for w in v.adjacenciesList:
        if w.visited == color.white:
            cfcDfs_visit(G, w, cfc)
    v.visited = color.black


if __name__ == '__main__':
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")

    node1.append(node2)
    node1.append(node3)
    node2.append(node3)
    node2.append(node4)
    node4.append(node5)
    graph = Graph([node1, node2, node3, node4, node5, node6])
    print(verifyX(graph, [node1, node2, node4, node5, node6]))
    # graph.dfs_init()
