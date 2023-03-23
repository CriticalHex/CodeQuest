"""System Module"""
import sys
import string


def score(throws: list[str], throw: str, i: int) -> int:
    if throw in string.digits:
        return int(throw)
    if throw == "-":
        return 0
    if throw == "X":
        return 10
    if throw == "/":
        return 10 - score(throws, throws[i - 1], i - 1)
    return 0


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        total: int = 0
        count: int = 0
        frames = line.split(",")
        throws: list[str] = []
        for frame in frames:
            throws.extend(list(frame))
        for i, throw in enumerate(throws):
            count += 1
            if throw in string.digits:
                total += int(throw)
            elif throw == "X":
                if i + 2 < len(throws):
                    if count == 19:
                        total += (
                            10
                            + score(throws, throws[i + 1], i + 1)
                            + score(throws, throws[i + 2], i + 2)
                        )
                        break
                    count += 1
                    total += (
                        10
                        + score(throws, throws[i + 1], i + 1)
                        + score(throws, throws[i + 2], i + 2)
                    )
            elif throw == "/":
                if i + 1 < len(throws):
                    if count == 20:
                        total += (
                            10
                            - score(throws, throws[i - 1], i - 1)
                            + score(throws, throws[i + 1], i + 1)
                        )
                        break
                    total += (
                        10
                        - score(throws, throws[i - 1], i - 1)
                        + score(throws, throws[i + 1], i + 1)
                    )
        print(total)


main()
