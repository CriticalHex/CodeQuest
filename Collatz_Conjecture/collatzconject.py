import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = int(sys.stdin.readline().rstrip())
    start = line
    iter = 0
    while line != 1:
        iter += 1
        if line % 2 == 0:
            line /= 2
        else:
            line = (line * 3) + 1
    print(start, ":", iter + 1, sep = "")