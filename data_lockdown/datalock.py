'''System module'''
import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    logLine = int(sys.stdin.readline().rstrip())
    for logLines in range(logLine):
        line = sys.stdin.readline().rstrip()
        website, dataSize = (str(val) for val in line.split(SEPARATOR))
        dataSize = int(dataSize)
        if dataSize > 1000:
            #if website[len(website)-10:len(website)-1] != ".lmco.com":
            if ".lmco.com" not in website:
                print(website, dataSize)
                