"""System module"""
import sys
import string

SEPARATOR = " "

NATO = {
    "A": "Alpha",
    "B": "Bravo",
    "C": "Charlie",
    "D": "Delta",
    "E": "Echo",
    "F": "Foxtrot",
    "G": "Golf",
    "H": "Hotel",
    "I": "India",
    "J": "Juliet",
    "K": "Kilo",
    "L": "Lima",
    "M": "Mike",
    "N": "November",
    "O": "Oscar",
    "P": "Papa",
    "Q": "Quebec",
    "R": "Romeo",
    "S": "Sierra",
    "T": "Tango",
    "U": "Uniform",
    "V": "Victor",
    "W": "Whiskey",
    "X": "Xray",
    "Y": "Yankee",
    "Z": "Zulu",
}

cases = int(sys.stdin.readline().rstrip())

for _ in range(cases):
    sub_cases = int(sys.stdin.readline().rstrip())
    for _ in range(sub_cases):
        output = ""
        line = sys.stdin.readline().rstrip().upper()
        for i in range(len(line) - 1):
            if line[i] in string.ascii_uppercase:
                output += NATO[line[i]]
                output += "-" if line[i + 1] in string.ascii_uppercase else line[i + 1]
        output += NATO[line[-1]]
        print(output)
