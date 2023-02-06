"""System Module"""
import sys

SEPARATOR = ","

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    data = list(val for val in line.split(SEPARATOR))
    employee = data[0]
    days = data[1:]
    hours: int = 0
    minutes: int = 0
    for day in days:
        hour, minute = (val for val in day.split(":"))
        hours += int(hour)
        minutes += int(minute)
    hours += int(minutes / 60)
    minutes %= 60
    minstr = f"{minutes} minutes" if minutes != 1 else f"{minutes} minute"
    hourstr = f"{hours} hours" if hours != 1 else f"{hours} hour"
    timestr = f"{hourstr} {minstr}" if minutes != 0 else f"{hourstr}"
    print(f"{employee}={timestr}")
