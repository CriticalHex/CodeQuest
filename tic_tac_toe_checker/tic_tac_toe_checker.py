'''System Module'''
import sys

def game_over(game):
    '''Checks if a game is over'''
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2]:
            if game[i][0] == "X":
                return "X WINS"
            if game[i][0] == "O":
                return "O WINS"
    for i in range(3):
        if game[0][i] == game[1][i] == game[2][i]:
            if game[0][i] == "X":
                return "X WINS"
            if game[0][i] == "O":
                return "O WINS"
    if game[0][0] == game[1][1] == game[2][2]:
        if game[0][0] == "X":
            return "X WINS"
        if game[0][0] == "O":
            return "O WINS"
    if game[0][2] == game[1][1] == game[2][0]:
        if game[0][2] == "X":
            return "X WINS"
        if game[0][2] == "O":
            return "O WINS"
    return "TIE"

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    board = []
    line = sys.stdin.readline().rstrip()
    temp = list(line)
    for i in range(3):
        board.append([])
        for j in range(3):
            board[i].append(temp[j+(i*3)])
    print(line, "=", game_over(board))
    