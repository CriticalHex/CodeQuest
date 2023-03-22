"""System Module"""
import sys


def get_group_number(c: str):
    g1 = ("b", "f", "p", "v")
    g2 = ("c", "g", "j", "k", "q", "s", "x", "z")
    g3 = ("d", "t")
    g4 = "l"
    g5 = ("m", "n")
    g6 = "r"
    if c in g1:
        return "1"
    if c in g2:
        return "2"
    if c in g3:
        return "3"
    if c in g4:
        return "4"
    if c in g5:
        return "5"
    if c in g6:
        return "6"
    return "0"


def get_numbered_group(c: str):
    g1 = ("b", "f", "p", "v")
    g2 = ("c", "g", "j", "k", "q", "s", "x", "z")
    g3 = ("d", "t")
    g4 = "l"
    g5 = ("m", "n")
    g6 = "r"
    if c in g1:
        return g1
    if c in g2:
        return g2
    if c in g3:
        return g3
    if c in g4:
        return g4
    if c in g5:
        return g5
    if c in g6:
        return g6


def remove_similar(line: str):
    wi = ("h", "w")
    l = list(line)
    while True:
        for i in range(len(l) - 1):
            first = l[i]
            if group := get_numbered_group(first):
                if l[i + 1] in group or l[i + 1] in wi:  # type: ignore
                    l.pop(i + 1)
                    break
        else:
            return "".join(l)


def remove_wild_vowels(line: str):
    wi = ("h", "w")
    vo = ("a", "e", "i", "o", "u", "y")
    l = list(line[1:])
    for c in line[1:]:
        if c in wi or c in vo:
            l.remove(c)
    return line[0] + "".join(l)


def get_code(line: str):
    line = remove_similar(line.lower())
    line = remove_wild_vowels(line)
    output = line[0].upper()
    for i in range(1, 4):
        try:
            output += get_group_number(line[i])
        except IndexError:
            output += "0"
    return output


def main():
    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        subcases = int(sys.stdin.readline().rstrip())
        codes: dict[str, int] = {}
        for _ in range(subcases):
            line = sys.stdin.readline().rstrip()
            code = get_code(line)
            if codes.get(code):
                codes[code] += 1
            else:
                codes[code] = 1
        ordered_codes = sorted(codes.keys())
        print("OUTPUT")
        for code in ordered_codes:
            print(code, codes[code])


main()
