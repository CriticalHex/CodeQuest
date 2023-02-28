"""System Module"""
import sys


def better_round(val: float, n_digits: int = 0) -> str:
    """Round Half Up"""
    val *= 10**n_digits
    result = int(val + (0.5 if val >= 0 else -0.5))
    rounded = str(result / 10**n_digits)
    num, dec = rounded.split(".")
    while len(dec) < n_digits:
        dec += "0"
    return f"{num}.{dec}"


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        n_charges = int(sys.stdin.readline().rstrip())
        savings: float = 0
        for _ in range(n_charges):
            charge = float(sys.stdin.readline().rstrip())
            rounded = int(charge + 1)
            savings += rounded - charge
            print(rounded)
        print(better_round(savings, 2))


main()
