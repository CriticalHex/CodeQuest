"""System Module"""
import sys
from math import sin, cos, radians


def x(r: int, cx: int, a: float):
    return r * cos(a) + cx


def y(r: int, cy: int, a: float):
    return r * sin(a) + cy


def better_round(val: float, n_digits: int = 0) -> str:
    """Round Half Up"""
    val *= 10**n_digits
    result = int(val + (0.5 if val >= 0 else -0.5))
    answer = str(result / 10**n_digits)
    num, dec = answer.split(".")
    while len(dec) < n_digits:
        dec += "0"
    return f"{num}.{dec}"


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        cx, cy, points, r1, r2 = (int(val) for val in line.split(" "))
        inc = 360 / points
        ext_angles = [radians(90 + i * inc) for i in range(points)]
        int_angles = [radians(90 + 0.5 * inc + i * inc) for i in range(points)]
        coords: list[str] = []
        for i, ext_angle in enumerate(ext_angles):
            ext_x = better_round(x(r1, cx, ext_angle), 2)
            ext_y = better_round(y(r1, cy, ext_angle), 2)
            int_x = better_round(x(r2, cx, int_angles[i]), 2)
            int_y = better_round(y(r2, cy, int_angles[i]), 2)
            coords.append(f"{ext_x},{ext_y}")
            coords.append(f"{int_x},{int_y}")
        print(*coords, sep=" ")


main()
