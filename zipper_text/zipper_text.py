"""System Module"""
import sys


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        sys.stdin.readline()
        upper_line_lengths = [
            int(val) for val in sys.stdin.readline().rstrip().split(" ")
        ]
        sys.stdin.readline()
        lower_line_lengths = [
            int(val) for val in sys.stdin.readline().rstrip().split(" ")
        ]
        full_in: str = ""
        while line := sys.stdin.readline():
            full_in += line
        lower_message: list[str] = []
        upper_message: list[str] = []
        for c in full_in:
            if c == "-":
                upper_message.append(" ")
            elif c == "=":
                lower_message.append(" ")
            elif c.isupper():
                upper_message.append(c)
            elif c.islower():
                lower_message.append(c)
        up_message_str = "".join(upper_message)
        low_message_str = "".join(lower_message)
        for length in upper_line_lengths:
            print(up_message_str[0:length])
            up_message_str = up_message_str[length:]
        print()
        for length in lower_line_lengths:
            print(low_message_str[0:length])
            low_message_str = low_message_str[length:]


main()
