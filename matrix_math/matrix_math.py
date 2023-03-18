"""System Module"""
import sys


def swap_row_col(mat: list[list[int]]):
    flipped: list[list[int]] = [[] for _ in range(len(mat[0]))]
    for row in mat:
        for j, cell in enumerate(row):
            flipped[j].append(cell)
    return flipped


def mat_mul(a: list[list[int]], b: list[list[int]]):
    flipped_b = swap_row_col(b)
    mat: list[list[int]] = [[] for _ in range(len(flipped_b))]
    for row in a:
        for i, col in enumerate(flipped_b):
            mat[i].append(sum((x * y) for x, y in zip(row, col)))
    return swap_row_col(mat)


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        a_rows, a_cols, b_rows, _ = (int(val) for val in line.split(" "))
        a: list[list[int]] = []
        b: list[list[int]] = []
        for i in range(a_rows):
            a.append([])
            line = sys.stdin.readline().rstrip()
            a[i].extend(int(val) for val in line.split(" "))
        for i in range(b_rows):
            b.append([])
            line = sys.stdin.readline().rstrip()
            b[i].extend(int(val) for val in line.split(" "))
        if a_cols != b_rows:
            print("undefined")
        else:
            multiplied = mat_mul(a, b)
            for row in multiplied:
                print(*row)


main()
