'''import libraries'''
import sys
import math

def zodiac(year):
    '''Gets your zodiac information'''
    element = [" Wood", " Fire", " Earth", " Metal", " Water"]
    animal = [ " Rat", " Ox", " Tiger", " Rabbit", " Dragon", " Snake",
              " Horse", " Goat", " Monkey", " Rooster", " Dog", " Pig"]
    output = str(year)
    if year % 2 == 0:
        output += " Yang"
    else:
        output += " Yin"
    year -= 4
    output += element[math.floor((year%10)/2)]
    output += animal[year % 12]
    return output
SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    Y = int(sys.stdin.readline().rstrip())
    print(zodiac(Y))
    