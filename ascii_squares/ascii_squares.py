"""System Module"""
import sys


class Square:
    def __init__(self, up: bool, down: bool, left: bool, right: bool) -> None:
        self.directions: list[bool] = [up, down, left, right]


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        height = int(line)
        lines: list[str] = []
        tiles: list[list[Square]] = []
        for i in range(height):
            lines.append(sys.stdin.readline().rstrip())
        for i, line in enumerate(lines):
            for j in range(1, len(line) - 1):
                up, down, left, right = (True for _ in range(4))
                if i - 1 >= 0:
                    if lines[i - 1][j] == "_":
                        up = False

        for i in range(y_rooms):
            for row in range(x_rooms):
                left_index = row * 3
                right_index = (row * 3) + 3
                top_index = i * 2
                bottom_index = (i * 2) + 2
                topline = lines[top_index][left_index + 1 : right_index]
                bottomline = lines[bottom_index][left_index + 1 : right_index]
                leftline = lines[top_index + 1][left_index]
                rightline = lines[top_index + 1][right_index]
                if topline != "--":
                    if topline == "vv":
                        tiles[i][row].is_entrance = True
                        entrace_index = (i, row)
                    elif topline == "^^":
                        tiles[i][row].is_exit = True
                        exit_index = (i, row)
                    tiles[i][row].directions[0] = True
                if bottomline != "--":
                    if bottomline == "vv":
                        tiles[i][row].is_exit = True
                        exit_index = (i, row)
                    elif bottomline == "^^":
                        tiles[i][row].is_entrance = True
                        entrace_index = (i, row)
                    tiles[i][row].directions[2] = True
                if leftline != "|":
                    if leftline == ">":
                        tiles[i][row].is_entrance = True
                        entrace_index = (i, row)
                    elif leftline == "<":
                        tiles[i][row].is_exit = True
                        exit_index = (i, row)
                    tiles[i][row].directions[3] = True
                if rightline != "|":
                    if rightline == ">":
                        tiles[i][row].is_exit = True
                        exit_index = (i, row)
                    elif rightline == "<":
                        tiles[i][row].is_entrance = True
                        entrace_index = (i, row)
                    tiles[i][row].directions[1] = True

        for i, row in enumerate(tiles):
            for j, room in enumerate(row):
                if j == len(row) - 1:
                    room.directions[1] = False
                if j == 0:
                    room.directions[3] = False
                if i == len(tiles) - 1:
                    room.directions[2] = False
                if i == 0:
                    room.directions[0] = False


main()
