import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    subcases = int(sys.stdin.readline().rstrip())
    for _ in range(subcases):
        line = int(sys.stdin.readline().rstrip())
        yes = False
        if line < 1582:
            yes = False
        elif line % 4 != 0:
            yes = False
        elif line % 100 != 0:
            yes = True
        elif line % 400 != 0:
            yes = False
        else:
            yes = True
        if yes:
            print("Yes")
        else:
            print("No")
