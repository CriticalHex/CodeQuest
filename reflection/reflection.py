"""System Module"""
import sys


def pad_mat(mat: list[list[str]]):
    longest = len(max(mat, key=len))
    for row in mat:
        while len(row) < longest:
            row.append(" ")


def pad_list(arr: list[str]):
    longest = len(max(arr, key=len))
    for i in range(len(arr)):
        while len(arr[i]) < longest:
            arr[i] = arr[i] + " "


def swap_row_col(mat: list[list[str]]):
    flipped: list[list[str]] = [[] for _ in range(len(mat[0]))]
    for row in mat:
        for j, cell in enumerate(row):
            flipped[j].append(cell)
    return flipped


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        n_lines = int(sys.stdin.readline().rstrip())
        lines: list[str] = []
        for _ in range(n_lines):
            line = sys.stdin.readline().rstrip()
            lines.append(line)
        instruction = sys.stdin.readline().rstrip()
        if instruction == "Y":
            pad_list(lines)
            for line in lines:
                print(*line[::-1], sep="")
        if instruction == "X":
            lines.reverse()
            for line in lines:
                print(*line, sep="")
        if instruction == "INVERSE":
            mat: list[list[str]] = []
            for line in lines:
                mat.append(list(line))
            pad_mat(mat)
            mat = swap_row_col(mat)
            for line in mat:
                if line:
                    print(*line, sep="")


main()
