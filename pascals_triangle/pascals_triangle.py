"""System Module"""
import sys


def generate():
    triangle: list[list[int]] = [[1]]
    for i in range(1, 60):
        triangle.append([])
        for j in range(len(triangle[i - 1]) + 1):
            if j == 0 or j == len(triangle[i - 1]):
                triangle[i].append(1)
            else:
                triangle[i].append(triangle[i - 1][j - 1] + triangle[i - 1][j])
    return triangle


def main():
    triangle = generate()
    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = int(sys.stdin.readline().rstrip())
        print(max(triangle[line]))


main()
