'''System Module'''
import sys
import copy

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

def possible(board, maximizing_player):
    '''Checks available moves'''
    board_states = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == "*":
                board[i][j] = "X" if maximizing_player else "O"
                board_states.append(copy.deepcopy(board))
                board[i][j] = "*"
    return board_states

def game_over(board):
    '''Check if game is over'''
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == "X":
                return 1
            if board[i][0] == "O":
                return -1
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == "X":
                return 1
            if board[0][i] == "O":
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

def minimax(position, depth, alpha, beta, maximizing_player):
    '''Recursive function to determine best possible moves in a turn based game'''
    if depth == 0 or game_over(position) is not None:
        # print(np.matrix(position))
        # print(game_over(position))
        return game_over(position)
    if maximizing_player:
        max_eval = -10
        for child in possible(position, True):
            evaluation = minimax(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, evaluation)
            alpha = max(alpha, evaluation)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = 10
        for child in possible(position, False):
            evaluation = minimax(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, evaluation)
            beta = min(beta, evaluation)
            if beta <= alpha:
                break
        return min_eval

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    BOARD = []
    MOVES = {}
    DONE = False
    for _ in range(3):
        line = sys.stdin.readline().rstrip()
        BOARD.append(list(line))
    BOARD = possible(BOARD, True)
    for game in BOARD:
        if game_over(game) == 1:
            for i in range(3):
                for j in range(3):
                    print(game[i][j], end="")
                print()
            BOARD.clear()
            DONE = True
    if not DONE:
        LENGTH = len(BOARD)
        for i in range(LENGTH):
            MOVES.update({i:minimax(BOARD[i], 9, -10, 10, False)})
        for i in range(3):
            for j in range(3):
                print(BOARD[get_key(max(MOVES.values()))][i][j], end="")
            print()
    