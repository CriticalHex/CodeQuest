"""System Module"""
import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    args = line.split(SEPARATOR)
    temp, water, surface, orbit = (
        float(args[0]),
        bool(args[1] == "true"),
        bool(args[2] == "true"),
        float(args[3]),
    )
    if temp > 100:
        print("The planet is too hot.")
    elif temp < 0:
        print("The planet is too cold.")
    elif not water:
        print("The planet has no water.")
    elif not surface:
        print("The planet has no magnetic field.")
    elif orbit > 0.6:
        print("The planet's orbit is not ideal.")
    else:
        print("The planet is habitable.")
