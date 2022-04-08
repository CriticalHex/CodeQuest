'''System Module'''
import sys
import math

def round_half_up(original):
    '''Better Rounding WHY DOES PYTHON SUCK'''
    multiplied = original * 100.0
    floored = math.floor(multiplied)
    remainder = multiplied - floored
    if remainder >= 0.5:
        floored += 1
    rounded = str(floored / 100.0)
    while len(rounded) - rounded.index('.') < 3:
        rounded += '0'
    return rounded

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    door_number, rounds, doors_per_round = (int(val) for val in line.split(SEPARATOR))
    START = 0
    doors = [0] * door_number
    chance = 100 / door_number
    for i in range(START, door_number):
        doors[i] = chance
    for i in range(rounds):
        REDIST = 0
        #contestant picks door
        START += 1
        for j in range(doors_per_round):
            REDIST += doors.pop()
        REDIST /= len(doors) - START
        for j in range(START, len(doors)):
            doors[j] += REDIST
    print(str(round_half_up(doors[START])) + "%")
    