"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        print(sys.stdin.readline().rstrip().lower())


main()
