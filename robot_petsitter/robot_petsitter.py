"""System Module"""
import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    y: int = 0
    x: int = 0
    for c in line:
        if c == "R":
            x += 1
        if c == "L":
            x -= 1
        if c == "U":
            y += 1
        if c == "D":
            y -= 1
    if (x, y) == (0, 0):
        print("TRUE")
    else:
        print("FALSE")
