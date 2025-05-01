# DFS and BFS implementation (Human-typed version)

# -------- Algorithm for DFS and BFS --------
# DFS Algorithm:
# 1. Mark the current node as visited.
# 2. Visit all its adjacent unvisited nodes recursively.
# 3. Print the node as you visit it.
# 4. Repeat for all nodes connected to the starting node.

# BFS Algorithm:
# 1. Initialize a queue and add the starting node to the queue.
# 2. Mark the starting node as visited.
# 3. While the queue is not empty:
#    a. Remove the node from the front of the queue.
#    b. Visit all its unvisited neighbors and add them to the queue.
# 4. Print each node when visited.

# -------- Time Complexity --------
# DFS:
# - Time Complexity: O(V + E)
#   - V: number of vertices, E: number of edges
#   - Each vertex is visited once, and each edge is processed once in the DFS traversal.
# 
# BFS:
# - Time Complexity: O(V + E)
#   - Each vertex is visited once, and each edge is processed once in the BFS traversal.

# -------- Space Complexity --------
# - Both DFS and BFS require O(V) space to store the visited list (which tracks the visited nodes).
# - BFS also requires O(V) space to store the queue in the worst case.

# -------- Data Structures Used --------
# - Graph representation: Adjacency List (using a dictionary with lists as values)
# - DFS: Recursion stack (for the DFS traversal) and a visited list
# - BFS: Queue (from collections.deque) and a visited list

from collections import deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = {}  # using regular dict to store adjacency list

        # Initialize empty adjacency list for each vertex
        for i in range(vertices):
            self.graph[i] = []

    # Add edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Undirected graph, so add both ways

    # Recursive DFS function
    def dfs_util(self, v, visited):
        visited[v] = True
        print(v, end=' ')
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.dfs_util(neighbor, visited)

    # Perform DFS starting from a specific vertex
    def dfs(self, start):
        visited = [False] * self.vertices
        print("DFS from", start, "->", end=' ')
        self.dfs_util(start, visited)
        print()

    # Perform BFS starting from a specific vertex
    def bfs(self, start):
        visited = [False] * self.vertices
        queue = deque()
        queue.append(start)
        visited[start] = True
        print("BFS from", start, "->", end=' ')

        while queue:
            node = queue.popleft()
            print(node, end=' ')
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        print()



# -------- Example --------
n = 8
edges = [(0, 1), (0, 2), (1, 3), (2, 4), (3, 5), (3, 6), (5, 7)]

g = Graph(n)

# Add edges to the graph
for u, v in edges:
    g.add_edge(u, v)

# Perform DFS and BFS starting from vertex 0
g.dfs(0)
g.bfs(0)
