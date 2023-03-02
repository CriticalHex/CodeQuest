"""System Module"""
import sys


def better_round(val: float, n_digits: int = 0):
    """Round Half Up"""
    val *= 10**n_digits
    result = int(val + (0.5000001 if val >= 0 else -0.5000001))
    rounded = result / 10**n_digits
    num, dec = str(rounded).split(".")
    while len(dec) < n_digits:
        dec += "0"
    return f"{num}.{dec}"


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        charge = float(line[1:])
        print(f"Total of the bill: {line}")
        print(f"15% = ${better_round(charge * 0.15, 2)}")
        print(f"18% = ${better_round(charge * 0.18, 2)}")
        print(f"20% = ${better_round(charge * 0.20, 2)}")


main()
