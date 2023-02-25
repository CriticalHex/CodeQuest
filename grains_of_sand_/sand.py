'''System Module'''
import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    subCases = int(sys.stdin.readline().rstrip())
    OUTPUT = 0
    for _ in range(subCases):
        OUTPUT += int(sys.stdin.readline().rstrip())
    print(OUTPUT)