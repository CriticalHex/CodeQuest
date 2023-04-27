"""Radioactive Blastervium"""


def recurse(
    targ_periods: int, periods: list[int], n_time_steps: int, multiplier: int = 1
) -> int:
    total: int = 0
    if targ_periods > 1:
        for i, period in enumerate(periods[: len(periods) - targ_periods + 1]):
            total += recurse(
                targ_periods - 1,
                periods[i + 1 :],
                n_time_steps,
                multiplier * period,
            )
    else:
        for period in periods:
            total += int(n_time_steps / (multiplier * period))
    return total


def main():
    """Main"""
    cases: int = int(input())
    for _ in range(cases):
        n_periods, n_time_steps = map(int, input().split())
        periods: list[int] = []
        for _ in range(n_periods):
            periods.append(int(input()))
        total: int = 0
        for i in range(1, n_periods + 1):
            if i % 2:
                total += recurse(i, periods, n_time_steps)
            else:
                total -= recurse(i, periods, n_time_steps)
        print(total)


main()
