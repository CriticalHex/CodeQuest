"""System Module"""
import sys
from math import sqrt


def circle(radius: float, x: float):
    if x > radius:
        return -1
    xsq = x**2
    rsq = radius**2
    return sqrt(rsq - xsq)


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        radius, width, height = (float(val) for val in line.split(" "))
        pairs: list[tuple[int, int]] = []
        for i in range(int(height + 1)):
            for j in range(int(width + 1)):
                if i > circle(radius, j):
                    pairs.append((j, i))
        pairs.sort(key=lambda x: x[0])
        for pair in pairs:
            x, y = pair
            print(f"{x}, {y}")


main()
