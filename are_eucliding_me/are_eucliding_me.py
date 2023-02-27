'''System Module'''
import sys

SEPARATOR = ","


cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    val1, val2 = (int(val) for val in line.split(SEPARATOR))
    COPRIME = False
    OUTPUT = -1
    while OUTPUT != 0:
        if val1 < val2:
            val1, val2 = val2, val1
        if val1 == 1 and val2 == 1:
            COPRIME = True
        OUTPUT = val1 - val2
        print(val1, "-", val2, "=", OUTPUT, sep = "")
        val1 = val2
        val2 = OUTPUT
    if not COPRIME:
        print("NOT COPRIME")
    else:
        print("COPRIME")
