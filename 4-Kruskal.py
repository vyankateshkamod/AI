#https://youtu.be/huQojf2tevI

# Algorithm:
# 1. Sort all the edges in non-decreasing order of their weights.
# 2. Initialize an empty MST set.
# 3. Make a disjoint set for each vertex (Union-Find structure).
# 4. For each edge (u, v):
#    a. If u and v are in different sets:
#       i. Add edge (u, v) to MST.
#       ii. Union the sets.
# 5. Repeat until MST has (V - 1) edges.


# ----------------------------- Time Complexity -----------------------------
# Sorting Edges: O(E * log E)
# DSU Operations: O(E * α(V)), where α is the inverse Ackermann function (very small, ~constant)
# Total Time Complexity: O(E * log E)
# - E = number of edges
# - V = number of vertices

# ----------------------------- Space Complexity -----------------------------
# O(V + E)
# - To store the parent and rank arrays (O(V))
# - To store the list of edges and MST result (O(E))

# ----------------------------- Data Structures Used -----------------------------
# 1. List of Edges:
#    - To hold all edges with their weights.
# 2. Set:
#    - To store unique vertices.
# 3. Disjoint Set (Union-Find with Path Compression & Union by Rank):
#    - To efficiently detect cycles while adding edges.
# 4. Result List:
#    - To store edges included in the MST.

# -----------------------------------------------------------------------------------


class Graph:
    def __init__(self):
        self.graph = []       # edges as (weight, u, v)
        self.nodes = set()    # unique set of nodes

    def add_edge(self, u, v, weight):
        self.graph.append((weight, u, v))
        self.nodes.add(u)
        self.nodes.add(v)

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[yroot] < rank[xroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []
        self.graph.sort()  # sort edges by weight

        parent = {}
        rank = {}

        for node in self.nodes:
            parent[node] = node
            rank[node] = 0

        for weight, u, v in self.graph:
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                result.append((u, v, weight))
                self.union(parent, rank, x, y)

        print("Edges in the Minimum Spanning Tree:")
        total_weight = 0 
        for u, v, weight in result:
            print(f"{u} -- {v} == {weight}")
            total_weight += weight
        print(f"Total weight of MST: {total_weight}")

# -------- Example --------
g = Graph()
g.add_edge('A', 'B', 4)
g.add_edge('A', 'C', 3)
g.add_edge('B', 'C', 1)
g.add_edge('B', 'D', 2)
g.add_edge('C', 'D', 4)
g.add_edge('D', 'E', 2)
g.add_edge('E', 'F', 6)

g.kruskal()
