#https://youtu.be/BdSJnIdR-4s
# N-Queens Problem using Backtracking with Branch and Bound

# Algorithm:
# 1. Place queens row by row.
# 2. For each row, try placing a queen in each column.
# 3. Check constraints:
#    - No queen in the same column.
#    - No queen on upper left or right diagonals.
# 4. If constraints are satisfied, place the queen and move to the next row.
# 5. If a placement leads to a dead end, backtrack (remove the queen and try next column).
# 6. Continue until all queens are placed or all possibilities are exhausted.

# tc : n!
# sc : n sq

def is_safe(board, row, col, n):
    # Check column above
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True

def solve_n_queens(board, row, n):
    if row == n:
        for r in board:
            print(" ".join(" Q" if c == 1 else " ." for c in r))
        print()
        return True  # change to False to print *all* solutions

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens(board, row + 1, n):
                return True
            board[row][col] = 0  # backtrack

    return False

# Main
n = 2
board = [[0 for _ in range(n)] for _ in range(n)]
solve_n_queens(board, 0, n)
