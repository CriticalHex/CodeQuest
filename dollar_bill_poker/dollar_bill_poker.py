"""System Module"""
import sys


def find_straight(counts: list[int]):
    for i in range(5):
        for j in range(i, i + 5):
            if counts[j] == 0:
                break
        else:
            return True
    return False


def find_pair(counts: list[int]):
    countstr = "".join(str(val) for val in counts)
    return countstr.count("2") >= 2


def find_house(counts: list[int]):
    if 3 in counts and 2 in counts:
        return True
    return "".join(str(val) for val in counts).count("3") >= 2


def main():
    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        counts: list[int] = []
        for i in range(1, 10):
            counts.append(line.count(str(i)))
        for i in range(5, 9):
            if i in counts:
                print(f"{line} = FIVE OF A KIND")
                break
        else:
            if 4 in counts:
                print(f"{line} = FOUR OF A KIND")
            elif find_house(counts):
                print(f"{line} = FULL HOUSE")
            elif find_straight(counts):
                print(f"{line} = STRAIGHT")
            elif 3 in counts:
                print(f"{line} = THREE OF A KIND")
            elif find_pair(counts):
                print(f"{line} = TWO PAIR")
            elif 2 in counts:
                print(f"{line} = PAIR")
            else:
                print(f"{line} = {max(list(line))}")


main()
