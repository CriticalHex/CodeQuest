"""System Module"""
import sys
import string

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    for c in line:
        if c in string.ascii_letters or c in string.digits or c == " ":
            print(c, end="")
    print()
