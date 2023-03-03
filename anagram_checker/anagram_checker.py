"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        word1, word2 = line.split("|")
        rem1, rem2 = list(word1), list(word2)
        if word1 == word2:
            print(f"{line} = NOT AN ANAGRAM")
        else:  # anagram check
            for c in word1:
                if c in word2 and c in rem1 and c in rem2:
                    rem1.remove(c)
                    rem2.remove(c)
            if not rem1 and not rem2:
                print(f"{line} = ANAGRAM")
            else:
                print(f"{line} = NOT AN ANAGRAM")


main()
