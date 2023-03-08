"""System Module"""
import sys
from math import radians, sin, cos


def wind_ns(speed: float, direction: int):
    val = speed * cos(radians(direction))
    return abs(val)


def wind_ew(speed: float, direction: int):
    val = speed * sin(radians(direction))
    return abs(val)


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        n_potentials = int(sys.stdin.readline().rstrip())
        lines: list[str] = []
        for _ in range(n_potentials):
            lines.append(sys.stdin.readline().rstrip())
        for line in lines:
            date, time, cloud_thickness, wind_speed, wind_direction = line.split(" ")
            cloud_thickness = int(cloud_thickness)
            wind_speed = float(wind_speed)
            wind_direction = int(wind_direction)
            if cloud_thickness > 1000:
                continue
            if (
                wind_ns(wind_speed, wind_direction) > 20
                or wind_ew(wind_speed, wind_direction) > 40
            ):
                continue
            print(f"{date} {time}")
            break
        else:
            print("ABORT LAUNCH")


main()
