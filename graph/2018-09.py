from datastructure import Graph, Node, color, Stack
# dato G ,Val che associa un valore k ad ogni vertice di V e u , s vertici
# TT che parte da s e contiene infinite occorrenze di u
# TT contiene infinite occorrenze di vertici che abbiano valore pari in val
# TT finite occorrenze di vertici che abbiano valore dispari

   def algo(G: Graph, s: Node, u: Node, VAL: list):
        L = Stack()
        G.init()
        # vedo se ce un percorso che parte da s e arriva a u e se u e pari
        G.dfs(s)
        if VAL[u.name] % 2 == 1 or u.visited == color.white:
            return False
        G.init()
        L = G.dfs1(L)
        Gt = G.traspose()
        Gt.cfcDfs(L)
        # controlli sulle componenti fortemente connesse
        for key in Gt.cfc:
            if len(Gt.cfc[key]) > 1:
                for v in Gt.cfc[key]:
                    if VAL[str(v)] % 2 == 1:
                        return False
            else:
                if VAL[Gt.cfc[key][0]] % 2 == 0:
                    return False
        return True

    node1 = Node("1")
    node2 = Node("2")
    node3 = Node("3")
    node4 = Node("4")
    node5 = Node("5")
    node1.append(node2)
    node2.append(node3)
    node3.append(node4)
    node4.append(node5)
    node3.append(node1)

    G = Graph([node1, node2, node3, node4, node5])
    VAL = {"1": 3, "2": 1, "3": 0, "4": 0, "5": 0}
    print(algo(G, node1, node3, VAL))
