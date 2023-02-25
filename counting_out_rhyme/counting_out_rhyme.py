"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        people, count = (int(val) for val in line.split(" "))
        peeps = list(range(1, people + 1))
        for start in range(people):  # try each person
            sim = peeps.copy()
            next_person = start
            for _ in range(people - 1):  # simulate rounds till one person remains
                # print(f"Starting on person: {sim[next_person]}")
                index = ((count - 1) + next_person) % len(sim)
                # print(f"Counting {count} lands on person: {sim[index]}")
                sim.pop(index)
                next_person = (index) % len(sim)
            # print(f"The remaining person is {sim[0]}")
            if sim[0] == 1:
                print(peeps[start])


main()
