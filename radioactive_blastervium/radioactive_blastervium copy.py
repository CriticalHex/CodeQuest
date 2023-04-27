"""Radioactive Blastervium"""
def main():
    """Main"""
    cases = int(input())
    for _ in range(cases):
        n_intervals, time = map(int, input().split())
        intervals: list[int] = [int(input()) for _ in range(n_intervals)]
        times: list[int] = []
        for interval in intervals:
            times.extend(range(interval, time + 1, interval))
        print(len(set(times)))


main()
