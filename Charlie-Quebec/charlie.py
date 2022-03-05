'''System module'''
import sys

SEPARATOR = " "

NATO = {"A": "Alpha", "B":"Bravo", "C":"Charlie", "D":"Delta",
        "E":"Echo", "F":"Foxtrot", "G":"Golf", "H":"Hotel",
        "I":"India", "J":"Juliet", "K":"Kilo", "L":"Lima",
        "M":"Mike", "N":"November", "O":"Oscar", "P":"Papa",
        "Q":"Quebec", "R":"Romeo", "S":"Sierra", "T":"Tango",
        "U":"Uniform", "V":"Victor", "W":"Whiskey", "X":"Xray",
        "Y":"Yankee", "Z":"Zulu"}

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    subCases = int(sys.stdin.readline().rstrip())
    for subCase in range(subCases):
        OUTPUT_STRING = ""
        line = sys.stdin.readline().rstrip()
        line = line.upper()
        for i in range(len(line)-1):
            if line[i] != " " and line[i+1] != " ":
                OUTPUT_STRING += NATO.get(line[i])
                OUTPUT_STRING += "-"
            elif line[i] != " ":
                OUTPUT_STRING += NATO.get(line[i])
            else:
                OUTPUT_STRING += " "
        OUTPUT_STRING += NATO.get(line[len(line)-1])
        print(OUTPUT_STRING)
        