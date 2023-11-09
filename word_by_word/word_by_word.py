"""Problem Solution"""
import string


def main():

    cases = int(input())
    for _ in range(cases):
        counts: dict[int, int] = {}  # length to how many words of that length
        n = int(input())
        for _ in range(n):
            line = input()
            for c in string.punctuation:
                line = line.replace(c, "")
            for word in line.split():
                if counts.get(len(word)):
                    counts[len(word)] += 1
                else:
                    counts[len(word)] = 1
        modes: list[int] = []
        most_counted = max(counts.values())
        values: list[int] = []
        for k, v in counts.items():
            if v == most_counted:
                modes.append(k)
            values.extend(k for _ in range(v))
        values.sort()
        modes.sort()
        length = len(values)
        largest = max(values)
        smallest = min(values)
        average = sum(values) / length
        median = (
            (values[length // 2 - 1] + values[length // 2]) / 2
            if len(values) % 2 == 0
            else values[length // 2]
        )
        print(f"Average: {average:.1f}")
        print(f"Median: {median:.1f}")
        print("Modes: ", end="")
        print(*modes, sep=",")
        print(f"Range: {largest - smallest}")
        for i in range(1, largest + 1):
            if not counts.get(i):
                counts[i] = 0
            print(f"{i:>2}|{'x'*counts[i]}")


main()
