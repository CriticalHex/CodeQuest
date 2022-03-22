'''System Module'''
import sys
import numpy as np

def available(board):
    '''Checks available moves'''
    player = 1
    board_states = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != "*":
                board[i][j] = "X" if player == 1 else "O"
                board_states.append(board)


def game_over(board):
    '''Check if game is over'''
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == "X":
                return 1
            else:
                return -1
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == "X":
            return 1
        else:
            return -1
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][0] == "X":
            return 1
        else:
            return -1
    if len(available(board)) == 0:
        return 0

def minimax(position, depth, alpha, beta, maximizingPlayer):
    '''Recursive function to determine best possible moves in a turn based game'''
    if depth == 0 or game_over(position) in (0,1,-1):
        return game_over(position)
    if maximizingPlayer:
        maxEval = -np.Infinity
        for child in position:
            eval = minimax(child, depth - 1, alpha, beta, False)
            maxEval = max(maxEval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval
    else:
        minEval = np.Infinity
        for child in position:
            eval = minimax(child, depth - 1, alpha, beta, False)
            minEval = min(minEval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval
cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    BOARD = []
    for _ in range(3):
        line = sys.stdin.readline().rstrip()
        BOARD.append(list(line))
    minimax(BOARD, 9, -np.Infinity, np.Infinity, True)
    print(np.matrix(BOARD))
    