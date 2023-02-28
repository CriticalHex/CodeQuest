"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        times, herald = (int(val) for val in line.split(" "))
        if times == herald:
            print("Times and Herald have the same number of subscribers")
        elif times > herald:
            print(f"Times has {times - herald} more subscribers")
        elif herald > times:
            print(f"Herald has {herald - times} more subscribers")


main()
