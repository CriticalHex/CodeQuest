"""easy problem"""
import sys
import decimal


SEPERATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    density, volume = (float(val) for val in line.split(SEPERATOR))
    mass = density * volume
    print(
        decimal.Decimal(f"{mass}").quantize(
            decimal.Decimal("1.00"), rounding=decimal.ROUND_HALF_UP
        )
    )
