"""System Module"""
import sys
from math import log, tan, pi, cos


def x(long: float, zoom: float):
    return int((((long + 180) / 360) * pow(2, zoom)))


def y(latt: float, zoom: float):
    in_frac = log(tan(latt * (pi / 180)) + (1 / cos(latt * (pi / 180)))) / pi
    return int(((1 - in_frac) * pow(2, zoom - 1)))


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        zoom, latt, long = (float(val) for val in line.split(" "))
        zoom = int(zoom)
        print(
            f"http://map.lmcodequestacademy.com/{zoom}/{x(long, zoom)}/{y(latt, zoom)}.png"
        )
        # http://tile.openstreetmap.org/14/15291/9798.png


main()
