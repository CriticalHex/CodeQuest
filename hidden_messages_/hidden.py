'''System Module'''
import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())
ALPHABET = sys.stdin.readline().rstrip()
for caseNum in range(cases - 1):
    line = sys.stdin.readline().rstrip()
    OUTPUT = ""
    NUM = ""
    i = 0
    for letter in line:
        i += 1
        if letter == " ":
            NUM = int(NUM)
            OUTPUT += ALPHABET[NUM - 1]
            NUM = str("")
            OUTPUT += " "
        else:
            if i == len(line):
                NUM += letter
                NUM = int(NUM)
                OUTPUT += ALPHABET[NUM - 1]
                NUM = str("")
            if letter != "-":
                NUM += letter
            else:
                NUM = int(NUM)
                OUTPUT += ALPHABET[NUM - 1]
                NUM = str("")
    print(OUTPUT)
    