'''System Module'''
import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    grid = []
    line = sys.stdin.readline().rstrip()
    y, x = (int(val) for val in line.split(SEPARATOR))
    for i in range(20):
        grid.append([])
        for j in range(20):
            grid[i].append("10")
    for i in range(20):
        for j in range(20):
            if (i == y and j == x):
                grid[i][j] = "100"
                if i - 1 >= 0:
                    grid[i - 1][j] = "50"
                    if j - 1 >= 0:
                        grid[i - 1][j - 1] = "50"
                    if j + 1 < 20:
                        grid[i - 1][j + 1] = "50"
                if i + 1 < 20:
                    grid[i + 1][j] = "50"
                    if j - 1 >= 0:
                        grid[i + 1][j - 1] = "50"
                    if j + 1 < 20:
                        grid[i + 1][j + 1] = "50"
                if j - 1 >= 0:
                    grid[i][j - 1] = "50"
                if j + 1 < 20:
                    grid[i][j + 1] = "50"
                #---------------------------------------------------------------------
                if i - 2 >= 0:
                    grid[i - 2][j] = "25"
                    if j - 2 >= 0:
                        grid[i - 2][j - 1] = "25"
                        grid[i - 2][j - 2] = "25"
                    if j + 2 < 20:
                        grid[i - 2][j + 1] = "25"
                        grid[i - 2][j + 2] = "25"
                if i + 2 < 20:
                    grid[i + 2][j] = "25"
                    if j - 2 >= 0:
                        grid[i + 2][j - 1] = "25"
                        grid[i + 2][j - 2] = "25"
                    if j + 2 < 20:
                        grid[i + 2][j + 1] = "25"
                        grid[i + 2][j + 2] = "25"
                if j - 2 >= 0:
                    grid[i][j - 2] = "25"
                    if y - 1 >= 0:
                        grid[i - 1][j - 2] = "25"
                    if y + 1 < 20:
                        grid[i + 1][j - 2] = "25"
                    grid[i][j - 2] = "25"
                if j + 2 < 20:
                    grid[i][j + 2] = "25"
                    if y - 1 >= 0:
                        grid[i - 1][j + 2] = "25"
                    if y + 1 < 20:
                        grid[i + 1][j + 2] = "25"
    for i in range(20):
        for j in range(20):
            if j < 19:
                print(grid[i][j], end=" ")
            else:
                print(grid[i][j], end="")
        print()
    