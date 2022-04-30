import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    newline = []
    for i in range(len(line)-1, -1, -1):
        newline.append(line[i])
    for i in newline:
        print(i, end="")
    print()