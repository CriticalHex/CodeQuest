"""Problem Solution"""


def better_round(val: float, n_digits: int = 0) -> str:
    """Round Half Up"""
    val *= 10**n_digits
    result = int(val + (0.500001 if val >= 0 else -0.500001))
    rounded = str(result / 10**n_digits)
    num, dec = rounded.split(".")
    while len(dec) < n_digits:
        dec += "0"
    return f"{num}.{dec}"


def main():

    cases = int(input())
    for _ in range(cases):
        item_count = int(input())
        budgets = map(float, input().split())
        costs = map(float, input().split())
        avg = (sum(costs) - sum(budgets)) / item_count
        print(better_round(avg, 2))


main()
