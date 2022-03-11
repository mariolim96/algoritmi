from enum import Enum
import sys
from typing import DefaultDict


class color(Enum):
    white = "white"
    grey = "grey"
    black = "black"


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


class Node(object):

    def __init__(self, name, adjacent=[],
                 visited=color.white, predecessor=None):
        self.name = name
        self.adjacenciesList = []
        self.visited = visited
        self.predecessor = predecessor
        self.start = None
        self.finish = None
        self.distance = sys.maxsize
        self.grade = 0

    def __repr__(self) -> str:
        # {[v.name for v in self.adjacenciesList]}
        return f'''{self.name}'''

    def append(self, vertex):
        self.adjacenciesList.append(vertex)

    def setColor(self, color):
        self.visited = color

    def init(self):
        self.visited = color.white
        self.predecessor = None
        self.start = None
        self.finish = None
        self.distance = sys.maxsize
        self.grade = 0


class Graph(object):
    time = 0
    cfc = DefaultDict(list)

    def __init__(self, nodeList: list = [], time: int = 0):
        self.nodeList = nodeList
        self.nodeCount = len(self.nodeList)

    def __repr__(self) -> str:
        return f'{[print(vertex,vertex.visited,":",vertex.adjacenciesList) for vertex in self.nodeList]}'

    def insert(self, node):
        self.nodeList.append(node)

    def findVertex(self, name):
        for n in self.nodeList:
            if n.name == name:
                return n

    def setEqualArray(self, A):
        A_prime = []
        for v in A:
            for u in self.nodeList:
                if v.name == u.name:
                    A_prime.append(u)
        return A_prime

    def insertNewNode(self, name: str, adjacent: list = []):
        node = Node(name, adjacent)
        self.nodeList.append(node)

    @staticmethod
    def edge(v: Node, u: Node):
        v.adjacenciesList.append(u)

    def init(self):
        for node in self.nodeList:
            node.init()

    def bfs_init(self):
        for node in self.nodeList:
            node.visited = color.white
            node.predecessor = None
            node.distance = sys.maxint

    def bfs(self, source: Node):
        self.bfs_init()
        queque = Queue()
        queque.enqueue(source)
        source.distance = 0
        source.visited = color.grey
        while(not queque.isEmpty()):
            node = queque.dequeue()
            for v in node.adjacenciesList:
                if v.visited == color.white:
                    v.visited = color.grey
                    v.predecessor = node.name
                    queque.enqueue(v)
                    v.distance = node.distance + 1
            node.visited = color.black

    def bfs_distance_between_2Nodes(self, source: Node, destination: Node):
        self.bfs_init()
        queque = Queue()
        queque.enqueue(source)
        source.distance = 0
        source.visited = color.grey
        while(not queque.isEmpty()):
            node = queque.dequeue()
            if node == destination:
                return node.distance
            for v in node.adjacenciesList:
                if v.visited == color.white:
                    v.visited = color.grey
                    v.predecessor = node
                    queque.enqueue(v)
                    v.distance = node.distance + 1
            node.visited = color.black

    def dfs_init(self):

        for node in self.nodeList:
            node.visited = color.white
            node.predecessor = None
            node.start = None
            node.finish = None
        self.time = 0
        for node in self.nodeList:
            if node.visited == color.white:
                node.visited = color.grey
                self.dfs(node)
                self.time += 1
                node.finish = self.time

    def dfs(self, source: Node):
        self.time += 1
        source.start = self.time
        source.visited = color.grey
        for node in source.adjacenciesList:
            if node.visited == color.white:
                node.predecessor = source.name
                self.dfs(node)
                self.time += 1
                node.finish = self.time
            node.visited = color.black

    def dfsColor(self, source: Node, colors: dict):
        self.time += 1
        source.start = self.time
        for node in source.adjacenciesList:
            if node.visited == color.white:
                node.predecessor = source.name
                self.dfs(node, colors)
                self.time += 1
                node.finish = self.time
            node.visited = color.black
            colors[node.name] = color.black

    def dfs_aciclicgraph(self, v):
        self.dfs_init(self)
        for v in self.nodeList:
            if v.visited == color.white:
                ret = self.aciclicgraph(self, v)
                if ret:
                    return True
        return False

    def aciclicGraph(self, source: Node):
        source.visited = color.grey
        for v in source.adjacenciesList:
            if v.visited == color.white:
                v.predecessor = source.name
                if self.aciclicgraph(self, v):
                    return True
            elif v.visited == color.grey:
                return True
        source.visited = color.black
        return False

    def enteringGrade(self):
        for v in self.nodeList:
            v.grade = 0
        for v in self.nodeList:
            for u in v.adjacenciesList:
                u.grade += 1

    def topologicalOrder(self):
        q = Queue()
        self.enteringGrade()
        for v in self.nodeList:
            if v.grade == 0:
                q.enqueue(v)
        while not q.isEmpty():
            v = q.dequeue()
            print(v.name)
            for u in v.adjacenciesList:
                u.grade -= 1
                if u.grade == 0:
                    q.enqueue(u)

    def dfstopologicalorder(self):
        pass

    # cfc algorithm

    def cfc_algo(self):
        L = Stack()
        self.dfs1(L)
        Gt = self.traspose()
        Gt.cfcDfs(L)

        return Gt.cfc

    def dfs1(self, L: Stack):
        for v in self.nodeList:
            if v.visited == color.white:
                v.visited = color.grey
                L = self.dfs1_visit(v, L)
        return L

    def dfs1_visit(self,  v: Node, L: Stack):
        v.visited = color.grey
        for w in v.adjacenciesList:
            if w.visited == color.white:
                L = self.dfs1_visit(w, L)
        v.visited = color.black
        L.push(v)
        return L

    # trasose of a graph

    def traspose(self):
        Gt = Graph()
        for v in self.nodeList:
            Gt.insertNewNode(v.name)
        for v in self.nodeList:
            for w in v.adjacenciesList:
                ww = Gt.findVertex(w.name)
                vv = Gt.findVertex(v.name)
                if ww is not None and vv is not None:
                    Gt.edge(ww, vv)

        return Gt

    def cfcDfs(self, L):
        cfc = 0
        self.modifyStack(L)
        while not L.isEmpty():
            v = L.pop()
            if(v.visited == color.white):
                self.cfcDfs_visit(v, cfc)
                cfc += 1

    def cfcDfs_visit(self, v, cfc):
        v.visited = color.grey
        self.cfc[cfc].append(int(v.name))
        for w in v.adjacenciesList:
            if w.visited == color.white:
                self.cfcDfs_visit(w, cfc)
        v.visited = color.black

    def modifyStack(self, L):
        L_prime = []
        for v in L.stack:
            for u in self.nodeList:
                if u.name == v.name:
                    L_prime.append(u)
        L.stack = L_prime

    def modifyArray(self, L):
        L_prime = []
        for v in L:
            for u in self.nodeList:
                if u.name == v.name:
                    L_prime.append(u)
        L = L_prime


