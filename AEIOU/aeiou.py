'''System module'''
import sys

SEPARATOR = " "
VOWELS = 0

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    for letter in line:
        if letter in ('a', 'e', 'i', 'o', 'u'):
            VOWELS += 1
    print(VOWELS)
    VOWELS = 0
    