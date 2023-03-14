"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        first, second = (int(val) for val in line.split(" "))
        result = first * second
        flag = False
        while first != 0:
            if flag:
                fstr = f"{first}*"
                flag = False
            else:
                fstr = str(first)
            if first % 2 == 0:
                sstr = f"{second} ***"
            else:
                flag = True
                sstr = str(second)

            first //= 2
            second *= 2
            print(fstr, sstr)
        print(result)


main()
