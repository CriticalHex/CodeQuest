'''System Module'''
import sys

ALPHABET = {"A":0, "B":1, "C":2, "D":3,
        "E":4, "F":5, "G":6, "H":7,
        "I":8, "J":9, "K":10, "L":11,
        "M":12, "N":13, "O":14, "P":15,
        "Q":16, "R":17, "S":18, "T":19,
        "U":20, "V":21, "W":22, "X":23,
        "Y":24, "Z":25}
CODEARRAY = ["a","b","c","d","e","f","g","h","i","j","k","l",
"m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
CA = ["A","B","C","D","E","F","G","H","I","J","K","L",
"M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    ENCODE = sys.stdin.readline().rstrip()
    LOOPS = len(ENCODE)
    line = str(sys.stdin.readline().rstrip()).replace(" ", "")
    DISTANCE = [int(i) for i in line]
    DISTANCE_LEN = len(DISTANCE)
    line = str(sys.stdin.readline().rstrip()).replace(" ", "")
    DIRECTION = [int(i) for i in line]
    DIRECTION_LEN = len(DIRECTION)
    OUTPUT = ""
    OTHER_I = 0
    for i in range(LOOPS):
        if ENCODE[i] in CA:
            if DIRECTION[OTHER_I % DIRECTION_LEN] == 0:
                OUTPUT += CODEARRAY[(ALPHABET.get(ENCODE[i]) + DISTANCE[OTHER_I % DISTANCE_LEN]) % 26]
            elif DIRECTION[OTHER_I % DIRECTION_LEN] == 1:
                OUTPUT += CODEARRAY[(ALPHABET.get(ENCODE[i]) - DISTANCE[OTHER_I % DISTANCE_LEN]) % 26]
            OTHER_I += 1
        else:
            OUTPUT += ENCODE[i]
    print(OUTPUT)
