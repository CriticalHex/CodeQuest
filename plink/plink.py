"""System Module"""
import sys
import math


class Node:
    """Graph nodes"""

    def __init__(self) -> None:
        self.visited = False
        self.adjacent: list[tuple[int, Node]]  # current score, next node
        self.score = -math.inf


def get_line() -> str:
    """Get rstripped stdin line"""
    return sys.stdin.readline().rstrip()


# def get_key(val):  # type: ignore
#     """inverse of getValue"""
#     for key, value in results.items():
#         if val == value:
#             return key


# def plinko(B, i=0, j=0, path="", total=0):
#     """Recursive function to determine best plinko path in a given board"""
#     if i >= len(B) - 1:
#         results[path] = total + B[i][j]
#     else:
#         plinko(B, i + 1, j, path + "L", total + B[i][j])
#         plinko(B, i + 1, j + 1, path + "R", total + B[i][j])


def main():
    """Main"""
    cases = int(get_line())
    for _ in range(cases):
        board: list[list[int]] = []
        rows = int(get_line())
        for row in range(rows + 1):
            line = get_line()
            board.append([])
            for val in line.split(" "):
                board[row].append(int(val))


main()
