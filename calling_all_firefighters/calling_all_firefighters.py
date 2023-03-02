"""System Module"""
import sys


def bresenham(x0: int, y0: int, x1: int, y1: int):
    """Yield integer coordinates on the line from (x0, y0) to (x1, y1).
    Input coordinates should be integers.
    The result will contain both the start and the end point.
    """
    dx: int = x1 - x0
    dy: int = y1 - y0

    xsign = 1 if dx > 0 else -1
    ysign = 1 if dy > 0 else -1

    dx = abs(dx)
    dy = abs(dy)

    if dx > dy:
        xx, xy, yx, yy = xsign, 0, 0, ysign
    else:
        dx, dy = dy, dx
        xx, xy, yx, yy = 0, ysign, xsign, 0

    d = 2 * dy - dx
    y = 0

    for x in range(dx + 1):
        yield x0 + x * xx + y * yx, y0 + x * xy + y * yy
        if d >= 0:
            y += 1
            d -= 2 * dx
        d += 2 * dy


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
                if space in (str(k) for k in list(range(1, n_antennae + 1))):
                    for pos in bresenham(j, i, *space0):
                        if grid[pos[1]][pos[0]] == "#":
                            break
                    else:
                        viable.append(space)

        if viable:
            viable.sort()
            print(*viable)
        else:
            print("No viable locations")


main()
