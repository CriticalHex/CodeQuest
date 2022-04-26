'''System Module'''
import sys
import numpy as np

class Piece:
    '''All the chess pieces hopefully'''
    def __init__(self, index_x: int, index_y: int, team: str):
        self.x = index_y
        self.y = index_y
        self.team = team
        self.available_moves = []
        self.available_captures = []

class King(Piece):
    '''The king'''
    def get_available_moves(self, board):
        '''Creates a list of all moves available to this piece'''
        for i in range(-1,2):
            for j in range(-1,2):
                if board[i][j] == ".":
                    self.available_moves.append(self.y - i, self.x - j)
                    #need vector for all piece options.
                    #need to consider piece checking order
                    #all pieces except king? pretty sure this has flaws, don't know what yet
                    #i thought the check all of one side would work, i dont think it does.
                    #imma watch sebastian lauges video on this



SEPARATOR = " "
ALPHA = ["a","b","c","d","e","f","g","h","i","j","k","l",
"m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
CAPALPHA = ["A","B","C","D","E","F","G","H","I","J","K","L",
"M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    board = []
    for i in range(8):
        line = sys.stdin.readline().rstrip()
        board.append(list(line))
    print(np.matrix(board))
    print()
    