class Queue:

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        return self.queue[0]

    def sizeQueue(self):
        return len(self.queue)


class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def top(self):
        return self.stack[-1]

    def sizeStack(self):
        return len(self.stack)


class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


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

    # Node with two children: get
    # inorder successor in the
    # right subtree
    next = leftMost(root.right)

    # Copy the inorder successor's
    # content to this node
    root.data = next.data

    # Delete the inorder successor
    root.right = deleteNode(root.right)

    return root


def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        # Use the larger one
        if lheight > rheight:
            return lheight+1
        else:
            return rheight+1


# Wrapper over print2DUtil()


class BinarySearchTree(object):

    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data, self.root)

    # O(logN)   if the tree is balanced !!!!!!!!!!!!!  --> it can reduced to O(N) --> AVL RBT are needed !!!!!
    def insertNode(self, data, node):

        if data < node.data:
            if node.left:
                self.insertNode(data, node.left)
            else:
                node.left = Node(data)
        else:
            if node.right:
                self.insertNode(data, node.right)
            else:
                node.right = Node(data)
    # O(logN)

    def removeNode(self, data, node):

        if not node:
            return node

        if data < node.data:
            node.left = self.removeNode(data, node.left)
        elif data > node.data:
            node.right = self.removeNode(data, node.right)
        else:

            if not node.left and not node.right:
                print("Removing a leaf node...")
                del node
                return None

            if not node.left:  # node !!!
                print("Removing a node with single right child...")
                tempNode = node.right
                del node
                return tempNode
            elif not node.right:   # node instead of self
                print("Removing a node with single left child...")
                tempNode = node.left
                del node
                return tempNode

            print("Removing node with two children....")
            # self instead of elf  + get predecessor
            tempNode = self.getPredecessor(node.left)
            node.data = tempNode.data
            node.left = self.removeNode(tempNode.data, node.left)

        return node   # !!!!!!!!!!!!

    def getPredecessor(self, node):

        if node.right:
            return self.getPredeccor(node.right)

        return node

    def remove(self, data):
        if self.root:
            self.root = self.removeNode(data, self.root)

        # O(logN)
    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)

    def getMin(self, node):

        if node.left:
            return self.getMin(node.left)

        return node.data

        # O(logN)
    def getMaxValue(self):
        if self.root:
            return self.getMax(self.root)

    def getMax(self, node):

        if node.right:
            return self.getMax(node.right)

        return node.data

    def traverse(self):
        if self.root:
            self.traverseInOrder(self.root)

            # O(N)
    def traverseInOrder(self, node):
        count = 1
        if node.left:
            count += self.traverseInOrder(node.left)

        print("%s " % node.data)

        if node.right:
            count += self.traverseInOrder(node.right)
        return count

    @staticmethod
    def countNodes(node):
        count = 1
        if node.left:
            count += BinarySearchTree.countNodes(node.left)
        if node.right:
            count += BinarySearchTree.countNodes(node.right)
        return count

    @staticmethod
    def printlevelorder(root):
        h = BinarySearchTree.countNodes(root)
        for i in range(1, h + 1):
            BinarySearchTree.printGivenLevel(root, i, h)
            print("\n")

    @staticmethod
    def printGivenLevel(root, level, nNodes):
        m = abs(nNodes//2+1)
        if root is None:
            print(m*"  "+" ", end='')
            return root

        if level == 1:
            tab = m*"  "+str(root.data)
            print(tab, end='')
        elif level > 1:
            BinarySearchTree.printGivenLevel(root.left, level - 1, m-1)
            BinarySearchTree.printGivenLevel(root.right, level - 1, m+1)
