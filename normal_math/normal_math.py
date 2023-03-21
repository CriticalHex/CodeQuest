"""System Module"""
import sys
from itertools import chain
from math import sqrt


def frobenius(mat: list[list[int]]):
    return sqrt(sum(cell**2 for cell in chain.from_iterable(zip(*mat))))


def better_round(val: float, n_digits: int = 0) -> str:
    """Round Half Up"""
    val *= 10**n_digits
    result = int(val + (0.5 if val >= 0 else -0.5))
    val = result / 10**n_digits
    num, dec = str(val).split(".")
    while len(dec) < n_digits:
        dec += "0"
    return f"{num}.{dec}"


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        rows, _ = (int(val) for val in line.split(" "))
        mat: list[list[int]] = []
        for _ in range(rows):
            mat.append([int(val) for val in input().split(" ")])
        print(better_round(frobenius(mat), 2))


main()
