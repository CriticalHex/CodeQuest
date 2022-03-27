'''System Module'''
import sys
import math
from collections import namedtuple

def leap_year(year):
    '''Checks for a leap year'''
    leap = False
    if year % 4 == 0:
        leap = True
    if year % 100 == 0:
        leap = False
    if year % 400 == 0:
        leap = True
    return leap

def calculate_time(day, month, year, ap):
    '''How many days ago was a certain day?'''
    days_per_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    c_day = 27
    c_month = 4
    c_year = 2019
    days = 0
    if ap == "PM":
        days -= .5
    for k in range(year, c_year):
        days_per_month.update({2:28})
        if leap_year(k):
            days_per_month.update({2:29})
        for i in range(month, 13):
            for j in range(day, days_per_month.get(i) + 1):
                days += 1
            month += 1
            day = 1
        year += 1
        month = 1
    days_per_month.update({2:28})
    if leap_year(year):
        days_per_month.update({2:29})
    for i in range(month, c_month):
        for j in range(day, days_per_month.get(month) + 1):
            days += 1
        month += 1
        day = 1
    for j in range(day, c_day):
        days += 1
    return days

def round_half_up(original):
    '''Better Rounding WHY DOES PYTHON SUCK'''
    multiplied = original * 1000.0
    floored = math.floor(multiplied)
    remainder = multiplied - floored
    if remainder >= 0.5:
        floored += 1
    rounded = str(floored / 1000.0)
    while len(rounded) - rounded.index('.') < 4:
        rounded += '0'
    return rounded

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    File = namedtuple('File',['score','name','size'])
    # Adding values
    F1 = File('feil1','231233','12312323232')
    files = []
    line = sys.stdin.readline().rstrip()
    file_num, disk_space = (val for val in line.split(" "))
    for _ in range(int(file_num)):
        line = sys.stdin.readline().rstrip()
        date, time, ap, file_size, file_name = (val for val in line.split(" "))
        day, month, year = (int(val) for val in date.split("/"))
        files.append(File((float(file_size) / 1000) * calculate_time(day, month, year, ap), file_name, float(file_size)))
    files.sort(reverse=True)
    delete = []
    iterations = 0
    while sum(delete) < ((float(disk_space) * 1000000) * .25):
        delete.append(files[iterations].size)
        iterations += 1
    for i in range(len(delete)):
        #print(files[i].name, files[i].score)
        print(files[i].name, round_half_up(files[i].score))
