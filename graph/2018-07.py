
# sia dato G (liste adiacenza) e due array A e B sottoinsiemi dei vertici V
# si scriva un algoritmo che dato in ingresso A,B,G ritorni Z tale che:
# z E Z <=> esistono in G due percorsi da z tali che uno passa per i vertici di A senza passare per i vertici di B e viceversa

# sbagliato forse,
from datastructure import Graph, color


def algo(G: Graph, A, B):
    G.init()
    color1 = {}
    color2 = {}
    Gt = G.transpose()
    for v in B:
        color1[v] = color.black
    Gt.dfs_init()
    Gt.modifyArray(A)
    Gt.modifyArray(B)
    for v in A:
        if color[v] == color.white:
            Gt.dfsColor(v, color1)

        for v in A:
            v.visited = color.black
        G.dfs_init()
        for v in B:
            if v.visited == color.black:
                return True


#buono
# ALGO(G,A,B)
#     init(G);
#     for each v in B do
#         color1[v]=nero;
#     Gt=Trasposto(G);
#     for each v in A do
#       if(color1[v]=bianco)then
#         DFS_VisitMod(Gt,v,color1);
#     for each v in A do 
#       color2[v]=nero;
#     for each v in B do
#       if(color2[v]=bianco)then
#         DFS_VisitMod(Gt,v,color2);
#     for each v in V do 
#       if(color1[v]=nero && color2[v]=nero)then
#         Z=add(Z,v);
#     return Z;