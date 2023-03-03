"""System Module"""
import sys
import string

def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        val1, val2 = line.split("|")
        greeting: list[str] = []
        response: list[str] = []
        for c in val1.lower():
            if c in string.ascii_lowercase:
                greeting.append(c)
        for c in val2.lower():
            if c in string.ascii_lowercase:
                response.append(c)
        for c in response:
            if c not in greeting:
                print("You're not a secret agent!")
                break
        else:
            print("That's my secret contact!")

main()
