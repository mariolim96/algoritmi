# min max  pred e succ hanno senso se esiste un ordinament
# array e una strutture contigue con accesso diretto
class array(object):
    def __init__(self, array=[]):
        self.array = array

    def ricerca(self, elemento):
        if elemento in self.array:
            return True

    def cancella(self, elemento):
        if elemento in self.array:
            self.array.remove(elemento)

    def aggiungi(self, elemento):
        self.array.append(elemento)

    def stampa(self):
        print(self.array)

    def min(self):
        return min(self.array)

    def max(self):
        return max(self.array)

    def predecessore(self, elemento):
        if elemento in self.array:
            return self.array[self.array.index(elemento)-1]

    def successore(self, elemento):
        if elemento in self.array:
            return self.array[self.array.index(elemento)+1]
