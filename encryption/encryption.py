"""System Module"""
import sys

SEPARATOR = " "
ALPHA = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
CAPALPHA = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    status = sys.stdin.readline().rstrip()
    cipher = sys.stdin.readline().rstrip()
    table: dict[str, str] = {}
    if status == "ENCRYPT":
        for i in range(26):
            table[ALPHA[i]] = cipher[i]
    else:
        for i in range(26):
            table[cipher[i]] = ALPHA[i]
    messages = int(sys.stdin.readline().rstrip())
    for _ in range(messages):
        message = sys.stdin.readline().rstrip()
        output: str = ""
        for c in message:
            if c.lower() in ALPHA:
                if c.isupper():
                    output += table[c.lower()].upper()
                else:
                    output += table[c]
            else:
                output += c
        print(output)
