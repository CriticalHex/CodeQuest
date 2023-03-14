"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        subcases = int(input())
        last_elevation = 0
        last_altitude = 0
        for _ in range(subcases):
            line = sys.stdin.readline().rstrip()
            current_altitude, next_elevation = (float(val) for val in line.split(","))
            predicted_altitude = 2 * current_altitude - last_altitude
            if next_elevation >= predicted_altitude:
                print("PULL UP!")
            elif current_altitude - last_elevation <= 500:
                print("Low Altitude!")
            else:
                print("ok")
            last_elevation = next_elevation
            last_altitude = current_altitude


main()
