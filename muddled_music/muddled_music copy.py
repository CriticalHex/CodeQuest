"""System Module"""
import sys


def space_strip(line: str):
    output = ""
    for c in line:
        if c != " ":
            output += c
    return output


def key(pair: str):
    title, artist = (val.lower() for val in pair.split(" - "))
    if artist[:4] == "the ":
        return f"{artist[4:]} {title}"
    return f"{artist} {title}"


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        pairs: list[str] = []
        subcases = int(sys.stdin.readline().rstrip())
        for _ in range(subcases):
            line = sys.stdin.readline().rstrip()
            pairs.append(line)
        pairs.sort(key=key)
        for pair in pairs:
            print(pair)


main()
