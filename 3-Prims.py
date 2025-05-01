#https://youtu.be/V9gXzD7g8fw?si=k0KRz21KqhkujS6X

# Prim's Algorithm (Character-labeled nodes)
# ------------------------------------------
# 1. Start from a given node (e.g., 'A').
# 2. Use a min-heap to find the smallest edge.
# 3. Add its connected node to the MST if not visited.
# 4. Repeat until all nodes are included.

# tc : E log V
# sc : V + E

# Data Structures Used:
# 1. Adjacency List: To represent the undirected weighted graph.
# 2. Min Heap (Priority Queue): To pick the edge with the smallest weight efficiently.
# 3. Visited Array: To track the vertices already included in the MST.

import heapq
class Graph:
    def __init__(self):
        self.graph = {}  # adjacency list

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # undirected

    def prim(self, start):
        visited = set()
        min_heap = [(0, start, None)]  # (weight, current_node, previous_node)
        mst_cost = 0
        mst_edges = []

        while min_heap:
            weight, current, prev = heapq.heappop(min_heap)

            if current in visited:
                continue

            visited.add(current)
            mst_cost += weight
            if prev is not None:
                mst_edges.append((prev, current, weight))

            for neighbor, w in self.graph[current]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (w, neighbor, current))

        print("Edges in the Minimum Spanning Tree:")
        for u, v, weight in mst_edges:
            print(f"{u} -- {v} == {weight}")
        print(f"Total cost of MST: {mst_cost}")

# ---- Example Usage ----
g = Graph()
g.add_edge('A', 'B', 4)
g.add_edge('A', 'C', 3)
g.add_edge('B', 'C', 1)
g.add_edge('B', 'D', 2)
g.add_edge('C', 'D', 4)
g.add_edge('D', 'E', 2)
g.add_edge('E', 'F', 6)

g.prim('A')
