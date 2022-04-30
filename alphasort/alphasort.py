import sys
import math
import string

all = []

cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    all.append(line)
all.sort()
for i in all:
    print(i)