"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        up_to = int(sys.stdin.readline().rstrip())
        primes: list[int] = []
        potentials: list[int] = list(range(2, up_to + 1))
        while potentials:
            primes.append(potentials[0])
            count = 0
            copy = potentials.copy()
            for val in potentials:
                if val % primes[-1] == 0:
                    count += 1
                    copy.remove(val)
            potentials = copy.copy()
            if count > 1:
                print(f"Prime {primes[-1]} Composite Set Size: {count - 1}")
        print("{", end="")
        print(*primes, sep=",", end="")
        print("}")


main()
