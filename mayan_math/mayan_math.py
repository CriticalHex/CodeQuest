"""System Module"""
import sys


def itom(num: int):
    values = [
        "0",
        ".",
        "..",
        "...",
        "....",
        "-",
        ".-",
        "..-",
        "...-",
        "....-",
        "--",
        ".--",
        "..--",
        "...--",
        "....--",
        "---",
        ".---",
        "..---",
        "...---",
        "....---",
    ]
    output = ""
    for digit in range(3, -1, -1):
        max_at_digit = 20**digit
        for i in range(len(values), -1, -1):
            if num - (i * max_at_digit) >= 0:
                num -= i * max_at_digit
                if values[i] != "0" or output:
                    output += f" {values[i]}"
                    break
    return output.lstrip()


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        num = int(sys.stdin.readline().rstrip())
        print(itom(num))


main()
