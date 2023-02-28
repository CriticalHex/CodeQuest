"""System Module"""
import sys
import string


def better_round(val: float, n_digits: int = 0) -> float:
    """Round Half Up"""
    val *= 10**n_digits
    result = int(val + (0.5 if val >= 0 else -0.5))
    return result / 10**n_digits


def get_percent(value: str, dictionary: dict[str, int]):
    val = str(better_round(((dictionary[value] / sum(dictionary.values())) * 100), 2))
    num, dec = val.split(".")
    while len(dec) < 2:
        dec += "0"
    return f"{num}.{dec}"


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        lines = int(sys.stdin.readline().rstrip())
        frequencies: dict[str, int] = {}
        for l in string.ascii_uppercase:
            frequencies[l] = 0
        for _ in range(lines):
            line = sys.stdin.readline().rstrip().upper()
            for l in string.ascii_uppercase:
                frequencies[l] += line.count(l)
        for l in frequencies:
            percent = get_percent(l, frequencies)
            print(f"{l}: {percent}%")


main()
