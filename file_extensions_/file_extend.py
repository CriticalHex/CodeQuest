'''System module'''
import sys

SEPARATOR = "."
DICTIONARY = {}

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    LINE = sys.stdin.readline().rstrip()
    DISCARD, EXTENSION = (str(val) for val in LINE.split(SEPARATOR))
    if EXTENSION in DICTIONARY.keys():
        temp = int(DICTIONARY.get(EXTENSION))
        temp += 1
        DICTIONARY.update({EXTENSION:temp})
    else:
        DICTIONARY.update({EXTENSION:1})
for val1, val2 in DICTIONARY.items():
    print(f"{val1} {val2}")
