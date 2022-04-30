import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    subcases = int(sys.stdin.readline().rstrip())
    for _ in range(subcases):
        line = sys.stdin.readline().rstrip()
        line = line.upper()
        first, middle, last = ((val) for val in line.split(" "))
        print(first[0],last[0],middle[0],sep="")