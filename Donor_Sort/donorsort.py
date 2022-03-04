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
    bothyears_string = ",".join(bothyears)
    thisyear.sort()
    thisyear_string = ",".join(thisyear)
    lastyear.sort()
    lastyear_string = ",".join(lastyear)
    print(lastyear_string)
    print(bothyears_string)
    print(thisyear_string)
    