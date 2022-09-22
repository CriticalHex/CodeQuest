'''System Module'''
import sys

SEPARATOR = " "
results = {}

def get_key(val):
    '''inverse of getValue'''
    for key, value in results.items():
        if val == value:
            return key
        
def norec(B):
    stack = []
    i = 0
    j = 0
    path = ""
    total = 0
    while True:
        if i >= len(B) - 1:
            results[path] = total + B[i][j]
        else:
            stack.append([i + 1, j, path + "L", total + B[i][j]])
            stack.append([i + 1, j + 1, path + "R", total + B[i][j]])

def plinko(B, i = 0, j = 0, path = "", total = 0):
    '''Recursive function to determine best plinko path in a given board'''
    if i >= len(B) - 1:
        results[path] = total + B[i][j]
    else:
        plinko(B, i + 1, j, path + "L", total + B[i][j])
        plinko(B, i + 1, j + 1, path + "R", total + B[i][j])
    
cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    board = []
    rows = int(sys.stdin.readline().rstrip())
    for r in range(rows + 1):
        line = sys.stdin.readline().rstrip()
        board.append([])
        for val in line.split(SEPARATOR):
            board[r].append(int(val))
    plinko(board)
    largest = max(results.values())
    print(get_key(largest), "=", largest)
    results = {}
    