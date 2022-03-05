'''System module'''
import sys

color_theory = {
"green":("blue","yellow"), "yellow-green":("blue","yellow"), "blue-green":("blue","yellow"),
"orange":("red","yellow"), "red-orange":("red","yellow"), "yellow-orange":("red","yellow"),
"violet":("blue","red"), "red-violet":("blue","red"), "blue-violet":("blue","red")}

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    LINE = str(sys.stdin.readline().rstrip())
    if LINE == "red" or LINE == "yellow" or LINE == "blue":
        print(f"No colors need to be mixed to make {LINE}.")
    else:
        print(f"In order to make {LINE}, {color_theory.get(LINE)[0]} and {color_theory.get(LINE)[1]} must be mixed.")
        