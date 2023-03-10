"""System Module"""
import sys


def better_round(val: float, n_digits: int = 0) -> float:
    """Round Half Up"""
    val *= 10**n_digits
    result = int(val + (0.5000001 if val >= 0 else -0.5000001))  # IHATECODEQUEST
    return result / 10**n_digits


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        row1 = [int(val) for val in sys.stdin.readline().rstrip().split(" ")]
        row2 = [int(val) for val in sys.stdin.readline().rstrip().split(" ")]
        fuel = [int(val) for val in sys.stdin.readline().rstrip().split(" ")]
        a, b, c, d = row1[0], row1[1], row2[0], row2[1]
        det = (a * d) - (b * c)
        inverse_consumtion = [[d / det, -b / det], [-c / det, a / det]]
        a1, b1, c1, d1 = (
            inverse_consumtion[0][0],
            inverse_consumtion[0][1],
            inverse_consumtion[1][0],
            inverse_consumtion[1][1],
        )
        engine1 = (a1 * fuel[0]) + (c1 * fuel[1])
        engine2 = (b1 * fuel[0]) + (d1 * fuel[1])
        print(int(better_round(engine1)), int(better_round(engine2)))


main()
