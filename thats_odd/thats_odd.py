"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        print("EVEN" if int(sys.stdin.readline().rstrip()) % 2 == 0 else "ODD")


main()
