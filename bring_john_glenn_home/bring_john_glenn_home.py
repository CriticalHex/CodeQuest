'''System Module'''
import sys
from math import sin, floor

SEPARATOR = " "

def round_half_up(original):
    '''Better Rounding WHY DOES PYTHON SUCK'''
    multiplied = original * 1000.0
    floored = floor(multiplied)
    remainder = multiplied - floored
    if remainder >= .5:
        floored += 1
    rounded = str(floored / 1000.0)
    return rounded

def df(x):
    '''Derivative'''
    if x == 0:
        return 1
    return sin(x)/x

def nonrec_eulers(x0,y0,h,n):
    '''Hoping'''
    seq = [(x0, y0)]
    for i in range(1,n+1):
        xn = h + seq[i-1][0]
        yn = seq[i-1][1] + h * df(seq[i-1][0])
        seq.append((xn,yn))
    return seq[n][1]

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    x, y, h, n = (float(val) for val in line.split(SEPARATOR))
    n = int(n)
    print(round_half_up(nonrec_eulers(x,y,h,n)))
    