import sys
import math

def Zodiac(year):
    Element = [" Wood", " Fire", " Earth", " Metal", " Water"]
    Animal = [ " Rat", " Ox", " Tiger", " Rabbit", " Dragon", " Snake", " Horse", " Goat", " Monkey", " Rooster", " Dog", " Pig"]
    output = str(year)
    if year % 2 == 0:
        output += " Yang"
    else:
        output += " Yin"
    year -= 4
    output += Element[math.floor((year%10)/2)]
    output += Animal[year % 12]
    return output
SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    year = int(sys.stdin.readline().rstrip())
    
    print(Zodiac(year))
    