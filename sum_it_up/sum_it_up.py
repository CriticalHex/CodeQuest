"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        x, y = (int(val) for val in line.split(" "))
        if x == y:
            print(2 * (x + y))
        else:
            print(x + y)


main()
