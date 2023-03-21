"""System Module"""
import sys


def swap_row_col(mat: list[list[int]]):
    flipped: list[list[int]] = [[] for _ in range(len(mat[0]))]
    for row in mat:
        for j, cell in enumerate(row):
            flipped[j].append(cell)
    return flipped


def pad(mat: list[list[int]]):
    longest = len(max(mat, key=len))
    for row in mat:
        while len(row) < longest:
            row.append(0)


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        left = sys.stdin.readline().rstrip()
        right = sys.stdin.readline().rstrip()
        left_vals = [int(val) for val in left.split()]
        right_vals = [int(val) for val in right.split()]
        new_vals: list[list[int]] = []
        for i, l in enumerate(left_vals):
            new_vals.append([0 for _ in range(i)])
            for r in right_vals:
                new_vals[i].append(l * r)
        eq: list[int] = []
        pad(new_vals)
        for col in swap_row_col(new_vals):
            eq.append(sum(col))
        output = ""
        for i, part in enumerate(eq):
            if part != 0:
                if part > 0:
                    output += "+"
                else:
                    output += "-"
                val = abs(part)
                if i == 0:
                    output += str(val)
                elif i == 1:
                    if val == 1:
                        output += "x"
                    else:
                        output += f"{val}x"
                else:
                    if val == 1:
                        output += f"x^{i}"
                    else:
                        output += f"{val}x^{i}"
        print(output.lstrip("+"))


main()
