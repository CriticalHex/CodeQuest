"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        subcases = int(sys.stdin.readline().rstrip())
        decode = sys.stdin.readline().rstrip()
        for _ in range(subcases):
            print("[", end="")
            key = sys.stdin.readline().rstrip()
            for i in range(0, len(key) - 1, 2):
                decsecstr = decode[i : i + 2]
                decsechex = int(decsecstr, 16)
                keysecstr = key[i : i + 2]
                keysechex = int(keysecstr, 16)
                xored = keysechex ^ decsechex
                print(chr(xored), end="")
            print("]")


main()
