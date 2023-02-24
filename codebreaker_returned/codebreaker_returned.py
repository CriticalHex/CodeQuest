"""System Module"""
import sys
import string


def digraph(word: str):
    for i in range(len(word) - 1):
        yield word[i : i + 2]


def trigraph(word: str):
    for i in range(len(word) - 2):
        yield word[i : i + 3]


def better_round(val: float, n_digits: int = 0) -> float:
    """Round Half Up"""
    val *= 10**n_digits
    result = int(val + (0.5 if val >= 0 else -0.5))
    return result / 10**n_digits


def get_percent(value: str, dictionary: dict[str, int]):
    val = str(better_round(((dictionary[value] / sum(dictionary.values())) * 100), 3))
    num, dec = val.split(".")
    while len(dec) < 3:
        dec += "0"
    return f"{num}.{dec}"


def main():

    digraphs: dict[str, int] = {}
    trigraphs: dict[str, int] = {}

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        lines = int(sys.stdin.readline().rstrip())
        words: list[str] = []
        for _ in range(lines):
            line = sys.stdin.readline().rstrip().upper()
            start = 0
            stop = 0
            newline = ""
            for c in line:
                if c in string.ascii_letters or c == " ":
                    newline += c
            line = newline
            for c in line:
                if c != " ":
                    stop += 1
                else:
                    words.append(line[start:stop])
                    stop += 1
                    start = stop
            words.append(line[start:stop])
        for word in words:
            for di in digraph(word):
                if digraphs.get(di) is None:
                    digraphs[di] = 1
                else:
                    digraphs[di] += 1
            for tri in trigraph(word):
                if trigraphs.get(tri) is None:
                    trigraphs[tri] = 1
                else:
                    trigraphs[tri] += 1
        sorted_digraphs = list(digraphs)
        sorted_digraphs.sort()
        for val in sorted_digraphs:
            percent = get_percent(val, digraphs)
            print(f"{val}: {percent}%")
        sorted_trigraphs = list(trigraphs)
        sorted_trigraphs.sort()
        for val in sorted_trigraphs:
            percent = get_percent(val, trigraphs)
            print(f"{val}: {percent}%")


main()
