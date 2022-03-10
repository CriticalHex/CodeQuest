'''System Module'''
import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    g1, g2 = (str(val) for val in line.split(SEPARATOR))
    if g1 == g2:
        print("true")
    else:
        print("false")
    