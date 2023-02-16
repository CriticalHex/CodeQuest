"""System Module"""
import sys


class Piece:
    """All the chess pieces hopefully"""

    def __init__(self, x: int, y: int, piece: str):
        self.pos = (x, y)
        self.piece = piece
        self.team = "WHITE" if piece.isupper() else "BLACK"
        self.available_moves: list[tuple[int, int]] = []
        self.available_captures: list[Piece] = []
        self.possible_moves: list[tuple[int, int]] = []

    def get_available_moves(self, board: list["Piece"]):
        """Creates a list of all moves available to this piece"""


class Knight(Piece):
    """The Knight"""

    def __init__(self, x: int, y: int, piece: str):
        super().__init__(x, y, piece)
        self.possible_moves = [
            (x + 1, y - 2),
            (x + 2, y - 1),
            (x + 2, y + 1),
            (x + 1, y + 2),
            (x - 1, y + 2),
            (x - 2, y - 1),
            (x - 2, y + 1),
            (x - 1, y + 2),
        ]

    def get_available_moves(self, board: list["Piece"]):
        for pos in self.possible_moves:
            for piece in board:
                if piece.pos == pos:
                    if piece.team == self.team:
                        continue
                    self.available_captures.append(piece)
                self.available_moves.append(pos)


class King(Piece):
    """The king"""

    def __init__(self, x: int, y: int, piece: str):
        super().__init__(x, y, piece)
        self.possible_moves = [
            (x + 1, y),
            (x - 1, y),
            (x + 1, y + 1),
            (x - 1, y + 1),
            (x + 1, y - 1),
            (x - 1, y - 1),
            (x, y - 1),
            (x, y + 1),
        ]

    def get_available_moves(self, board: list["Piece"]):
        """More like attempt escape"""
        for pos in self.possible_moves:
            for piece in board:
                if piece.pos == pos:
                    if piece.team == self.team:
                        continue
                    self.available_captures.append(piece)
                self.available_moves.append(pos)


def main():

    cases = int(sys.stdin.readline().rstrip())

    for _ in range(cases):
        board: list[Piece] = []
        for y in range(8):
            line = sys.stdin.readline().rstrip()
            for x, c in enumerate(line):
                if c != ".":
                    board.append(Piece(x, y, c))
        for piece in board:
            print(piece.piece)


main()
