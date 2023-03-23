"""System Module"""
import sys


def in_bounds(grid: list[list[str]], pos: tuple[int, int]):
    # pos is y,x
    if pos[0] >= 0 and pos[0] < len(grid) and pos[1] >= 0 and pos[1] < len(grid[0]):
        return True
    return False


def check_letter(
    grid: list[list[str]], y: int, x: int, index: int, word: str, good: list[str]
):
    if index == len(word):
        if word not in good:
            good.append(word)
        return True
    else:
        letter = word[index]
        around = [
            (y - 1, x - 1),
            (y - 1, x),
            (y - 1, x + 1),
            (y, x - 1),
            (y, x + 1),
            (y + 1, x - 1),
            (y + 1, x),
            (y + 1, x + 1),
        ]
        for pos in around:
            if in_bounds(grid, pos):
                found = grid[pos[0]][pos[1]]
                if found == letter:
                    if check_letter(grid, *pos, index + 1, word, good):
                        break


def worm(word: str, grid: list[list[str]], good: list[str]):
    for i, row in enumerate(grid):
        for j, char in enumerate(row):
            if char == word[0]:
                check_letter(grid, i, j, 1, word, good)


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        grid: list[list[str]] = []
        line = sys.stdin.readline().rstrip()
        rows, _ = (int(val) for val in line.split())
        for _ in range(rows):
            grid.append(input().split())
        subcases = int(sys.stdin.readline().rstrip())
        for _ in range(subcases):
            line = sys.stdin.readline().rstrip()
            good: list[str] = []
            worm(line, grid, good)
            for word in good:
                print(word)


main()
