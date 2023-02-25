'''import libraries'''
import sys

SEPARATOR1 = ":"
SEPARATOR2 = ","

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    SLG = 0
    AT_BATS = 0
    SINGLES = 0
    DOUBLES = 0
    TRIPLES = 0
    HOME_RUNS = 0

    line = sys.stdin.readline().rstrip()
    NAME, bats = (val for val in line.split(SEPARATOR1))
    NAME = str(NAME)
    bats = [str(val) for val in bats.split(SEPARATOR2)]
    for bat in bats:

        if bat != "BB":
            AT_BATS += 1
        if bat == "1B":
            SINGLES += 1
        elif bat == "2B":
            DOUBLES += 1
        elif bat == "3B":
            TRIPLES += 1
        elif bat == "HR":
            HOME_RUNS += 1
    if AT_BATS != 0:
        SLG = format(((SINGLES + (2 * DOUBLES) + (3 * TRIPLES) + (4 * HOME_RUNS))/AT_BATS), '.3f')
    else:
        SLG = format(0, '.3f')
    #SLG = float(SLG)
    #OutputString = name + "=" + SLG
    print(NAME, "=", SLG, sep = "")
    