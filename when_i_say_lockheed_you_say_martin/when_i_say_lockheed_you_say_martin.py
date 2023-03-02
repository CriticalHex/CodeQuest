"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        number = int(sys.stdin.readline().rstrip())
        flag = False
        if number % 3 == 0:
            flag = True
            print("LOCKHEED", end="")
        if number % 7 == 0:
            flag = True
            print("MARTIN", end="")
        if not flag:
            print(number)
        else:
            print()


main()
