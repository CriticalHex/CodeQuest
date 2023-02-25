"""System Module"""
import sys


def direct(x1: int, y1: int, x2: int, y2: int):
    steep = abs(y2 - y1) > abs(x2 - x1)
    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    dx = x2 - x1
    dy = abs(y2 - y1)
    error = dx // 2
    ystep = 1 if y1 > y2 else -1
    y = y1
    for x in range(x1, x2 + 1):
        # y, x (backwards) or x, y (as inputted)
        val = (y if steep else x, x if steep else y)
        if val[1] >= 0:
            yield val
        error = error - dy
        if error < 0:
            y += ystep
            error += dx


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        height, width, n_antennae = (int(val) for val in line.split(" "))
        grid: list[list[str]] = []
        for i in range(height):
            grid.append(list(sys.stdin.readline().rstrip()))
        for row in grid:
            while len(row) < width:
                row.append(" ")

        space0 = (0, 0)
        for i, row in enumerate(grid):
            for j, space in enumerate(row):
                if space == "0":
                    space0 = (j, i)

        viable: list[str] = []
        for i, row in enumerate(grid):
            for j, space in enumerate(row):
                for i in range(1, n_antennae + 1):
                    if space == str(i):
                        for pos in direct(j, i, *space0):
                            if grid[pos[1]][pos[0]] == "#":
                                break
                        else:
                            viable.append(space)

        if viable:
            viable.sort()
            output = ""
            for v in viable:
                output += v + " "
            print(output.rstrip())
        else:
            print("No viable locations")


main()
