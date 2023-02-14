"""System Module"""
import sys


class Room:
    def __init__(self) -> None:
        self.directions: list[bool] = []
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
    print(x_rooms, y_rooms)
    for i in range(y_rooms):
        for j in range(x_rooms):
            if i % 2 == 0:
                left_x = j * 3
                right_x = (j * 3) + 3
                top = i
                bottom = i + 2
                print(lines[top][left_x + 1:right_x])
