'''System Module'''
import sys

SEPARATOR = " "
ALPHA = ["a","b","c","d","e","f","g","h","i","j","k","l",
"m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
CAPALPHA = ["A","B","C","D","E","F","G","H","I","J","K","L",
"M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    TABLE = {}
    if line == "ENCRYPT":
        line = sys.stdin.readline().rstrip()
        for i in range(len(ALPHA)):
            TABLE.update({ALPHA[i]:line[i]})
    else:
        line = sys.stdin.readline().rstrip()
        for i in range(len(ALPHA)):
            TABLE.update({line[i]:ALPHA[i]})
    subCases = int(sys.stdin.readline().rstrip())
    for _ in range(subCases):
        OUTPUT = ""
        line = sys.stdin.readline().rstrip()
        for letter in line:
            if letter in CAPALPHA:
                OUTPUT += TABLE.get(letter.lower()).capitalize()
            else:
                if letter == " ":
                    OUTPUT += " "
                else:
                    OUTPUT += TABLE.get(letter)
        print(OUTPUT)
    