"""System Module"""
import sys
import decimal

SEPARATOR = " "


def br(num: float, degree: str = "1.00"):
    return float(
        decimal.Decimal(f"{num}").quantize(
            decimal.Decimal(degree), rounding=decimal.ROUND_HALF_UP
        )
    )


cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    money = float(line[1:])
    quarters = int(money / 0.25)
    money %= 0.25
    money = br(money)
    dimes = int(money / 0.10)
    money %= 0.10
    money = br(money)
    nickels = int(money / 0.05)
    money %= 0.05
    money = br(money)
    pennies = int(money / 0.01)
    money %= 0.01
    money = br(money)
    print(line)
    print(f"Quarters={quarters}")
    print(f"Dimes={dimes}")
    print(f"Nickels={nickels}")
    print(f"Pennies={pennies}")
