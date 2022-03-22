'''Solves Sudoku Puzzles'''
from os import system
import sys
import numpy as np

def board_setup():
    '''Create the board'''
    global BOARD
    BOARD = []
    for i in range(9):
        line = sys.stdin.readline().rstrip()
        BOARD.append(list(line))
        for j in range(9):
            if BOARD[i][j] != "_":
                BOARD[i][j] = int(BOARD[i][j])
            else:
                BOARD[i][j] = 0

def possible(y, x, n):
    '''Can a number go in a postion'''
    for i in range(9):
        if BOARD[y][i] == n:
            return False
    for i in range(9):
        if BOARD[i][x] == n:
            return False
    subgrid_X = (x//3)*3
    subgrid_Y = (y//3)*3
    for i in range(3):
        for j in range(3):
            if BOARD[subgrid_Y + i][subgrid_X + j] == n:
                return False
    return True

def solve():
    '''Recursive function to test values in the grid'''
    for i in range(9):
        for j in range(9):
            if BOARD[i][j] == 0:
                for k in range(1,10):
                    if possible(i,j,k):
                        BOARD[i][j] = k
                        solve()
                        system("CLS")
                        print(np.matrix(BOARD))
                        print()
                        BOARD[i][j] = 0
                return
    for i in range(9):
        for j in range(9):
            print(BOARD[i][j], end="")
        print()

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    board_setup()
    solve()
