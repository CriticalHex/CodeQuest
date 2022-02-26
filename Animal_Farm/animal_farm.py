import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    
    turkeys, goats, horses = (int(val) for val in line.split(SEPARATOR))

    print((turkeys * 2) + (goats * 4) + (horses * 4))