'''System Module'''
import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    subCases = int(sys.stdin.readline().rstrip())
    for _ in range(subCases):
        line = sys.stdin.readline().rstrip()
        temp, scale = (str(val) for val in line.split(SEPARATOR))
        temp = float(temp)
        if scale == "F":
            print(line, "=", format((5 / 9) * (temp - 32), '.1f'), "C", sep = " ")
        else:
            print(line, "=", format((((9 * temp) / 5) + 32), '.1f'), "F", sep = " ")
        