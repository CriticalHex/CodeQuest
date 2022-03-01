import sys

SEPARATOR = " "

def ticketMe(speed, birthday):
    bdaybonus = 0
    if birthday == True:
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
    
    speed, birthday = (val for val in line.split(SEPARATOR))
    speed = int(speed)
    if birthday == "false":
        birthday = False
    else:
        birthday = True
    ticketMe(speed, birthday)
    