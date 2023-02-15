"""System Module"""
import sys


class Room:
    def __init__(self) -> None:
        self.directions: list[bool] = [False for _ in range(4)]
        self.is_entrance = False
        self.is_exit = False


SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    c_height, c_width = (int(val) for val in line.split(SEPARATOR))
    x_rooms = (c_width - 1) // 3
    y_rooms = (c_height - 1) // 2
    lines: list[str] = []
    maze: list[list[Room]] = []
    for i in range(y_rooms):
        maze.append([])
        for j in range(x_rooms):
            maze[i].append(Room())
    for i in range(c_height):
        lines.append(sys.stdin.readline().rstrip())
    for i in range(y_rooms):
        for j in range(x_rooms):
            left_index = j * 3
            right_index = (j * 3) + 3
            top_index = i * 2
            bottom_index = (i * 2) + 2
            topline = lines[top_index][left_index + 1 : right_index]
            bottomline = lines[bottom_index][left_index + 1 : right_index]
            leftline = lines[top_index + 1][left_index]
            rightline = lines[top_index + 1][right_index]
            if topline != "--":
                if topline == "vv":
                    maze[i][j].is_entrance = True
                    entrace_index = (i, j)
                elif topline == "^^":
                    maze[i][j].is_exit = True
                    exit_index = (i, j)
                maze[i][j].directions[0] = True
            if bottomline != "--":
                if bottomline == "vv":
                    maze[i][j].is_exit = True
                    exit_index = (i, j)
                elif bottomline == "^^":
                    maze[i][j].is_entrance = True
                    entrace_index = (i, j)
                maze[i][j].directions[2] = True
            if leftline != "|":
                if leftline == ">":
                    maze[i][j].is_entrance = True
                    entrace_index = (i, j)
                elif leftline == "<":
                    maze[i][j].is_exit = True
                    exit_index = (i, j)
                maze[i][j].directions[3] = True
            if rightline != "|":
                if rightline == ">":
                    maze[i][j].is_exit = True
                    exit_index = (i, j)
                elif rightline == "<":
                    maze[i][j].is_entrance = True
                    entrace_index = (i, j)
                maze[i][j].directions[1] = True
