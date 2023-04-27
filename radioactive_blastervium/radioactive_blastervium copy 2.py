def product(arr: list[int]):
    p = 1
    for i in arr:
        p *= i
    return p

def permutations(frequencies)


def count2(frequencies:list[int], time: int):
    total = 0
    for permutation in permutations():
        total += pow(-1,len(permuation) + 1) * int(time/product(permutation))

def main():

    cases = int(input())
    for _ in range(cases):
        n_frequencies, time = map(int, input().split())
        frequencies:list[int] = []
        for _ in range(n_frequencies):
            frequencies.append(int(input()))
        times:set[int] = set()
        for frequency in frequencies:
            for i in range(frequency, time + 1, frequency):
                times.add(i)
        print(len(times))
        print(count(frequencies, time))

main()