'''System Module'''
import sys

def render_out(y_pos, x_pos, arr):
    '''adds 1 to the count of each neighboring cell'''
    for ypos in range(-1, 2):
        for xpos in range(-1, 2):
            if y_pos+ypos >= 0 and y_pos+ypos < ROWS and x_pos+xpos >= 0 and x_pos+xpos < COLS:
                if arr[y_pos+ypos][x_pos+xpos] != "100":
                    arr[y_pos+ypos][x_pos+xpos] = "50"
    for ypos in range(-2, 3):
        for xpos in range(-2, 3):
            if y_pos+ypos >= 0 and y_pos+ypos < ROWS and x_pos+xpos >= 0 and x_pos+xpos < COLS:
                if arr[y_pos+ypos][x_pos+xpos] != "100" and arr[y_pos+ypos][x_pos+xpos] != "50":
                    arr[y_pos+ypos][x_pos+xpos] = "25"
    return arr

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())
ROWS = 20
COLS = 20

for caseNum in range(cases):
    grid = []
    line = sys.stdin.readline().rstrip()
    y, x = (int(val) for val in line.split(SEPARATOR))
    for i in range(ROWS):
        grid.append([])
        for j in range(COLS):
            grid[i].append("10")
    for i in range(ROWS):
        for j in range(COLS):
            if (i == y and j == x):
                grid[i][j] = "100"
                grid = render_out(i,j,grid)
    for i in range(ROWS):
        for j in range(COLS):
            if j < COLS - 1:
                print(grid[i][j], end=" ")
            else:
                print(grid[i][j], end="")
        print()
    