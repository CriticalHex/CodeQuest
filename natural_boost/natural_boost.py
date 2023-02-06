"""System Module"""
import sys
from math import pi, radians, cos, floor


def circum(radius: float | int):
    """circumference"""
    return pi * 2 * radius


SEPARATOR = " "
R = 6370000
S = 86400
cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    angle = float(sys.stdin.readline().rstrip())
    r = R * cos(radians(angle))
    print(floor(circum(r) / S))
