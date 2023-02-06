"""System Module"""
import sys
import string

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    status = sys.stdin.readline().rstrip()
    cipher = sys.stdin.readline().rstrip()
    table: dict[str, str] = {}
    if status == "ENCRYPT":
        for i in range(26):
            table[string.ascii_lowercase[i]] = cipher[i]
    else:
        for i in range(26):
            table[cipher[i]] = string.ascii_lowercase[i]
    messages = int(sys.stdin.readline().rstrip())
    for _ in range(messages):
        message = sys.stdin.readline().rstrip()
        output: str = ""
        for c in message:
            if c.lower() in string.ascii_lowercase:
                if c.isupper():
                    output += table[c.lower()].upper()
                else:
                    output += table[c]
            else:
                output += c
        print(output)
