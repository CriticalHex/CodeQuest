"""System Module"""
import sys


class Node:
    """Graph nodes"""

    def __init__(self, value: int) -> None:
        self.value = value
        self.score: int = 0


def get_line() -> str:
    """Get rstripped stdin line"""
    return sys.stdin.readline().rstrip()


def list_to_string(lis: list[str]) -> str:
    """A list of str to str"""
    string: str = ""
    for char in lis:
        string += char
    return string


def get_path(board: list[list[Node]], index: int):
    """get path"""
    path: list[str] = []
    peg = index
    for row in range(-1, -(len(board)), -1):
        if peg == 0:
            path.append("L")
        elif peg == len(board[row]) - 1:
            path.append("R")
            peg -= 1
        else:
            choices = (board[row - 1][peg - 1], board[row - 1][peg])
            if choices[0].score > choices[1].score:
                path.append("R")
                peg -= 1
            else:
                path.append("L")
    path.reverse()
    return list_to_string(path)


def plink(board: list[list[Node]]):
    """Plink it"""
    board[0][0].score = board[0][0].value
    for i in range(1, len(board)):
        for j, peg in enumerate(board[i]):
            if j == 0:
                peg.score = board[i - 1][j].score + peg.value
            elif j == len(board[i]) - 1:
                peg.score = board[i - 1][j - 1].score + peg.value
            else:
                choices = (board[i - 1][j - 1], board[i - 1][j])
                if choices[0].score > choices[1].score:
                    peg.score = choices[0].score + peg.value
                else:
                    peg.score = choices[1].score + peg.value
    best_node = max(board[-1], key=lambda node: node.score)
    index = 0
    for i, node in enumerate(board[-1]):
        if node is best_node:
            break
        index += 1
    print(f"{get_path(board, index)} = {best_node.score}")


def main():
    """Main"""
    cases = int(get_line())
    for _ in range(cases):
        board: list[list[Node]] = []
        rows = int(get_line())
        for row in range(rows + 1):
            line = get_line()
            board.append([])
            for val in line.split(" "):
                board[row].append(Node(int(val)))
        plink(board)


if __name__ == "__main__":
    main()
