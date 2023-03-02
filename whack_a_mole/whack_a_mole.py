"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip().split(" ")
        moles: list[int] = []
        for i, c in enumerate(line):
            if c == "M":
                moles.append(i + 1)
        print(*moles, sep=" ")


main()
