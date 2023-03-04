"""System Module"""
import sys
from math import sqrt


def dist(x0: int, y0: int, z0: int, x1: int, y1: int, z1: int):
    return sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2 + (z1 - z0) ** 2)


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = [int(val) for val in sys.stdin.readline().rstrip().split()]
        chroma = line[0:3]
        tolerance = line[3]
        foreground = line[4:7]
        background = line[7:10]
        distance = dist(*chroma, *foreground)
        if distance < tolerance:
            print(*background)
        else:
            print(*foreground)

main()
