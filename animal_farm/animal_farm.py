"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        turkeys, goats, horses = (int(val) for val in line.split(" "))
        print((turkeys * 2) + (goats * 4) + (horses * 4))


main()
