'''System module'''
import sys
from math import factorial

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = int(sys.stdin.readline().rstrip())
    print(factorial(line))
    