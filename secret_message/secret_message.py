"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        n_lines = int(sys.stdin.readline().rstrip())
        encoded: list[str] = []
        for _ in range(n_lines):
            line = sys.stdin.readline().rstrip()
            encoded.append(line)
        line = sys.stdin.readline().rstrip()
        y, x = (int(val) for val in line.split(","))
        decoder: list[tuple[int, int]] = []
        n_lines = int(sys.stdin.readline().rstrip())
        for i in range(n_lines):
            line = sys.stdin.readline().rstrip()
            for j, c in enumerate(line):
                if c == "O":
                    decoder.append((i + y, j + x))
        output: str = ""
        for char in decoder:
            output += encoded[char[0]][char[1]]
        print(output)


main()
