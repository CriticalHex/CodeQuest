"""System Module"""
import sys


def better_round(val: float, n_digits: int = 0) -> float:
    """Round Half Up"""
    val *= 10**n_digits
    result = int(val + (0.5 if val >= 0 else -0.5))
    return result / 10**n_digits


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        region = sys.stdin.readline().rstrip()
        subcases = int(sys.stdin.readline().rstrip())
        values: list[tuple[str, str]] = []
        for _ in range(subcases):
            line = sys.stdin.readline().rstrip()
            value, year = line.split(" ")
            values.append((year, value))
        values.sort(key=lambda x: x[0])
        print(f"{region}:")
        for pair in values:
            rounded = better_round(float(pair[1]), -3)
            stars = ""
            for _ in range(int(rounded / 1000)):
                stars += "*"
            pair = (pair[0], stars)
            print(*pair)


main()
