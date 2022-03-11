# given a not oriented graph G=(V,E) represented with adjacent list,
# find an algorithm that verify if is possible to partition the set of
# nodes into two sets V1 C V and V2 C V with this condition:
#  V1 U V2 = V
#  V1 intersected V2= void set
# v belong to V1  <=>  for each edge (v,w) in E , w belongs to V2
from datastructure import Graph, Node, Queue, color
# giusto


def bipartite(G: Graph):
    if G.nodeCount % 2 == 0:
        return bfs(G, G.nodeList[0])
    return None


def bfs(G: Graph, s: Node):
    V1 = set()
    V2 = set()
    Q = Queue()
    Q.enqueue(s)
    V1.add(s)
    s.visited = color.grey
    while not Q.isEmpty():
        v = Q.dequeue()
        for w in v.adjacenciesList:
            if w.visited == color.white:
                if v.visited == color.black:
                    w.visited = color.grey
                    V1.add(w)
                else:
                    V2.add(w)
                    w.visited = color.black
                Q.enqueue(w)
            elif w.visited == v.visited:
                return None
    return V1, V2


if __name__ == '__main__':
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node1.append(node2)
    node2.append(node3)
    node3.append(node4)
    node4.append(node1)
    G = Graph(nodeList=[node1, node2, node3, node4])
    print(bipartite(G))
