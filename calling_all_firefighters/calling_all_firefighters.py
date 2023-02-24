"""System Module"""
import sys
from math import dist


class Node:
    def __init__(self, val: str) -> None:
        self.distance: None | int = None
        self.val = val
        self.directions: list[bool] = [True, True, True, True]


def direct(p1: tuple[int, int], p2: tuple[int, int]):
    count = 0
    if p1[0] > p2[0]:
        x1, x2 = p2[0], p1[0]
    else:
        x1, x2 = p1[0], p2[0]
    # x2 is bigger
    while x2 > x1:
        count += 1
        x1 += 1
    if p1[1] > p2[1]:
        y1, y2 = p2[1], p1[1]
    else:
        y1, y2 = p1[1], p2[1]
    # y2 is bigger
    while y2 > y1:
        count += 1
        y1 += 1
    return count


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        height, width, n_antennae = (int(val) for val in line.split(" "))
        grid: list[list[Node]] = []
        for i in range(height):
            grid.append([])
            grid[i].extend(Node(val) for val in list(sys.stdin.readline().rstrip()))
        for row in grid:
            while len(row) < width:
                row.append(Node(" "))

        for i, row in enumerate(grid):
            for j, room in enumerate(row):
                if j == len(row) - 1 or grid[i][j + 1].val == "#":
                    room.directions[1] = False
                if j == 0 or grid[i][j - 1].val == "#":
                    room.directions[3] = False
                if i == len(grid) - 1 or grid[i + 1][j].val == "#":
                    room.directions[2] = False
                if i == 0 or grid[i - 1][j].val == "#":
                    room.directions[0] = False

        node0 = (0, 0)
        for i, row in enumerate(grid):
            for j, node in enumerate(row):
                if node.val == "0":
                    node.distance = -1
                    node0 = (j, i)

        finished: bool = False
        while not finished:
            finished: bool = True

            for i, row in enumerate(grid):
                for j, node in enumerate(row):
                    if node.distance is None:
                        distances: list[int] = []

                        if node.directions[0]:
                            if grid[i - 1][j].distance is not None:
                                distances.append(grid[i - 1][j].distance)  # type: ignore
                        if node.directions[1]:
                            if row[j + 1].distance is not None:
                                distances.append(row[j + 1].distance)  # type: ignore
                        if node.directions[2]:
                            if grid[i + 1][j].distance is not None:
                                distances.append(grid[i + 1][j].distance)  # type: ignore
                        if node.directions[3]:
                            if row[j - 1].distance is not None:
                                distances.append(row[j - 1].distance)  # type: ignore

                        if distances:
                            node.distance = min(distances) + 1
                            finished: bool = False

        viable: list[str] = []
        for i, row in enumerate(grid):
            for j, node in enumerate(row):
                for i in range(1, n_antennae + 1):
                    if node.val == str(i):
                        if node.distance is not None:
                            # print(i, node.distance, direct((j, i), node0))
                            if node.distance <= direct((j, i), node0):
                                viable.append(node.val)
                                # print(node.val, end=" ")
        if viable:
            output = ""
            for v in viable:
                output += v + " "
            print(output.rstrip())
        else:
            print("No viable locations")


main()
