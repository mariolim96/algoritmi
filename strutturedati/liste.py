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

    def insert(self, data):
        if self.node is not None and self.node.data < data:
            tmp = self.node
            p = None
            while(tpm is not None and tmp.data < data):
                p = tmp
                tmp = tmp.next
            newNode = Node(data)
            p.next = newNode

    @staticmethod
    def insert_recursive(lista, data):
        if lista is None or lista.data >= data:
            newNode = Node(data)
            newNode.next = lista
            lista = newNode
        else:
            if lista.data < data:
                L1 = insert_recursive(lista.next, data)
                L.next = L1
        return lista

    def ricerca(self, elemento):  # O(n)
        current = self.node
        while current is not None and current.data != elemento:
            current = current.next
        return current

    def ricerca_ordinata(self, elemento):  # O(n)
        if node is None:
            return None
        if node.data == elemento:
            return node
        elif node.data < data:
            return Lista.ricerca_ordinata(node.next, elemento)
        return None

    @ staticmethod
    def ricerca_ricorsivo(node, elemento):  # O(n)
        if node is None:
            return False
        if node.data == elemento:
            return node
        return Lista.ricerca_ricorsivo(node.next, elemento)

    def cancella_ricorsivo(L, data):
        if L is None or L.data > data:
            return None
        if L.data == data:
            L1 = L.next
            free(L)
            return L1
        else:
            L = cancella(L.next, data)
        return L

    def cancella(L, data):
        while(L is not None and L.data < data):
            p = L
            L = L.next
        