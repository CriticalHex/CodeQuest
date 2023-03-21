"""System Module"""
import sys
import string


def check(pword: str):
    def lowercase():
        for c in pword:
            if c in string.ascii_lowercase:
                return True
        return False

    def uppercase():
        for c in pword:
            if c in string.ascii_uppercase:
                return True
        return False

    def digits():
        for c in pword:
            if c in string.digits:
                return True
        return False

    def special():
        for c in pword:
            if c in string.punctuation:
                return True
        return False

    if len(pword) < 8:
        return False
    if lowercase() + uppercase() + digits() + special() < 3:
        return False
    for i in range(len(pword) - 2):
        if pword[i] == pword[i + 1] and pword[i] == pword[i + 2]:
            return False
    return True


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        password = sys.stdin.readline().rstrip()
        print("VALID" if check(password) else "INVALID")


main()
