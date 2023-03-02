"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = [int(val) for val in sys.stdin.readline().rstrip().split(",")]
        line.sort()
        print(*line, sep=",")


main()
