"""System Module"""
import sys

SEPARATOR = "|"
ALPHA = ["a","b","c","d","e","f","g","h","i","j","k","l",
"m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    val1, val2 = (list(val.lower()) for val in line.split(SEPARATOR))
    greeting: list[str] = []
    response: list[str] = []
    for c in val1:
        if c in ALPHA:
            greeting.append(c)
    for c in val2:
        if c in ALPHA:
            response.append(c)
    for c in response:
        if c not in greeting:
            print("You're not a secret agent!")
            break
    else:
        print("That's my secret contact!")
