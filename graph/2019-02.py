# si scriva un algoritmpo che dato un grafo e un valore intero k e un vertice s E V e un insieme A C V
# in tempo lineare
# ogni percorso che parte dal vertice s e raggiunge un qualche vertice A ha lunghezza maggiore di k

# idea:
# 1. inizializzo i nodi G in bianco e le distanze a infinito
# 2. faccio partire una bfs dal nodo s
# 3. se la bfs raggiunge un nodo A, allora la distanza del nodo A dal nodo s è minore di k restituisco False
# 4. altrimenti restituisco True

#dovrebbe essere giusto
from datastructure import Graph, Node


def algo(G: Graph, s: Node, A: list, k: int):
    G.bfs_init()
    G.bfs(s)
    for v in A:
        if v.distance < k:
            return False
    return True
