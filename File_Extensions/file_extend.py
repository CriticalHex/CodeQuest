'''System module'''
import sys

SEPARATOR = "."
DICTIONARY = {}

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    LINE = sys.stdin.readline().rstrip()
    DISCARD, EXTENSION = (str(val) for val in LINE.split(SEPARATOR))
    print(DICTIONARY.keys())
    if DICTIONARY.keys() == EXTENSION:
        DICTIONARY.update(EXTENSION, 2)
    else:
        DICTIONARY.update({EXTENSION:1})
print(DICTIONARY)
