# dati due grafi G1(V,E1) e G2(V,E2), e due vertici u e v
# verificare in tempo lineare che :
# 1) nel Grafo G1 ogni percorso massimale finito che parte da u non passa per v
# 2) nel Grafo G2 tutti i percorsi infiniti che partono da u devono passare per v
# un percorso si dice massimale se non puo essere ulteriormente esteso , quindi se e on infinito o finiscen in un vertice pozzo
from datastructure import Graph, Node, Stack, color


def dfs(self, s: Node, colors: dict):
    for node in s.adjacenciesList:
        if colors[node] == color.white:
            self.dfs(node, colors)
        colors[node] = color.black


def dfscycle(self, s: Node, colors: dict):
    for node in s.adjacenciesList:
        if colors[node] == color.white:
            if self.dfs(node, colors):
                return True
        if colors[node] == color.grey:
            return True
        colors[node] = color.black
    return False


def init(G, color):
    for node in G.nodeList:
        color[node] = color.white


def algo(G1: Graph, G2: Graph, u: Node, v: Node):
    color = {}
    init(G1, color)
    dfs(G1, u, color)
    if color[v] == color.black:  # questo e sbagliato
        return False
    init(G2, color)
    color[v] = color.black  # questo e giusto
    if dfscycle(G2, u, color):
        return False
    return True
