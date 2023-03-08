"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        n_old, n_new = (int(val) for val in line.split(" "))
        old: list[str] = []
        new: list[str] = []
        old_emps: list[tuple[str, str, str]] = []
        new_emps: list[str] = []
        for _ in range(n_old):
            old.append(sys.stdin.readline().rstrip())
        for _ in range(n_new):
            new.append(sys.stdin.readline().rstrip())
        for entry in old:
            old_emps.append(tuple(entry.split(",")))
        for entry in new:
            new_emps.append(tuple(entry.split(",")))


main()
