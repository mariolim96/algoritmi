from datastructure import Node, BinarySearchTree, Stack, Queue
#funziona
# deleting all noded from a tree between two values


def leftMost(root):
    if (root is None):
        return None
    while (root.left):
        root = root.left
    return root


def deleteNode(root):
    if (root.left is None):
        child = root.right
        root = None
        return child
    elif (root.right is None):
        child = root.left
        root = None
        return child
    # Node with two children
    next = leftMost(root.right)
    root.data = next.data
    root.right = deleteNode(next)
    return root


def algo(T: Node, k1: int, k2: int):

    if T is not None:
        T.left = algo(T.left, k1, k2)
        T.right = algo(T.right, k1, k2)
        if T.data > k1 and T.data < k2:
            T = deleteNode(T)
        return T

# versione iterativa
# Dato un ABR T scrivere un algoritmo iterativo efficiente che dato T e un intero non negativo k
# restituisca la chiave cha ha valore numericamente più vicino a k ma diversa da k stesso

# presupponendo che l'albero possa contenere anche valori negativi


def nearValueK(T, k):
    q = Stack()
    q.enqueue(T)
    nearValue = k
    while(not q.isEmpty()):
        node = q.pop()
        if nearValue-node.data != 0:
            nearValue = min(nearValue, abs(node.data-k))
        if nearValue == 1:
            return nearValue
        if node.left is not None:
            q.push(node.left)
        if node.right is not None:
            q.push(node.right)

# eliminare valori between k1 and k2


def deleteValueBetween(T: BinarySearchTree, k1: int, k2: int):
    q = Stack()
    q.enqueue(T.root)
    while(not q.isEmpty()):
        node = q.pop()
        if(node and node.left.data >= k1):
            q.push(node.left)
        if(node and node.right.data <= k2):
            q.push(node.left)
        if(node.data >= k1 and node.data <= k2):
            node = deleteNode(node)


# given a graph G and two vertices u and v i,


if __name__ == '__main__':

    tree = BinarySearchTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(2)
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)
    tree.printlevelorder(tree.root, )
    algo(tree.root, 3, 7)
    tree.printlevelorder(tree.root, )
