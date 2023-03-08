"""System Module"""
import sys


def get_depth(lines: list[str]):
    max_depth = 0
    current_depth = 0

    for line in lines:
        if line == "{":
            current_depth += 1
        elif line == "}":
            current_depth -= 1

        max_depth = max(max_depth, current_depth)

    return max_depth


def get_complexity(lines: list[str]):
    com = 1
    for line in lines:
        if line[:3] == "If ":
            com += 1
    return com


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        n_lines, max_cyclo, max_depth = (int(val) for val in line.split(" "))
        lines: list[str] = []
        for _ in range(n_lines):
            lines.append(sys.stdin.readline().rstrip())
        complexity, depth = get_complexity(lines), get_depth(lines)
        print(complexity, depth, end=" ")
        if complexity > max_cyclo or depth > max_depth:
            print("FAIL")
        else:
            print("PASS")


main()
