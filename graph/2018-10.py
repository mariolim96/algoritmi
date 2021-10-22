#dato un grafo G e due insiemi B e C, restituisce una lista L di vertici tale che:
# v appartiene a B e deve raggiungere s
# esiste unpercorso da s a v che non passa per nessun vertice di C
# dobbiamo creare L

#giusto
def algo(G, B, C, s):
    L = col1 = col2 = []
    G.init()
    Gt = G.traspose()
    Gt.dfs(s, col1)
    for v in C:
        v.visited = color.black
    G.dfs(s,col2)

    for v in B:
        if col1[v] == color.black and col2[v] == color.black:
            L.append(v)
    return L
