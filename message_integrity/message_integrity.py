"""System Module"""
import sys


def divide(binary: str):
    divide_by = "1011"
    div = divide_by
    while int(binary, 2) >= 11:
        div = divide_by
        while len(div) < len(binary):
            div += "0"
        binary = f"{(int(binary,2) ^ int(div,2)):>b}"
    if int(binary, 2) == 0:
        return True
    return False


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        binary = sys.stdin.readline().rstrip()
        if divide(binary):
            print("ok")
        else:
            print("corrupt")


main()
