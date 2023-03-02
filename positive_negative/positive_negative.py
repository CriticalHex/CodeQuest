"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        print("POSITIVE" if int(sys.stdin.readline().rstrip()) > 0 else "NEGATIVE")


main()
