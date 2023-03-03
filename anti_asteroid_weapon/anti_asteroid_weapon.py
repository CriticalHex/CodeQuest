"""System Module"""
import sys
from math import sqrt


def dist(x: int, y: int):
    return sqrt(x**2 + y**2)


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        asteroids: dict[tuple[int, int], float] = {}
        subcases = int(sys.stdin.readline().rstrip())
        for _ in range(subcases):
            line = sys.stdin.readline().rstrip()
            x, y = (int(val) for val in line.split(" "))
            asteroids[x, y] = dist(x, y)
        asteroid_list = list(asteroids.keys())
        asteroid_list.sort(key=lambda x: asteroids[x])
        for a in asteroid_list:
            print(*a)


main()
