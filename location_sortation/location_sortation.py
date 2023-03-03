"""System Module"""
import sys


def main():
    countries: list[str] = []
    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        countries.append(sys.stdin.readline().rstrip())
    countries.sort()
    for c in countries:
        print(c)


main()
