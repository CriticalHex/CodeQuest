'''import libraries'''
import sys
import math

def get_key(val):
    '''inverse of getValue'''
    for key, value in ASTEROIDS.items():
        if val == value:
            return key

SEPARATOR = " "


cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    ASTEROIDS = {}
    DISTANCES = []
    line = sys.stdin.readline().rstrip()

    for coords in range(int(line)):
        line = sys.stdin.readline().rstrip()
        x, y = (int(val) for val in line.split(SEPARATOR))
        distance = math.sqrt(pow(x, 2) + pow(y, 2))
        DISTANCES.append(distance)
        ASTEROIDS.update({line : distance}) 
    DISTANCES.sort()
    for distance in DISTANCES:
        print(get_key(distance))
