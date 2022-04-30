import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    c, p, s = (float(val) for val in line.split(" "))
    average = ((p+s)/2)
    if abs(p-s) > 5:
        print("WARNING")
    elif average-2 >= c:
        print("ALARM")
    else:
        print("OK")