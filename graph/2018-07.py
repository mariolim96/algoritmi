# sia dato G (liste adiacenza) e due array A e B sottoinsiemi dei vertici V
# si scriva un algoritmo che dato in ingresso A,B,G ritorni Z tale che:
# z E Z <=> esistono in Gdue percorsi da z tali che uno passa per i vertici di A senza passare per i vertici di B e viceversa
from datastructure import Graph, color


def algo(G: Graph, A, B):
    G.init()
    for v in B:
        v.visited = color.black
    G.dfs_init()
    find = False
    for v in A:
        if v.visited == color.black:
            find = True
            break
    if find:
        for v in A:
            v.visited = color.black
        G.dfs_init()
        for v in B:
            if v.visited == color.black:
                return True
