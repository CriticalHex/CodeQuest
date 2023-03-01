"""System Module"""
import sys


def better_round(val: float, n_digits: int = 0) -> str:
    """Round Half Up"""
    val *= 10**n_digits
    result = int(val + (0.500002 if val >= 0 else -0.500002))
    rounded = str(result / 10**n_digits)
    num, dec = rounded.split(".")
    while len(dec) < n_digits:
        dec += "0"
    return f"{num}.{dec}"


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        val1, val2 = (float(val) for val in line.split(" "))
        print(better_round(val1 * val2, 2))


main()
