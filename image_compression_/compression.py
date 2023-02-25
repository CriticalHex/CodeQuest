'''System Module'''
import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    subCases = int(sys.stdin.readline().rstrip())
    LINES = []
    OUTPUT = []
    for _ in range(subCases):
        LINES.append(float(sys.stdin.readline().rstrip()))
    for vals in LINES:
        OUTPUT.append(vals)
    OUTPUT.sort()
    MIN = OUTPUT[0]
    MAX = OUTPUT[len(OUTPUT) - 1]
    for val in LINES:
        print(round(((val - MIN)/(MAX - MIN)) * 255))
    