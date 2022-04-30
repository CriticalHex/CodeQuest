import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    number, style = ((val) for val in line.split(" "))
    number = list(number)
    if style == "PARENTHESES":
        number.insert(0, '(')
        number.insert(4, ')')
        number.insert(5, ' ')
        number.insert(9, '-')
    elif style == "DASHES":
        number.insert(3, '-')
        number.insert(7, '-')
    elif style == "PERIODS":
        number.insert(3, '.')
        number.insert(7, '.')
    for i in number:
        print(i,end="")
    print()