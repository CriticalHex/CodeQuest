'''import libraries'''
import sys
import math

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    print(round(((math.pi * (int(line) * 2)) + 40075), 1))
    