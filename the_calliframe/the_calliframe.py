"""System Module"""
import sys
import string


def only_letters(word: str):
    for c in word:
        if c not in string.ascii_letters:
            return False
    return True


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        word = sys.stdin.readline().rstrip()
        if len(word) >= 5 and len(word) <= 32 and only_letters(word):
            print(word)
            for i in range(1, len(word) - 1):
                print(
                    word[i],
                    *[" " for _ in range(len(word) - 2)],
                    word[-i - 1],
                    sep=""
                )
            print(word[::-1])
        else:
            print("Not a Calliframe")


main()
