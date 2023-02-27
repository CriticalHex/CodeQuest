"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        dims: list[int] = []
        dims.extend(int(val) for val in line.split(" "))
        for i, d in enumerate(dims):
            if d % 2 == 0:  # even
                dims[i] += 2
            else:
                dims[i] += 1
        print(*dims)


main()
