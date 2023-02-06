"""System Module"""
import sys

SEPARATOR = " "

text = ["off", "red", "green", "blue"]

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    battery, heat, water, temp = (val for val in line.split(SEPARATOR))
    battery = 0 if battery == "WORKING" else 8
    heat = 0 if heat == "WORKING" else 4
    water = 0 if water == "WORKING" else 2
    temp = 0 if temp == "WORKING" else 1
    code = battery + heat + water + temp
    print(text[code // 4], text[code % 4])
