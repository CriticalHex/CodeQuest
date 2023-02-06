"""System Module"""
import sys
import decimal


def better_round(user_in: float, degree: str = "1.0"):
    """Round Half Up"""
    return float(
        decimal.Decimal(user_in).quantize(
            decimal.Decimal(degree), rounding=decimal.ROUND_HALF_UP
        )
    )


SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    vol, fill, leak = (float(val) for val in line.split(SEPARATOR))
    waste = (vol / (fill - leak)) * leak
    print(int(better_round(waste, "1")))
