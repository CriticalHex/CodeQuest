'''System Module'''
import sys

def slope(x1,x2,y1,y2):
    '''Calculate Slope'''
    return (y2-y1)/(x2-x1)

SEPARATOR = ","

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    subcases = int(sys.stdin.readline().rstrip())
    for _ in range(subcases):
        line = sys.stdin.readline().rstrip()
        plane_name = line
        line = sys.stdin.readline().rstrip()
        plane_x, plane_y = (float(val) for val in line.split(SEPARATOR))
        line = sys.stdin.readline().rstrip()
        start_x, start_y = (float(val) for val in line.split(SEPARATOR))
        line = sys.stdin.readline().rstrip()
        end_x, end_y = (float(val) for val in line.split(SEPARATOR))
        if slope(plane_x, start_x, plane_y, start_y) >= -1.6 and\
            slope(plane_x, end_x, plane_y, end_y) <=-.8:
            print(plane_name, ", Clear To Land!", sep="")
        else:
            print(plane_name, ", Abort Landing!", sep="")
        