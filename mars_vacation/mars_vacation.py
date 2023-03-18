"""System Module"""
import sys
from math import dist, degrees, acos


def angle(a: float, b: float, c: float):
    return degrees(acos(((-c * c) + (a * a) + (b * b)) / (2 * a * b)))


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        ex, ey, mx, my = (float(val) for val in line.split(" "))
        a = dist((ex, ey), (0, 0))  # earth to sun
        b = dist((ex, ey), (mx, my))  # earth to mars
        c = dist((mx, my), (0, 0))  # mars to sun
        if angle(a, b, c) < 2:
            print("VACATION")
        else:
            print("WORKING HARD")


main()
