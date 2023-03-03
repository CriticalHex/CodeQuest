"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        val1, val2 = (float(val) for val in line.split(" "))
        print(int(val1 + val2), int(val1 * val2))

main()
