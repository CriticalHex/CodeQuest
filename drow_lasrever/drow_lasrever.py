"""System Module"""
import sys
import string


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        rev_words: list[str] = []
        words = line.split(" ")
        for word in words:
            caps = [c.isupper() for c in word]
            nospecial = "".join(
                c.lower() if c in string.ascii_letters else "" for c in word
            )[::-1]
            onlyspecial: list[tuple[str, int]] = []
            for i, c in enumerate(word):
                if c not in string.ascii_letters:
                    onlyspecial.append((c, i))
            nospecial = list(nospecial)
            for c, i in onlyspecial:
                nospecial.insert(i, c)
            for i, c in enumerate(nospecial):
                nospecial[i] = c.upper() if caps[i] else c
            nospecial = "".join(nospecial)
            rev_words.append(nospecial)
        print(*rev_words, sep=" ")


main()
