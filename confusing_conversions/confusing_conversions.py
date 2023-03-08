"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        args = line.split(" ")
        command = args.pop(0)
        if command == "formatHeight":
            print(f"{args[0]}'{args[1]}\"")
        elif command == "concatenate":
            print(*args, sep=",")
        elif command == "formatDate":
            year = args[0]
            month = args[1]
            day = args[2]
            if len(month) < 2:
                month = "0" + month
            if len(day) < 2:
                day = "0" + day
            print(year, month, day, sep="")


main()
