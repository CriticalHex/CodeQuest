import sys

SEPARATOR = " "

NATO = {"A": "Alpha", "B":"Bravo", "C":"Charlie", "D":"Delta",
        "E":"Echo", "F":"Foxtrot", "G":"Golf", "H":"Hotel",
        "I":"India", "J":"Juliet", "K":"Kilo", "L":"Lima",
        "M":"Mike", "N":"November", "O":"Oscar", "P":"Papa",
        "Q":"Quebec", "R":"Romero", "S":"Sierra", "T":"Tango",
        "U":"Uniform", "V":"Victor", "W":"Whiskey", "X":"Xray",
        "Y":"Yankee", "Z":"Zulu"}

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    subCases = int(sys.stdin.readline().rstrip())
    for subCase in range(subCases):
        outputString = ""
        line = sys.stdin.readline().rstrip()
        line = line.upper()
        
        for i in range(len(line)):
            if line[i] != " ":
                outputString += NATO.get(line[i])
                
                outputString += "-"
            else:
                outputString += " "
        print(outputString)