if __name__ == '__main__':
    # node1 = Node("1")
    # node2 = Node("2")
    # node3 = Node("3")
    # node4 = Node("4")
    # node5 = Node("5")
    # node6 = Node("F")
    # node7 = Node("G")
    # node8 = Node("H")
    # node9 = Node("I")
    # node1.append(node2)
    # node1.append(node3)
    # node3.append(node1)
    # node2.append(node3)
    # node2.append(node4)
    # node4.append(node5)
    # graph = Graph([node1, node2, node3, node4, node5])
    # graph.topologicalOrder()
    # print(graph)
    # print(graph.cfc_algo())

    def algo(G: Graph, s: Node, u: Node, VAL: list):
        L = Stack()
        G.init()
        # vedo se ce un percorso che parte da s e arriva a u e se u e pari
        G.dfs(s)
        if VAL[u.name] % 2 == 1 or u.visited == color.white:
            return False
        G.init()
        L = G.dfs1(L)
        Gt = G.traspose()
        Gt.cfcDfs(L)
        # controlli sulle componenti fortemente connesse tramite tabella hash
        for key in Gt.cfc:
            if len(Gt.cfc[key]) > 1:
                for v in Gt.cfc[key]:
                    if VAL[str(v)] % 2 == 1:
                        return False
            else:
                if VAL[Gt.cfc[key][0]] % 2 == 0:
                    return False
        return True

    node1 = Node("1")
    node2 = Node("2")
    node3 = Node("3")
    node4 = Node("4")
    node5 = Node("5")
    node1.append(node2)
    node2.append(node3)
    node3.append(node4)
    node4.append(node5)
    node3.append(node1)

    G = Graph([node1, node2, node3, node4, node5])
    VAL = {"1": 3, "2": 1, "3": 0, "4": 0, "5": 0}
    print(algo(G, node1, node3, VAL))
