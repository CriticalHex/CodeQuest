"""System Module"""
import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    num_all_systems, num_good_systems = (int(val) for val in line.split(SEPARATOR))
    all_systems: list[str] = []
    good_systems: list[str] = []
    for i in range(num_all_systems):
        all_systems.append(sys.stdin.readline().rstrip())
    for i in range(num_good_systems):
        good_systems.append(sys.stdin.readline().rstrip())
    all_systems.sort(key=lambda s: s.lower())
    good_systems.sort(key=lambda s: s.lower())
    for s in all_systems:
        if s not in good_systems:
            print(s)
