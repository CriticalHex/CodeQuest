"""System Module"""
import sys


def better_round(val: float, n_digits: int = 0):
    """Round Half Up"""
    val *= 10**n_digits
    result = int(val + (0.5 if val >= 0 else -0.5))
    rounded = result / 10**n_digits
    num, dec = str(rounded).split(".")
    while len(dec) < n_digits:
        dec += "0"
    return f"{num}.{dec}"


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        density, volume = (float(val) for val in line.split(" "))
        mass = density * volume
        print(better_round(mass, 2))


main()
