import sys
import math

SEPARATOR1 = ":"
SEPARATOR2 = ","

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    SLG = 0
    atBats = 0
    Singles = 0
    Doubles = 0
    Triples = 0
    HomeRuns = 0

    line = sys.stdin.readline().rstrip()
    
    name, bats = (val for val in line.split(SEPARATOR1))
    name = str(name)
    bats = [str(val) for val in bats.split(SEPARATOR2)]
    for bat in bats:

        if bat != "BB":
            atBats += 1
        if bat == "1B":
            Singles += 1
        elif bat == "2B":
            Doubles += 1
        elif bat == "3B":
            Triples += 1
        elif bat == "HR":
            HomeRuns += 1
    if atBats != 0:
        SLG = format(((Singles + (2 * Doubles) + (3 * Triples) + (4 * HomeRuns))/atBats), '.3f')
    else:
        SLG = format(0, '.3f')
    #SLG = float(SLG)
    #OutputString = name + "=" + SLG
    print(name, "=", SLG, sep = "")