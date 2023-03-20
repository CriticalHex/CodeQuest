"""System Module"""
import sys


def mandelbrot(c: complex):
    z = complex(0, 0)
    count = 0
    while abs(z) < 100 and count < 53:
        z = (z * z) + c
        count += 1
    return count


def color(count: int):
    if count <= 10:
        return "RED"
    if count < 21:
        return "ORANGE"
    if count < 31:
        return "YELLOW"
    if count < 41:
        return "GREEN"
    if count < 51:
        return "BLUE"
    return "BLACK"


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        a_in, b_in = line.split(" ")
        a, b = float(a_in), float(b_in)
        c = complex(a, b)
        count = mandelbrot(c)
        print(f"{a_in}+{b_in}i {color(count)}")


main()
