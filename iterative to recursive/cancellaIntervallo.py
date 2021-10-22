from datastructure import Stack, BinarySearchTree, Node, deleteNode


def cancellaI(T: Node, a, b):
    if T is not None:
        if T.data < a:
            T.right = cancellaI(T.right, a, b)
        elif T.data > b:
            T.left = cancellaI(T.left, a, b)
        else:
            T.left = cancellaI(T.left, a, b)
            T.right = cancellaI(T.right, a, b)
            T = deleteNode(T)

    return T


def cancellaintervallo(T, a, b):
    stackT = Stack()
    ret = None
    cT = T
    last = None
    while cT is not None or not stackT.isEmpty():
        if cT is not None:
            if cT.data < a:
                stackT.push(cT)
                cT = cT.right
            elif cT.data > b:  # queste due sono uguali e si puo sparagnare
                stackT.push(cT)
                cT = cT.left
            else:
                stackT.push(cT)
                cT = cT.left
        else:
            cT = stackT.top()
            if cT.data < a:
                cT.right = ret
                ret = cT

                stackT.pop()
                last = cT
                cT = None

            elif cT.data > b:
                cT.left = ret
                ret = cT

                stackT.pop()
                last = cT
                cT = None
            else:
                if last is not cT.right and cT.right is not None:
                    cT.left = ret
                    cT = cT.right
                elif cT.right is None:
                    cT.left = ret
                    cT.right = None
                    cT = deleteNode(cT)
                    ret = cT
                    last = cT
                    stackT.pop()
                    cT = None
                else:
                    cT.right = ret
                    cT = deleteNode(cT)
                    ret = cT
                    # risalita
                    last = cT
                    stackT.pop()
                    cT = None

    return ret


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(6)
    # tree.insert(7)
    # tree.insert(1)
    # tree.insert(4)
    # tree.insert(6)
    # tree.insert(8)

    tree.printlevelorder(tree.root, tree.countNodes(tree.root))
    print("albero dopp \n")
    T = cancellaintervallo(tree.root, 3, 6)
    tree.printlevelorder(T, tree.countNodes(tree.root))
