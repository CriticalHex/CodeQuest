'''System Module'''
import sys
import copy
from numpy import Infinity

def get_key(val):
    '''inverse of getValue'''
    for key, value in MOVES.items():
        if val == value:
            return key

def available(board):
    '''Are there spaces to change?'''
    for i in range(3):
        for j in range(3):
            if board[i][j] == "*":
                return True
    return False

def possible(board, maximizingPlayer):
    '''Checks available moves'''
    board_states = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "*":
                board[i][j] = "X" if maximizingPlayer else "O"
                board_states.append(copy.deepcopy(board))
                board[i][j] = "*"
    return board_states

def game_over(board):
    '''Check if game is over'''
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[0][0] == "X":
                return 1
            if board[0][0] == "O":
                return -1
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][0] == "X":
                return 1
            if board[0][0] == "O":
                return -1
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "X":
            return 1
        if board[0][0] == "O":
            return -1
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == "X":
            return 1
        if board[0][2] == "O":
            return -1
    if not available(board):
        return 0

def minimax(position, depth, maximizingPlayer):
    '''Recursive function to determine best possible moves in a turn based game'''
    if depth == 0 or game_over(position) in (0,1,-1):
        return game_over(position)
    if maximizingPlayer:
        maxEval = -10000000
        for child in possible(position, True):
            eval = minimax(child, depth - 1, False)
            maxEval = max(maxEval, eval)
        return maxEval
    else:
        minEval = 10000000
        for child in possible(position, False):
            eval = minimax(child, depth - 1, True)
            minEval = min(minEval, eval)
        return minEval

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    BOARD = []
    MOVES = {}
    for _ in range(3):
        line = sys.stdin.readline().rstrip()
        BOARD.append(list(line))
    BOARD = possible(BOARD, True)
    for i in range(len(BOARD)):
        MOVES.update({i:minimax(BOARD[i], 9, False)})
    for i in range(3):
        for j in range(3):
            print(BOARD[get_key(max(MOVES.values()))][i][j], end="")
        print()
    