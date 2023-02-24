"""System Module"""
import sys


class Tank:
    def __init__(self, capacity: int) -> None:
        self.full = False
        self.cap = capacity
        self.value: int = 0
        self.strval: str = ""


def tanks_equal(tanks: list[Tank]):
    val = 0
    for t in tanks:
        if not t.full:
            val = t.value
            break
    for t in tanks:
        if not t.full:
            if t.value != val:
                return False
    return True


def all_full(tanks: list[Tank]):
    for t in tanks:
        if not t.full:
            return False
    return True


def unfull_count(tanks: list[Tank]):
    counter = 0
    for t in tanks:
        if not t.full:
            counter += 1
    return counter


def distribute(tanks: list[Tank], fuel: int):
    if fuel > unfull_count(tanks):
        for t in tanks:
            if not t.full:
                t.value += 1
                fuel -= 1
                if t.value == t.cap:
                    t.full = True
        return fuel, True
    return fuel, False


def simplify_frac(n: int, d: int):
    i = 2
    while i < min(n, d) + 1:
        if n % i == 0 and d % i == 0:
            n = n // i
            d = d // i
        else:
            i += 1
    return n, d


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        fuel, n_tanks = (int(val) for val in line.split(" "))
        line = sys.stdin.readline().rstrip()
        tanks: list[Tank] = []
        tanks.extend(Tank(int(val)) for val in line.split(" "))
        filling = True
        while filling:
            fuel, filling = distribute(tanks, fuel)
        unfull: list[Tank] = []
        for t in tanks:
            if not t.full:
                unfull.append(t)
                fuel += t.value
                t.value = 0
            else:
                t.strval = str(t.value)
        for t in unfull:
            if fuel // len(unfull) == fuel / len(unfull):
                t.strval = f"{fuel // len(unfull)}"
            else:
                n, d = fuel, len(unfull)
                n, d = simplify_frac(n, d)
                t.strval = f"{n}/{d}"

        for t in tanks:
            t.strval += " "
        output = "".join(val.strval for val in tanks).rstrip()
        print(output)


main()
