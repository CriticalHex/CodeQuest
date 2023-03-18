"""System Module"""
import sys


def better_round(val: float, n_digits: int = 0) -> float:
    """Round Half Up"""
    val *= 10**n_digits
    result = int(val + (0.5 if val >= 0 else -0.5))
    return result / 10**n_digits


def ftot(time: float):
    days: int = 0
    hours: int = 0
    minutes: int = 0
    seconds: int = 0
    if time >= 86400:
        days = int(time / 86400)
        time %= 86400
    if time >= 3600:
        hours = int(time / 3600)
        time %= 3600
    if time >= 60:
        minutes = int(time / 60)
        time %= 60
    if time >= 1:
        seconds = int(time)
    return days, hours, minutes, seconds


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        distance, speed = (float(val) for val in line.split(" "))
        time = (distance / speed) * 3600000000
        days, hours, minutes, seconds = ftot(better_round(time))
        print(
            f"Time to Mars: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
        )


main()
