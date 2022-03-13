'''System Module'''
import sys

ALPHABET = {"A":0, "B":1, "C":2, "D":3,
        "E":4, "F":5, "G":6, "H":7,
        "I":8, "J":9, "K":10, "L":11,
        "M":12, "N":13, "O":14, "P":15,
        "Q":16, "R":17, "S":18, "T":19,
        "U":20, "V":21, "W":22, "X":23,
        "Y":24, "Z":25}
ALPHA = ["A","B","C","D","E","F","G","H","I","J","K","L",
"M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
CODEARRAY = ["A","B","C","D","E","F","G","H","I","J","K","L",
"M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    ENCODE = sys.stdin.readline().rstrip()
    LOOPS = len(ENCODE)
    CODE = sys.stdin.readline().rstrip()
    CODE_LEN = len(CODE)
    OUTPUT = ""
    OTHER_I = 0
    for i in range(LOOPS):
        if ENCODE[i] != " ":
            for j in range(ALPHABET.get(CODE[OTHER_I % CODE_LEN])):
                CODEARRAY.append(CODEARRAY.pop(0))
            OUTPUT += CODEARRAY[ALPHABET.get(ENCODE[i])]
            CODEARRAY = ["A","B","C","D","E","F","G","H","I","J","K","L",
                "M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
            OTHER_I += 1
        else:
            OUTPUT += " "
    print(OUTPUT)
