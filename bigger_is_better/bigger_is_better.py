"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())

    for _ in range(cases):
        print(max([int(val) for val in input().split(" ")]))


main()
