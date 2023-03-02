"""System Module"""
import sys


def main():

    decision_table: dict[int, int] = {
        -15: 2,
        -14: 1,
        -13: 2,
        -12: 1,
        -11: 2,
        -10: 2,
        -9: 1,
        -8: 2,
        -7: 1,
        -6: 1,
        -5: 2,
        -4: 2,
        -3: 1,
        -2: 2,
        -1: 1,
        0: 1,
        1: 2,
        2: 1,
        3: 1,
        4: 1,
        5: 2,
        6: 1,
        7: 1,
        8: 1,
        9: 1,
        10: 1,
        11: 1,
        12: 2,
    }

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        us, them = (int(val) for val in line.split(" "))
        up = us - them
        if (result := decision_table.get(up)) is not None:
            print(result)
        else:
            print(1)


main()
