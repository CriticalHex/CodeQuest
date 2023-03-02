"""System Module"""
import sys

def check_letters(a: str, b: str):
    la = list(a)
    lb = list(b)
    la.sort()
    lb.sort()
    return la == lb

def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        incorrect, correct = sys.stdin.readline().rstrip().split(" ")
        if check_letters(incorrect, correct):
            if (incorrect[0], incorrect[-1]) == (correct[0], correct[-1]):
                print(correct)
            else:
                print(incorrect)
        else:
            print(incorrect)




main()
