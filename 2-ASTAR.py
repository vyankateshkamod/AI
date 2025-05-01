
#https://youtu.be/nmWGhb9E4es?si=Bl_iE9VnUo6jDHdU
#https://youtu.be/LYkbWAQWGro?si=JyPKqZ2IqQyFZrv5


# ----------------------------- Algorithm Used -----------------------------
# We use the A* (A-Star) Search Algorithm to solve the 8 puzzle problem.
# The algorithm uses a priority queue to explore puzzle states with the lowest cost first.
# Cost = g(n) + h(n), where:
# - g(n): number of moves taken to reach current state
# - h(n): heuristic estimate of cost to reach goal (Manhattan Distance)
# The state with the lowest total estimated cost is expanded first.

# ----------------------------- Time Complexity -----------------------------
# Worst-case Time Complexity: O(b^d)
# Where:
# - b = branching factor (up to 4 for the 8-puzzle: up, down, left, right)
# - d = depth of the solution (average depth is around 20–30 moves)
# In the worst case, we may need to explore all 9! = 362,880 possible states.

# ----------------------------- Space Complexity -----------------------------
# Worst-case Space Complexity: O(b^d)
# - All states are stored in the visited set and the priority queue (open list).
# - Each state requires O(1) space (9 integers), but the number of states can be large.

# ----------------------------- Data Structures Used -----------------------------
# 1. Priority Queue (heapq):
#    - Used to always expand the node with the least cost (g + h).
# 2. Set:
#    - To store visited states and prevent cycles.
# 3. Tuple:
#    - Represents puzzle states because tuples are immutable and hashable.
# 4. Custom Class (PuzzleState):
#    - Encapsulates puzzle configuration, move count, and parent reference for path tracing.

# --------------------------------------------------------------------------------------------


import heapq

# Goal state for reference
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Convert 2D list to tuple for hashing
def to_tuple(state):
    return tuple(tuple(row) for row in state)

# Get the position of a number in a matrix
def find_pos(state, num):
    for i in range(3):
        for j in range(3):
            if state[i][j] == num:
                return i, j

# Manhattan Distance Heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                goal_i, goal_j = find_pos(goal_state, val)
                distance += abs(goal_i - i) + abs(goal_j - j)
    return distance

# Generate possible moves
def get_neighbors(state):
    neighbors = []
    x, y = find_pos(state, 0)
    moves = [(-1,0), (1,0), (0,-1), (0,1)]  # up, down, left, right

    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# A* Algorithm
def a_star(start_state):
    start_tuple = to_tuple(start_state)
    goal_tuple = to_tuple(goal_state)

    open_list = []
    heapq.heappush(open_list, (manhattan_distance(start_state), 0, start_state))
    visited = set()
    parent = {to_tuple(start_state): None}
    cost_so_far = {start_tuple: 0}

    while open_list:
        _, cost, current = heapq.heappop(open_list)
        current_tuple = to_tuple(current)

        if current_tuple == goal_tuple:
            path = []
            while current:
                path.append(current)
                current = parent[to_tuple(current)]
            return path[::-1]

        if current_tuple in visited:
            continue
        visited.add(current_tuple)

        for neighbor in get_neighbors(current):
            neighbor_tuple = to_tuple(neighbor)
            new_cost = cost + 1

            if neighbor_tuple not in cost_so_far or new_cost < cost_so_far[neighbor_tuple]:
                cost_so_far[neighbor_tuple] = new_cost
                priority = new_cost + manhattan_distance(neighbor)
                heapq.heappush(open_list, (priority, new_cost, neighbor))
                parent[neighbor_tuple] = current

    return None

# ----- Main Execution -----
start_state = [
    [1, 2, 3],
    [0, 4, 5],
    [6, 7, 8]
]

solution = a_star(start_state)

if solution:
    print("Solution steps:")
    for step in solution:
        for row in step:
            print(' '.join(str(x) if x != 0 else '_' for x in row))
        print()
else:
    print("No solution found.")
