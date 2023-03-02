"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        width = int(sys.stdin.readline().rstrip())
        for _ in range(width):
            line = ""
            for _ in range(width):
                line += "# "
            print(line.rstrip())


main()
