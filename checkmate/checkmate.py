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

    def prune_edges(self):
        new_moves: list[tuple[int, int]] = []
        for move in self.possible_moves:
            if move[0] > 7 or move[0] < 0 or move[1] > 7 or move[1] < 0:
                continue
            new_moves.append(move)
        self.possible_moves = new_moves


def get_piece(at_pos: tuple[int, int], board: list[Piece]):
    for piece in board:
        if piece.pos == at_pos:
            return piece


class Pawn(Piece):
    """The Pawn"""

    def __init__(self, x: int, y: int, piece: str):
        super().__init__(x, y, piece)
        self.at_home = False
        if self.team == "BLACK":
            move_dir = 1
            if self.pos[1] == 1:
                self.at_home = True
        else:
            move_dir = -1
            if self.pos[1] == 6:
                self.at_home = True
        self.possible_moves = [
            (x, y + move_dir),
            (x, y + (2 * move_dir)),
        ]
        self.attack_moves = [
            (x + 1, y + move_dir),
            (x - 1, y + move_dir),
        ]
        self.prune_edges()

    def get_available_moves(self, board: list["Piece"]):
        piece_pos = [piece.pos for piece in board]
        if self.possible_moves[0] not in piece_pos:
            self.available_moves.append(self.possible_moves[0])
            if self.at_home and self.possible_moves[1] not in piece_pos:
                self.available_moves.append(self.possible_moves[1])
        for pos in self.attack_moves:
            for piece in board:
                if piece.pos == pos:
                    if piece.team == self.team:
                        continue
                    self.available_captures.append(piece)
                    self.available_moves.append(pos)


class Rook(Piece):
    """The Rook"""

    def __init__(self, x: int, y: int, piece: str):
        super().__init__(x, y, piece)
        left_line: list[tuple[int, int]] = []
        right_line: list[tuple[int, int]] = []
        up_line: list[tuple[int, int]] = []
        down_line: list[tuple[int, int]] = []
        for i in range(x, 8):
            right_line.append((x + i, y))
        for i in range(x, -1, -1):
            left_line.append((x + i, y))
        for i in range(y, 8):
            down_line.append((x, y + i))
        for i in range(y, -1, -1):
            up_line.append((x, y + i))
        self.lines = [left_line, right_line, up_line, down_line]

    def get_available_moves(self, board: list["Piece"]):
        for line in self.lines:
            index = len(line)
            for i, pos in enumerate(line):
                if piece := get_piece(pos, board):
                    index = i
                    if piece.team != self.team:
                        self.available_captures.append(piece)
                        self.available_moves.append(pos)
                    break
            self.available_moves.extend(line[0:index])


class Bishop(Piece):
    """The Bishop"""

    def __init__(self, x: int, y: int, piece: str):
        super().__init__(x, y, piece)
        left_up_line: list[tuple[int, int]] = []
        right_up_line: list[tuple[int, int]] = []
        left_down_line: list[tuple[int, int]] = []
        right_down_line: list[tuple[int, int]] = []
        for i in range(x, 8):
            right_up_line.append((x + i, y - i))
        for i in range(x, -1, -1):
            left_up_line.append((x - i, y - i))
        for i in range(y, 8):
            right_down_line.append((x + i, y + i))
        for i in range(y, -1, -1):
            left_down_line.append((x - i, y + i))
        self.lines = [left_up_line, right_up_line, left_down_line, right_down_line]

    def get_available_moves(self, board: list["Piece"]):
        for line in self.lines:
            index = len(line)
            for i, pos in enumerate(line):
                if piece := get_piece(pos, board):
                    index = i
                    if piece.team != self.team:
                        self.available_captures.append(piece)
                        self.available_moves.append(pos)
                    break
            self.available_moves.extend(line[0:index])


class Queen(Piece):
    """The Queen"""

    def __init__(self, x: int, y: int, piece: str):
        super().__init__(x, y, piece)
        left_up_line: list[tuple[int, int]] = []
        right_up_line: list[tuple[int, int]] = []
        left_down_line: list[tuple[int, int]] = []
        right_down_line: list[tuple[int, int]] = []
        left_line: list[tuple[int, int]] = []
        right_line: list[tuple[int, int]] = []
        up_line: list[tuple[int, int]] = []
        down_line: list[tuple[int, int]] = []
        for i in range(x, 8):
            right_line.append((x + i, y))
        for i in range(x, -1, -1):
            left_line.append((x + i, y))
        for i in range(y, 8):
            down_line.append((x, y + i))
        for i in range(y, -1, -1):
            up_line.append((x, y + i))
        for i in range(x, 8):
            right_up_line.append((x + i, y - i))
        for i in range(x, -1, -1):
            left_up_line.append((x - i, y - i))
        for i in range(y, 8):
            right_down_line.append((x + i, y + i))
        for i in range(y, -1, -1):
            left_down_line.append((x - i, y + i))
        self.lines = [
            left_line,
            right_line,
            up_line,
            down_line,
            left_up_line,
            right_up_line,
            left_down_line,
            right_down_line,
        ]

    def get_available_moves(self, board: list["Piece"]):
        for line in self.lines:
            index = len(line)
            for i, pos in enumerate(line):
                if piece := get_piece(pos, board):
                    index = i
                    if piece.team != self.team:
                        self.available_captures.append(piece)
                        self.available_moves.append(pos)
                    break
            self.available_moves.extend(line[0:index])


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
        self.prune_edges()

    def get_available_moves(self, board: list["Piece"]):
        for pos in self.possible_moves:
            for piece in board:
                if piece.pos == pos:
                    if piece.team == self.team:
                        continue
                    self.available_captures.append(piece)
                if pos not in self.available_moves:
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
        self.prune_edges()

    def get_available_moves(self, board: list["Piece"]):
        """More like attempt escape"""
        for pos in self.possible_moves:
            if piece := get_piece(pos, board):
                if piece.pos == pos:
                    if piece.team == self.team:
                        continue
                    self.available_captures.append(piece)
                    self.available_moves.append(pos)
            if pos not in self.available_moves:
                self.available_moves.append(pos)


def find_check(board: list[Piece]):
    for piece in board:
        if piece.piece.lower() == "k":
            for other in board:
                if other is not piece:
                    if piece.pos in other.available_moves:
                        return piece


def is_checkmate(check: Piece, board: list[Piece]):
    escapes: list[tuple[int,int]] = []
    for other in board:
        if other is not check:
            for move in check.available_moves:
                if move in other.available_moves:
                    continue
                


def get_type(c: str):
    if c.lower() == "k":
        return King
    elif c.lower() == "q":
        return Queen
    elif c.lower() == "r":
        return Rook
    elif c.lower() == "b":
        return Bishop
    elif c.lower() == "n":
        return Knight
    elif c.lower() == "p":
        return Pawn
    else:
        # should not happen
        print("ERROR")
        return Piece


def main():

    cases = int(sys.stdin.readline().rstrip())

    for _ in range(cases):
        board: list[Piece] = []
        for y in range(8):
            line = sys.stdin.readline().rstrip()
            for x, c in enumerate(line):
                if c != ".":
                    board.append(get_type(c)(x, y, c))
        for piece in board:
            piece.get_available_moves(board)
        if check := find_check(board):
            print(check.piece)
            if is_checkmate(check, board):
                winner = "WHITE" if check.team == "BLACK" else "WHITE"
                print(f"CHECKMATE {winner}")
            else:
                print("NO CHECKMATE")
        else:
            print("NO CHECKMATE")


main()
