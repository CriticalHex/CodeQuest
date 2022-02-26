import sys

SEPARATOR = " "
VOWELS = 0

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    
    for i in range(len(line)):
        if line[i] == "a" or line[i] == "e" or line[i] == "i" or line[i] == "o" or line[i] == "u":
            VOWELS += 1

    print(VOWELS)
    VOWELS = 0