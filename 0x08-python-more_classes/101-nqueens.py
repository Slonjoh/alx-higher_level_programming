#!/usr/bin/python3

"""
    The queens gambit
"""


import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at the given row and column.
    """
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    """
    Solve the N-Queens problem and return all solutions.
    """
    if n < 4:
        return []

    def solve(board, row):
        if row == n:
            solutions.append([(i, j) for i, row in enumerate(board)
                             for j, col in enumerate(row) if col == 1])
            return
        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                solve(board, row + 1)
                board[row][col] = 0

    solutions = []
    board = [[0] * n for _ in range(n)]
    solve(board, 0)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solutions = solve_nqueens(N)
        for solution in solutions:
            print(solution)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    except Exception:
        print("N must be at least 4")
        sys.exit(1)
