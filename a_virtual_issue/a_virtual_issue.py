"""System Module"""
import sys


def extr(x: float, x1: float, y1: float, x2: float, y2: float):
    """extrapolate"""
    return y1 + (x - x1) / (x2 - x1) * (y2 - y1)


def quality_check(quality: int):
    if quality > 10:
        return 10
    if quality < 1:
        return 1
    return quality


def main():

    low = 7.77
    extrapolate = 9.435
    high = 9.99

    cases = int(sys.stdin.readline().rstrip())

    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        frame0, frame1, frame2, quality = (float(val) for val in line.split(" "))
        quality = int(quality)
        if frame2 > high:
            print(quality_check(quality - 2))
        elif frame2 > extrapolate:
            if max(extr(3, 0, frame0, 2, frame2), extr(3, 1, frame1, 2, frame2)) > high:
                print(quality_check(quality - 2))
        elif max(frame0, frame1, frame2) < low:
            print(quality_check(quality + 1))
        else:
            print(quality_check(quality))


main()
