"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        if (stripped := line.rstrip("th"))[-1] in ("1", "2", "3"):
            if len(stripped) > 1:
                if stripped[-2] == "1":
                    print(line)
                    continue
            if stripped[-1] == "1":
                print(stripped + "st")
            elif stripped[-1] == "2":
                print(stripped + "nd")
            else:
                print(stripped + "rd")
        else:
            print(line)


main()
