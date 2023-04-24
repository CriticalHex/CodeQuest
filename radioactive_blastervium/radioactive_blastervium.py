"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        n_intervals, time = map(int, line.split(" "))
        intervals: list[int] = []
        for _ in range(n_intervals):
            intervals.append(int(sys.stdin.readline().rstrip()))
        times: set[int] = set()
        for interval in intervals:
            for i in range(interval, time + 1, interval):
                times.add(i)
        # print(*times)
        print(len(times))


main()
