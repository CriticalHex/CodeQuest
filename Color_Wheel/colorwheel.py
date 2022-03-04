import sys

ColorTheory = {"green":("blue","yellow"), "yellow-green":("blue","yellow"), "blue-green":("blue","yellow"),
                "orange":("red","yellow"), "red-orange":("red","yellow"), "yellow-orange":("red","yellow"),
              "violet":("blue","red"), "red-violet":("blue","red"), "blue-violet":("blue","red")}

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = str(sys.stdin.readline().rstrip())
    
    if line == "red" or line == "yellow" or line == "blue":
        print(f"No colors need to be mixed to make {line}.")
    else:
        print(f"In order to make {line}, {ColorTheory.get(line)[0]} and {ColorTheory.get(line)[1]} must be mixed.")