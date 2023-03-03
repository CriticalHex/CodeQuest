"""System Module"""
import sys


def coprime(x0: int, x1: int):
    if x1 > x0:
        x0, x1 = x1, x0
    diff = x0 - x1
    print(f"{x0}-{x1}={diff}")
    if x0 == x1:
        if x0 == 1:
            print("COPRIME")
            return
        else:
            print("NOT COPRIME")
            return
    coprime(x1, diff)


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        x0, x1 = (int(val) for val in line.split(","))
        coprime(x0, x1)


main()
