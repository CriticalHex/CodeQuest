"""System Module"""
import sys


class Airplane:
    def __init__(self, date: str) -> None:
        year, month, day = (int(val) for val in date.split("-"))
        self.made = year * 365 + month * 30 + day


def eval(produced: list[Airplane], orders: int):
    flag: bool = True
    for _ in range(orders):
        line = sys.stdin.readline().rstrip()
        if flag:
            date, total = line.split(" ")
            year, month, day = (int(val) for val in date.split("-"))
            made = year * 365 + month * 30 + day
            # print("Checking", made)
            # for plane in produced:
            # print(plane.made)
            for _ in range(int(total)):
                for plane in produced:
                    # print(made - plane.made)
                    if made - plane.made < 28 and made - plane.made > 0:
                        produced.remove(plane)
                        break
                else:
                    flag = False
    if not flag:
        return flag
    return not bool(produced)


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        products, orders = (int(val) for val in line.split(" "))
        produced: list[Airplane] = []
        for _ in range(products):
            line = sys.stdin.readline().rstrip()
            date, total = line.split(" ")
            for _ in range(int(total)):
                produced.append(Airplane(date))
        print("OK" if eval(produced, orders) else "NOT OK")


main()
