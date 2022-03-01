from cgitb import small
import sys

def wallBuilds(small, large, wall):
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
    if wallBuilds(smallBricks, largeBricks, wallSize) == True:
        print("true")
    else:
        print("false")
    
        