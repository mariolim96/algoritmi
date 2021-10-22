
# schema astratto simulatore per algoritme ricorsivi
#     1)o inizia la simulazione di una chimata ricorsiva
#     2)riprendere simulazione di una chiamata sospesa
#     while Inizio||ripresa:
#         if inizio:
#             simula nuova chiamata
#         else:\
#             #ogni volta che un padre genera una chimata figlia
#             #l'algoritmo salva delle variabili nello stack
#             3)ripristino contesto di esecuzione:"riprendere valori
#               dall stack"
#             4)capire da dove riprende l'esecuzione
#             5)ripulire gli stack,e forzeremo la condizione "inizio" ad essere
#               falsa e assegnazione di eventuali valori di ritorno
#             #se ogni chiamata puo fare piu chiamate ricorsive allora
#               dobbiamo capire da quale delle chiamate stiamo ritornando

# aspetti da considerare:
# 1)come il padre comunica con il padre
# 2) come il figlio comunica con il padre
# attraverso delle variabili condivise
# il simulatore simulera le copie private delle variabili
# delle varie chiamate tramite uno o piu stack
from datastructure import Stack

def factorial(n):
    if n == 0:
        r = 1
    else:
        x = factorial(n-1)
        r = n * x
    return r


def iterativeFactorial(n):
    stack = Stack()
    cn = n
    ret = 0
    while cn >= 0 or not stack.isEmpty():
        if cn >= 0:
            if cn == 0:
                r = 1
                ret = r
                cn = cn-1
            else:
                x = stack.push(cn)
                cn = cn-1
        else:
            cn = stack.top()
            x = ret  # il valore che la funzione ricorsiva ritorna
            r = x*cn
            stack.pop()
            ret = r
            cn = -1
    return ret


if __name__ == "__main__":
    # stack = Stack()
    # print(stack.isEmpty())
    print(iterativeFactorial(5))
    print(factorial(5))
