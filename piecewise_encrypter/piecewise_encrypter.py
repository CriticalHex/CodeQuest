"""System Module"""
import sys
import string


def gcf(num: int):
    for i in range(26):
        for j in range(26):
            if j * i == num and j != num and i != num:
                return max(j, i)
    return 1


def main():
    alpha: dict[str, int] = {}
    for i in range(1, 27):
        alpha[string.ascii_uppercase[i - 1]] = i

    for i in range(5):
        alpha[string.ascii_uppercase[i]] += 6

    for i in range(5, 10):
        alpha[string.ascii_uppercase[i]] **= 2

    for i in range(10, 15):
        num = alpha[string.ascii_uppercase[i]]
        alpha[string.ascii_uppercase[i]] = ((num % 3) * 5) + 1

    for i in range(15, 20):
        num = alpha[string.ascii_uppercase[i]]
        a, b = int(str(num)[0]), int(str(num)[1])
        alpha[string.ascii_uppercase[i]] = (a + b) * 8

    for i in range(20, 26):
        num = alpha[string.ascii_uppercase[i]]
        alpha[string.ascii_uppercase[i]] = gcf(num) * 2
    # print(alpha)

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        output = ""
        for c in line:
            output += string.ascii_uppercase[(alpha[c] - 1) % 26]
        print(output)


main()
