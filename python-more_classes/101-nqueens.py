#!/usr/bin/python3
import sys


def is_valid(board, row, col):
    for r, c in board:
        if c == col or r + c == row + col or r - c == row - col:
            return False
    return True


def nqueens_helper(n, row, board, solutions):
    if row == n:
        solutions.append(board.copy())
    else:
        for col in range(n):
            if is_valid(board, row, col):
                board.append((row, col))
                nqueens_helper(n, row + 1, board, solutions)
                board.pop()


def nqueens(n):
    if not isinstance(n, int):
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solutions = []
    nqueens_helper(n, 0, [], solutions)
    for solution in solutions:
        print(solution)
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
