'''System module'''
import sys

SEPARATOR = ","

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    bothyears = []
    lastyear = []
    thisyear = []
    line = sys.stdin.readline().rstrip()
    lastyear = line.split(SEPARATOR)
    line = sys.stdin.readline().rstrip()
    thisyear = line.split(SEPARATOR)
    for i in lastyear:
        for j in thisyear:
            if i == j:
                bothyears.append(i)
    for person in bothyears:
        thisyear.remove(person)
        lastyear.remove(person)
    bothyears.sort()
    BOTH = ",".join(bothyears)
    thisyear.sort()
    THIS = ",".join(thisyear)
    lastyear.sort()
    LAST = ",".join(lastyear)
    print(LAST)
    print(BOTH)
    print(THIS)
    