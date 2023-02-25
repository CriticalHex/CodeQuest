'''System module'''
import sys

def can_build(small, large, wall):
    '''Checks if your bricks can build a wall'''
    for i in range(small + 1):
        for j in range(large + 1):
            if (i) + (5 * j) == wall:
                return True
    return False

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    smallBricks, largeBricks, wallSize = (int(val) for val in line.split(SEPARATOR))
    if can_build(smallBricks, largeBricks, wallSize):
        print("true")
    else:
        print("false")
        