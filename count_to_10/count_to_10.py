"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        bits = int(sys.stdin.readline().rstrip())
        for i in range(2**bits):
            print(f"{i:0>{bits}b}")


main()
