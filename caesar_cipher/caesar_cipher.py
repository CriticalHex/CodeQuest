"""System Module"""
import sys
import string


def main():
    alphabet = list(string.ascii_lowercase)
    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        shift = int(sys.stdin.readline().rstrip())
        line = sys.stdin.readline().rstrip()
        output = ""
        for c in line:
            if c == " ":
                output += " "
            else:
                index = alphabet.index(c) - (shift % 26)
                output += alphabet[index]
        print(output)


main()
