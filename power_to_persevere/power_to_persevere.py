"""System Module"""
import sys
from math import pi
import decimal

SEPARATOR = " "


def better_round(user_in: float, degree: str = "1.0") -> float:
    """Round Half Up"""
    return float(
        decimal.Decimal(user_in).quantize(
            decimal.Decimal(degree), rounding=decimal.ROUND_HALF_UP
        )
    )


cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    d, repro, wpr, rpm, ah, v, dis = (float(val) for val in line.split(SEPARATOR))
    dis *= 100
    dpro = pi * d
    rots = dis / dpro
    revs = rots * repro
    t = revs / rpm
    w = revs * wpr
    p = w / v
    am = p * t
    x = am / 60
    if x < ah:
        rt: str = str(better_round(t, "1.0000"))
        if len(rt) < 6:
            for i in range(6):
                rt += "0"
                if len(rt) >= 6:
                    break
        print(f"Success {rt}")
    else:
        print("Fail")
