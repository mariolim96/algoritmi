from datastructure import Graph, Node, color

# trova tutti  i percorsi da u a v che passano da z che hanno lunghezza maggiore di k


def printAllPaths(start: Node, end: Node, path, path_list):
    path.append(start.name)
    start.visited == color.black
    if start == end:
        path_list.append(path[:])
    else:
        for v in start.adjacenciesList:
            if v.visited == color.white:
                path_list = printAllPaths(v, end, path, path_list)
    start.visited == color.white
    path.pop()
    return path_list


def printAllPathsWithLength(u: Node, v: Node, k: Node, val):
    list1 = []
    list2 = []
    list2 = printAllPaths(u, k, [], [])
    list1 = printAllPaths(k, v, [], [])

    print(list1)
    print(list2)
    l1 = len(min(list1, key=lambda x: len(x)))
    l2 = len(min(list2, key=lambda x: len(x)))

    if(l1+l2 > val):
        print("yes")
    else:
        print("no")


if __name__ == '__main__':
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")
    node5 = Node("E")
    node6 = Node("F")
    node7 = Node("G")
    node8 = Node("H")
    node9 = Node("I")
    node1.append(node2)
    node1.append(node3)
    node2.append(node3)
    node2.append(node4)
    node3.append(node4)
    node4.append(node5)
    printAllPathsWithLength(node1, node5, node4, 10)
