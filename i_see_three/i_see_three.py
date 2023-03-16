"""System Module"""
import sys


def main():
    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        nums = [int(val) for val in line.split(" ")]
        counts: list[int] = []
        for i in range(max(nums)):
            counts.append(nums.count(i))
        if 3 in counts:
            print("TRUE")
        else:
            print("FALSE")


main()
