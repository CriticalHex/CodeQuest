"""System Module"""
import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    encrypted = sys.stdin.readline().rstrip()
    i = 0
    while i < len(encrypted):
        if encrypted[i] in ("a", "e", "i", "o", "u"):
            print(encrypted[i + 1], end="")
            i += 1
        i += 1
    print()
