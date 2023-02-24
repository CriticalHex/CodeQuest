"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        people, count = (int(val) for val in line.split(" "))
        peeps = list(range(1, people + 1))
        for selection in range(people):
            sim = peeps.copy()
            for round in range(people - 1):
                # print(sim)
                # print(f"Value at index {16 % (p + 1)} is", end=" ")
                # print(sim[16 % (p + 1)])
                index = (selection + count) % len(sim) - 1
                # print(selection + 1, index, end=": ")
                selection = (index + 1) % len(sim)
                sim.pop(index)
                # print(sim.pop(index))
            print(sim)
            # if sim[0] == 1:
            #     print(selection)


main()
