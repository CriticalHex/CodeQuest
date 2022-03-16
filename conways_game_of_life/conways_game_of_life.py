'''System Module'''
import sys

def inc_neighbors(y_pos, x_pos, arr):
    '''adds 1 to the count of each neighboring cell'''
    total = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if y_pos+i >= 0 and y_pos+i < 10 and x_pos+j >= 0 and x_pos+j < 10 and (y_pos + i, x_pos + j) != (y_pos,x_pos):
                if arr[y_pos+i][x_pos+j] != "0":
                    total += 1
    return total

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    grid = []
    GENERATIONS = int(sys.stdin.readline().rstrip())
    for i in range(10):
        grid.append(list(sys.stdin.readline().rstrip()))
    for k in range(GENERATIONS):
        NEIGHBORS = {}
        for i in range(10):
            for j in range(10):
                NEIGHBORS.update({(i,j):inc_neighbors(i, j, grid)})
        for i in range(10):
            for j in range(10):
                if NEIGHBORS.get((i,j)) >= 4 and grid[i][j] == "1":
                    grid[i][j] = "0"
                elif NEIGHBORS.get((i,j)) >= 2 and grid[i][j] == "1":
                    grid[i][j] = "1"
                elif NEIGHBORS.get((i,j)) >= 0 and grid[i][j] == "1":
                    grid[i][j] = "0"
                if NEIGHBORS.get((i,j)) == 3 and grid[i][j] == "0":
                    grid[i][j] = "1"
    for i in range(10):
        for j in range(10):
            print(grid[i][j], end="")
        print()
        