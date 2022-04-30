import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())
for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    plays = list(val for val in line.split(" "))
    R = 0
    P = 0
    S = 0
    for i in plays:
        if i == "R":
            R+=1
        elif i == "P":
            P+=1
        elif i == "S":
            S+=1
    if "R" in plays and "S" in plays and "P" not in plays:
        if R > 1:
            print("NO WINNER")
        else:
            print("ROCK")
    elif "S" in plays and "P" in plays and "R" not in plays:
        if S > 1:
            print("NO WINNER")
        else:
            print("SCISSORS")
    elif "P" in plays and "R" in plays and "S" not in plays:
        if P > 1:
            print("NO WINNER")
        else:
            print("PAPER")
    else:
        print("NO WINNER")