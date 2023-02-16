"""System Module"""
import sys

class Room:
    """Room"""
    def __init__(self) -> None:
        self.directions: list[bool] = [False for _ in range(4)]
        self.is_entrance = False
        self.is_exit = False
        self.distance: int | None = None

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
        for row in range(x_rooms):
            maze[i].append(Room())
    for i in range(c_height):
        lines.append(sys.stdin.readline().rstrip())
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
                    maze[i][row].is_entrance = True
                    entrace_index = (i, row)
                elif topline == "^^":
                    maze[i][row].is_exit = True
                    exit_index = (i, row)
                maze[i][row].directions[0] = True
            if bottomline != "--":
                if bottomline == "vv":
                    maze[i][row].is_exit = True
                    exit_index = (i, row)
                elif bottomline == "^^":
                    maze[i][row].is_entrance = True
                    entrace_index = (i, row)
                maze[i][row].directions[2] = True
            if leftline != "|":
                if leftline == ">":
                    maze[i][row].is_entrance = True
                    entrace_index = (i, row)
                elif leftline == "<":
                    maze[i][row].is_exit = True
                    exit_index = (i, row)
                maze[i][row].directions[3] = True
            if rightline != "|":
                if rightline == ">":
                    maze[i][row].is_exit = True
                    exit_index = (i, row)
                elif rightline == "<":
                    maze[i][row].is_entrance = True
                    entrace_index = (i, row)
                maze[i][row].directions[1] = True

    for i, row in enumerate(maze):
        for j, room in enumerate(row):
            if j == len(row) - 1:
                room.directions[1] = False
            if j == 0:
                room.directions[3] = False
            if i == len(maze) - 1:
                room.directions[2] = False
            if i == 0:
                room.directions[0] = False

    ################################### Actually solve the maze ###################################

    for i in maze:
        for row in i:
            if row.is_entrance:
                row.distance = 1

    finished: bool = False
    while not finished:
        finished: bool = True

        for i, row in enumerate(maze):
            for j, room in enumerate(row):
                if room.distance is None:
                    distances: list[int] = []

                    if room.directions[0]:
                        if maze[i - 1][j].distance is not None:
                            distances.append(maze[i - 1][j].distance) #type: ignore
                    if room.directions[1]:
                        if row[j + 1].distance is not None:
                            distances.append(row[j + 1].distance) #type: ignore
                    if room.directions[2]:
                        if maze[i + 1][j].distance is not None:
                            distances.append(maze[i + 1][j].distance) #type: ignore
                    if room.directions[3]:
                        if row[j - 1].distance is not None:
                            distances.append(row[j - 1].distance) #type: ignore

                    if distances:
                        room.distance = min(distances) + 1
                        finished: bool = False

    for i in maze:
        for row in i:
            if row.is_exit:
                print(row.distance)

    # for i in maze:
    #     for j in i:
    #         print(j.directions, end = " ")
    #     print()

        #loop through the thing
