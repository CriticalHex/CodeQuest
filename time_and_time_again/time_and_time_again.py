"""System Module"""
import sys
import string


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        hours: str = "00"
        minutes: str = "00"
        seconds: str = "00"
        try:
            h = line.index("h")
            if line[h - 2] in string.digits:
                hours = line[h - 2 : h]
            else:
                hours = f"0{line[h - 1 : h]}"
        except ValueError:
            pass
        try:
            m = line.index("m")
            if line[m - 2] in string.digits:
                minutes = line[m - 2 : m]
            else:
                minutes = f"0{line[m - 1 : m]}"
        except ValueError:
            pass
        try:
            s = line.index("s")
            if line[s - 2] in string.digits:
                seconds = line[s - 2 : s]
            else:
                seconds = f"0{line[s - 1 : s]}"
        except ValueError:
            pass
        print(hours, minutes, seconds, sep=":")


main()
