from datastructure import Stack, BinarySearchTree, Node


def FIND(T: Node, K):
    elem = None
    if T is not None:
        if T.data == K:
            elem = T
        else:
            elem = FIND(T.left)
            if elem is None:
                elem = FIND(T.right)
    return elem


def iterative_find(T, K):
    cT = T
    ret = None
    stackT = Stack()
    last = None
    while cT is not None or not stackT.isEmpty():
        if cT is not None:
            elem = None
            if cT.data == K:
                elem = cT
                # forzare risalita
                last = cT
                ret = elem
                cT = None
            else:
                stackT.push(cT)
                cT = cT.left
        else:
            cT = stackT.top()
            if last is not cT.right and cT.right is not None:
                elem = ret
                if elem is None:
                    last = cT
                    cT = cT.right
                else:
                    last = cT
                    stackT.pop()
                    ret = elem
                    cT = None
            else:
                elem = ret
                last = cT
                stackT.pop()
                ret = elem
                cT = None
    return ret


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(8)
    tree.insert(6)
    tree.insert(1)
    tree.insert(4)
    tree.insert(9)
    tree.insert(8)
    stack = Stack()
    print(stack.isEmpty())

    tree.printlevelorder(tree.root, tree.countNodes(tree.root))
    print(iterative_find(tree.root, 62))


# teoria prof
# e fondamentale che se una variabile viene stabilita prima di una chiamata ricorsiva
# e letta dopo la chiamata ricorsiva e necessario quindi salvare il valore della variabile
# il valore di elem ha prima di ogni chiamata ricorsiva non verra usata dopo la chiamata ricorsiva


# iterativo
# FIND(T, K)
#     stack = None
#     CT = T
#     elem = None
#     last = None
#     ret = None
#     while(CT is not None | | stack is not None)do
#          if CT is not None:
#             elem = None
#             if CT . key = K:
#                 elem = CT
#                 last = CT
#                 CT = None
#                 ret = elem
#             else
#                 stack.push(CT)
#                 CT = CT . left
#         else
#             CT =stack.top()
#             // ora dobbiamo chiederci dove ci siamo sospesi ? nella chiamata a destra o a sinistra ?
#             if (last not CT.right && CT.rightis notNone):// qui sono tornato da qualcosa diverso dal destro , ci siamo sospesi alla chiamata ricorsiva di sx
#                 elem=ret
#                 if elem = None :
#                     CT=CT.dx
#                 else
#                     stack.pop()
#                     last = CT
#                     CT = None
#                     ret = elem
#             else
#                 stack.pop()
#                 last = CT
#                 CT = None
#                 ret = elem
