from datastructure import color, Queue
# Given a graph G, a vertex u, and an array VAL[] that associates every vertex v with a natural number
# (For each vertex v of V, VAL[v]=n, where n is a natural number).

# A simple path in G is maximal if it can't be expanded anymore,
# maintaining the property to be simple.

# Define an algorithm that verifies that all simple maximal paths,
# that depart from vertex u necessarily pass 2 vertices associated with
# numbers of different parity.


# per ogni nodo terminale dobbiamo chiederci se puo essere raggiunto
# da un nodo solo parita' o solo disparita


class Node(object):

    def __init__(self, name, adjacency=[],
                 visited=False, predecessor=None):
        self.name = name
        self.adjacency = adjacency
        self.visited = visited
        self.predecessor = predecessor

    def __repr__(self) -> str:
        return f'''{self.name}'''

    def append(self, vertex):
        self.adjacency.append(vertex)


def dfs(start: Node, VAL: dict):
    start.visited == color.grey
    parity = VAL[start.name] % 2
    for v in start.adjacenciesList:
        if v.visited == color.white:
            if parity != (VAL[v.name] % 2) and dfs(v, VAL):
                return True
    start.visited == color.black
    return False

# Init(G)
#     for each v in V do
#         color1[v] = 'b'

# Algo(G)
#     Init(G)
#     for each v in Adj [u] do
#         if color1[v] == 'b' then
#             if !DFS_Visit(G,v,VAL[v]%2) then
#                 return false
#     return true

# DFS_Visit(G,v,parity)
#     color1[v] == 'g'
#     valid_path = false
#     for each u in Adj[v] do
#         if color1[u] == 'b' then
#             adj_parity = VAL[u]%2
#             if adj_parity == parity then
#                 if !DFS_Visity(G,u,adj_parity) then
#                     return false
#                 else valid_path = true
#             else valid_path = true
#         else if color1[u] == 'n' then
#             valid_path = true;
#     color1[v] = 'n'
#     return valid_path

if __name__ == "__main__":
    node1 = Node("A")
    node2 = Node("B")
    node3 = Node("C")
    node4 = Node("D")

    node1.append(node2)
    node1.append(node3)
    node2.append(node3)
    node2.append(node4)
    node3.append(node4)
    VAL = {"A": 1, "B": 3, "C": 4, "D": 5}
    print(dfs(node1, VAL))
