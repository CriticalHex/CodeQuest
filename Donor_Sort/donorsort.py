import sys

SEPARATOR = ","

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    bothyears = []
    line = sys.stdin.readline().rstrip()
    lastyear = [(str(val) for val in line.split(SEPARATOR))]
        
    line = sys.stdin.readline().rstrip()
    thisyear = [(str(val) for val in line.split(SEPARATOR))]
    
    for i in range(len(lastyear)):
        for j in range(len(thisyear)):
            if lastyear[i] == thisyear[j]:
                bothyears.append(lastyear[i])
                thisyear.remove[j]
                lastyear.remove[i]
    
    for i in range(len(bothyears)):
        print(bothyears[i],end=",")      
    # print(lastyear)
    # print(bothyears)
    # print(thisyear)