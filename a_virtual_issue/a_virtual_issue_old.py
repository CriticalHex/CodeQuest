'''System Module'''
import sys

def extrapolate(x, x1, y1, x2, y2):
    '''extrapolate'''
    return y1 + (x - x1)/(x2 - x1) * (y2 - y1)

SEPARATOR = " "
LOW = 7.77
EXTR = 9.435
HIGH = 9.99
cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    frame0, frame1, frame2, quality = (float(val) for val in line.split(SEPARATOR))
    quality = int(quality)
    if frame0 > HIGH and frame1 > HIGH and frame2 > HIGH:
        quality -= 2
    elif frame2 > EXTR:
        if extrapolate(3,0,frame0,2,frame2) > HIGH:
            quality -= 2
        elif extrapolate(3,1,frame1,2,frame2) > HIGH:
            quality -= 2
    elif frame0 < LOW and frame1 < LOW and frame2 < LOW:
        quality += 1
    if quality > 10:
        quality = 10
    elif quality < 1:
        quality = 1
    print(quality)
    