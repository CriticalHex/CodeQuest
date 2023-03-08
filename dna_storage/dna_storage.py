"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        binary: list[str] = []
        for i in range(0, len(line), 7):
            binary.append(line[i : i + 7])
        for i, s in enumerate(binary):
            temp = ""
            for c in s:
                if c in ("G", "C"):
                    temp += "1"
                else:
                    temp += "0"
            binary[i] = temp
        for s in binary:
            print(chr(int(s, 2)), end="")
        print()


main()
