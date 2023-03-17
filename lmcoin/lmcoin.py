"""System Module"""
import sys
import string


def val_num(val: str):
    ascii_list = list(string.ascii_lowercase)
    total: int = 0
    for c in val:
        total += ascii_list.index(c) + 1
    return total


def better_round(val: float, n_digits: int = 0) -> float:
    """Round Half Up"""
    val *= 10**n_digits
    result = int(val + (0.5 if val >= 0 else -0.5))
    return result / 10**n_digits


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        # guaranteed to be len 10
        values = sys.stdin.readline().rstrip().split(" ")
        dates = sys.stdin.readline().rstrip().split(" ")
        hashes: list[float] = [0]
        for i in range(1, 11):
            newhash: float = (
                int(dates[i - 1]) + val_num(values[i - 1]) + i + hashes[i - 1]
            )
            newhash *= 50 / 147
            hashes.append(newhash)
        print(int(better_round(hashes[-1])))


main()
