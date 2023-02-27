"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        print("PASS" if int(sys.stdin.readline().rstrip()) >= 70 else "FAIL")


main()
