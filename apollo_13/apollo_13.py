"""System Module"""
import sys


def better_round(val: float, n_digits: int = 0) -> float:
    """Round Half Up"""
    val *= 10**n_digits
    result = int(val + (0.5 if val >= 0 else -0.5))
    return result / 10**n_digits


def add_zeros(num: float):
    val, dec = str(num).split(".")
    val = list(val)
    while len(val) < 3:
        val.insert(0, "0")
    while len(dec) < 2:
        dec += "0"
    return f"{''.join(val)}.{dec}"


def angle_check(angle: float):
    angle -= 180
    if angle < 0:
        return angle + 360
    return angle


def main():
    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        in_angles = [float(val) for val in line.split(" ")]
        out_angles: list[str] = []
        for a in in_angles:
            out_angles.append(add_zeros(better_round(angle_check(a), 2)))

        print(*out_angles)


main()
