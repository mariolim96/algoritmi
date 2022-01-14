# la lista e una struttura ad accesso sequenziale e non contiguo contenente una sequenza di eleementi
# Oppure puo essere definita come:
# L e una lista se:
# 1)L=O/
# 2)L=l1->none
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class Lista(object):
    def __init__(self, node: Node = None):
        self.node = node

    def ricerca(self, elemento):  # O(n)
        current = self.node
        while current is not None and current.data != elemento:
            current = current.next
        return current

    @staticmethod
    def ricerca_ricorsivo(node, elemento):  # O(n)
        if node is None:
            return False
        if node.data == elemento:
            return node
        return Lista.ricerca_ricorsivo(node.next, elemento)

    def cancella(self, elemento):

    def aggiungi(self, elemento):

    def stampa(self):

    def min(self):

    def max(self):

    def predecessore(self, elemento):

    def successore(self, elemento):
