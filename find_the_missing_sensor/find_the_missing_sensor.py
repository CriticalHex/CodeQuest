"""System Module"""
import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    n = int(sys.stdin.readline().rstrip())
    line = sys.stdin.readline().rstrip()
    sensors = list(int(val) for val in line.split(SEPARATOR))
    for i in range(1, n + 1):
        if i not in sensors:
            print(i)
            break
