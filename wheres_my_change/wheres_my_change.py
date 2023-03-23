"""System Module"""
import sys


def better_round(val: float, n_digits: int = 0) -> float:
    """Round Half Up"""
    val *= 10**n_digits
    result = int(val + (0.5 if val >= 0 else -0.5))
    return result / 10**n_digits


def change(val: float):
    give: list[int] = [0 for _ in range(11)]
    while val > 0:
        val = better_round(val, 2)
        if val - 100 >= 0:
            val -= 100
            give[0] += 1
        elif val - 50 >= 0:
            val -= 50
            give[1] += 1
        elif val - 20 >= 0:
            val -= 20
            give[2] += 1
        elif val - 10 >= 0:
            val -= 10
            give[3] += 1
        elif val - 5 >= 0:
            val -= 5
            give[4] += 1
        elif val - 2 >= 0:
            val -= 2
            give[5] += 1
        elif val - 1 >= 0:
            val -= 1
            give[6] += 1
        elif val - 0.25 >= 0:
            val -= 0.25
            give[7] += 1
        elif val - 0.10 >= 0:
            val -= 0.10
            give[8] += 1
        elif val - 0.05 >= 0:
            val -= 0.05
            give[9] += 1
        elif val - 0.01 >= 0:
            val -= 0.01
            give[10] += 1
    return give


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        charge = float(sys.stdin.readline().rstrip())
        given = change(charge)
        print(*given, sep="")


main()
