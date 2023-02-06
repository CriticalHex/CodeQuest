"""System Module"""
import sys
import decimal

SEPARATOR = ","


def better_round(user_in: float, degree: str = "1.00"):
    """Round Half Up"""
    return decimal.Decimal(user_in).quantize(
        decimal.Decimal(degree), rounding=decimal.ROUND_HALF_UP
    )


cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    days = int(sys.stdin.readline().rstrip())
    total: float = 0
    daily_balances: list[float] = []
    for _ in range(days):
        line = sys.stdin.readline().rstrip()
        day, add, subtract = (val for val in line.split(SEPARATOR))
        if add:
            add = float(add)
            total += add
        if subtract:
            subtract = float(subtract)
            total -= subtract
        daily_balances.append(total)
    total = sum(daily_balances)
    print(f"${better_round((total / days) * (0.18 / 12))}")
