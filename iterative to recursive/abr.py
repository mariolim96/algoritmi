# return the number of odd keys contained into abr
from datastructure import Stack, BinarySearchTree


def countodd(root: BinarySearchTree):
    r = 0
    if root is not None:
        r += countodd(root.left)
        if root.data % 2 == 1:
            r = r + 1
        r += countodd(root.right)
    return r


def countOddIterative(tree: BinarySearchTree):
    cT = tree.root
    ret = 0
    stackR = Stack()
    stackABR = Stack()
    last = None
    while not stackR.isEmpty() or cT is not None:
        if cT is not None:
            r = 0
            stackABR.push(cT)
            cT = cT.left
            ret = r
        else:
            cT = stackABR.top()
            if last != cT.right and cT.right is not None:  # non torno da destra e destra non e null
                r = ret
                if cT.data % 2 == 1:
                    r = r+1
                stackABR.push(cT)
                cT = cT.right
            else:
                if cT.right is None:  # torno da sinistra ma destro e null
                    if cT.data % 2 == 1:
                        r = r+1
                    r = r+0  # chiamata ricorsiva con caso base che e zero
                    stackABR.pop()
                    last = cT
                    cT = None
                else:  # torno da destra
                    r = stackABR.top()
                    r += ret
                    ret = r
                    stackABR.pop()
                    stackR.pop
                    last = cT
                    ct = None

    return r


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(2)
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)

    tree.printlevelorder(tree.root, tree.countNodes(tree.root))
