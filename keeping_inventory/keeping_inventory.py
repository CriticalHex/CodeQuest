"""System Module"""
import sys
import string


def key(part_num: str):
    values: list[float] = []
    for c in part_num:
        if c == "/":
            values.append(-3)
        elif c == ".":
            values.append(-2)
        elif c == "-":
            values.append(-1)
        elif c != "O" and c in string.ascii_uppercase:
            values.append(ord(c) - 65)
        else:
            if c in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                values.append(int(c) + 26)
            elif c == "O":
                values.append(26)
    return values


def main():
    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        part_nums: list[str] = []
        subcases = int(sys.stdin.readline().rstrip())
        for _ in range(subcases):
            line = sys.stdin.readline().rstrip()
            part_nums.append(line)
        part_nums.sort(key=key)
        for num in part_nums:
            print(num)


main()
