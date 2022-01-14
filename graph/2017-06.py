# dato G e 4 vertici a,b,c,d
# verifica se ogni percorso infinito che parte da a e passa per b
# continua la traccia

# esercizio praticamente uguale a quello del 2017-07
from datastructure import Graph, Node, color


def algo(G: Graph, a, b, c, d):

    G.init()
    c.visited = d.visited = color.black
    G.dfs(a)
    if b.visited == color.black:
        G.init()
        c.visited = d.visited = color.black
        return G.aciclicGraph(b)

# ALGO(G,a,b,c,d)
#   init(G);
#   color[c]=color[d]=nero;
#   DFS_Visit(G,a);
#   ret=true;
#   if(color[b]=nero)then
#     init(G);
#     ret=DFS_VisitMod(G,b);
#   return ret;

# DFS_Visit(G,a)
#   color[a]=grigio;
#   for each v in V do
#     if(color[v]=bianco)then
#       DFS_Visit(G,v);
#   color[a]=nero;

# DFS_VisitMod(G,b)
#   color[b]=grigio;
#   for each v in adj(b) do
#     if(color[v]=bianco)then
#       ret=DFS_VisitMod(G,v);
#       if(ret=false)then
#         return false;
#     else if(color[v]=grigio)then
#       return false;
#   color[b]=nero;
#   return true;
