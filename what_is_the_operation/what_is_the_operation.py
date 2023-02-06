"""System Module"""
import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    a, b, c = (int(val) for val in line.split(SEPARATOR))
    if a + b == c:
        print("Addition")
    elif a - b == c:
        print("Subtraction")
    elif a * b == c:
        print("Multiplication")
    elif int(a / b) == c:
        print("Division")
    elif a % b == c:
        print("Modulo")
