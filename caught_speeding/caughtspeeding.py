'''System module'''
import sys

SEPARATOR = " "

def ticket_me(speed, birthday):
    '''Checks which ticket you recieve'''
    bdaybonus = 0
    if birthday:
        bdaybonus = 5
    if speed <= 60 + bdaybonus:
        print("no ticket")
    elif speed <= 80 + bdaybonus:
        print("small ticket")
    elif speed > 80 + bdaybonus:
        print("big ticket")

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    S, B = (val for val in line.split(SEPARATOR))
    S = int(S)
    if B == "false":
        B = False
    else:
        B = True
    ticket_me(S, B)
    