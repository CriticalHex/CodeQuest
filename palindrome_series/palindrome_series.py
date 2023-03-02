"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        subcases = int(sys.stdin.readline().rstrip())
        bools: list[bool] = []
        for _ in range(subcases):
            line = sys.stdin.readline().rstrip().lower()
            if line == line[::-1]:
                bools.append(True)
            else:
                bools.append(False)
        if sum(bools) == len(bools):
            print("True")
        else:
            print("False - ", end="")
            output = ""
            for i, b in enumerate(bools):
                if not b:
                    output += str(i + 1) + ", "
            print(output.rstrip(", "))


main()
