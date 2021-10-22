from datastructure import Graph, Queue, Node

#dovrebbe essere giusto
def grade(G):
    for v in G.nodeList:
        v.grade = 0
    for v in G.nodeList:
        for u in v.adjacenciesList:
            u.grade += 1


def examOrder(G: Graph):
    grade(G)
    q = Queue()
    propedeuticQueque = Queue()
    for v in G.nodeList:
        if v.grade == 0:
            q.enqueue(v)
    semester = 1
    while not q.isEmpty() or not propedeuticQueque.isEmpty():
        if not q.isEmpty():
            v = q.dequeue()
            print(v.name, semester)
            for u in v.adjacenciesList:
                u.grade -= 1
                if u.grade == 0:
                    propedeuticQueque.enqueue(u)
        else:
            semester = semester+1
            q = propedeuticQueque
            propedeuticQueque = Queue()


if __name__ == '__main__':
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")
    node8 = Node("H")
    node1.append(node2)
    node1.append(node3)
    node2.append(node3)
    node2.append(node4)
    node4.append(node5)
    node4.append(node6)
    node5.append(node6)
    node5.append(node7)
    node8.append(node7)
    graph = Graph([node1, node2, node3, node4, node5, node6, node7, node8])

    examOrder(graph)
