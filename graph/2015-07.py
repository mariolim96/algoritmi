# dato un albero and un numero naturale k , trovare il nodo che ha il numero piu vicino a k
from datastructure import Stack, Node
# si puo applicare anche una  bfs e risolverlo in maniera lineare
# questa soluzione non e corretta


def find_diff_value(T, k: int):
    if T is not None:
        diff1 = abs(T.value - k)
        diff2 = find_diff_value(T.left, k)
        diff3 = find_diff_value(T.right, k)
        return min(diff1, diff2, diff3)
    return k  # se il nodo e' nullo ritorno e le massima distanza da k ,ossia k


def find_diff_value_iterative(T, k: int):
    cT = T
    stackT = Stack()
    lastT = None
    stackDiff1 = Stack()
    stackDiff2 = Stack()
    retval = k
    while cT is not None and not stackT.is_empty():
        if cT is not None:
            diff1 = abs(cT.value, k)
            stackDiff1.push(diff1)
            stackT.push(cT)
            cT = cT.left
        else:
            cT = stackT.Top()
            diff1 = stackDiff1.Top()
            if lastT is not None and cT.right is not None:  # sto venendo da sinistra e destro non e null
                diff2 = retval
                stackDiff2.push(diff2)
                cT = cT.right
            elif lastT is not None:  # sto venendo da destra
                diff2 = stackDiff2.Top()
                diff3 = retval
                lastT = cT
                cT = None
                stackT.pop()
                stackDiff1.pop()
                stackDiff2.pop()
                retval = min(diff1, diff2, diff3)
            else:  # sto venendo da una radice nulla e restituisco  k
                lastT = cT
                retval = k
                stackT.pop()
                stackDiff1.pop()
                stackDiff2.pop()
                cT = None

# 4)grafo


Sia dato un grafo orientato G, un array VAL[]
che associa ad ogni vertice v un numero naturale VAL[v]
e un vertice u del grafo.

Un percorso in G si dice massimale se non può essere ulteriormente
esteso, quindi se o è infinito o termina in un vertice pozzo.

Si definisca un algoritmo che, in tempo lineare sulla dimensione del
grafo G, verifichi se tutti i percorsi massimali che si dipartono
dal vertice u passano necessariamente da un vertice cui è associato
un numero pari


def Algoritmo(Graph G, Array VAL, Vertex u)
   for vert in V DO
       colore[vert] = BIANCO
        pred[vert] = NIL
    for vert in ADJ DO
        if ( not visita_controlla(G, vert, false) )
           return false
    return true


def visita_controlla( G:Graph,  u: Node , trovato_pari,VAL:dict)
    if VAL[u] % 2 == 0 :
       trovato_pari = True
    colore = GRIGIO
    if ADJ == NULL : # nessun arco uscente, nodo pozzo
        if (not trovato_pari ) :
            return False
    for vert in ADJ DO
        if colore[vert] == GRIGIO :
            if (not trovato_pari ) :
                return False
        if colore[vert] == BIANCO :
            res = visita_controlla(G, vert,trovato_pari)
    colore = NERO
    return res
