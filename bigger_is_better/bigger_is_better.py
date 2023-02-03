"""System Module"""
import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    scores = list(int(val) for val in line.split(SEPARATOR))
    print(max(scores))
