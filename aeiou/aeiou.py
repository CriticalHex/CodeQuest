"""System Module"""
import sys


def main():
    vowels = ("a", "e", "i", "o", "u")
    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        count = sum(line.count(v) for v in vowels)
        print(count)


main()
