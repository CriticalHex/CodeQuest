"""System Module"""
import sys
import string

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    digits = list(line)
    total: int = 0
    flag = False
    for d in digits[0:9]:
        if d not in list(string.digits):
            flag = True
            break
    if flag:
        continue
    for i in range(len(digits) - 1):
        total += int(digits[i]) * (10 - i)
    digit = 0
    for i in range(0, 11):
        if (total + i) % 11 == 0:
            digit = i
    if digits[-1] == "X":
        if digit == 10:
            print("VALID")
        else:
            print("INVALID")
    elif digits[-1] not in list(string.digits):
        print("INVALID")
    elif int(digits[-1]) == digit:
        print("VALID")
    else:
        print("INVALID")
