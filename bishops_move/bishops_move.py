'''System Module'''
import sys

def even(x):
    '''is a number even'''
    if x % 2 == 0:
        return True
    return False

SEPARATOR = ","

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    rows, cols = (int(val) for val in line.split(SEPARATOR))
    grid = [[0 if even(j + i) else 1 for j in range(cols + 1)] for i in range(rows + 1)]
    line = sys.stdin.readline().rstrip()
    r1, c1 = (int(val) for val in line.split(SEPARATOR))
    line = sys.stdin.readline().rstrip()
    r2, c2 = (int(val) for val in line.split(SEPARATOR))
    if grid[r1][c1] == grid[r2][c2]:
        print("Yes")
    else:
        print("No")
    