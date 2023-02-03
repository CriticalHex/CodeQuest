"""System Module"""
import sys

ALPHABET = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25,
}
LA = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
CA = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    encrypted = sys.stdin.readline().rstrip().lower()
    shifts = list(int(var) for var in sys.stdin.readline().rstrip().split(" "))
    directions = list(
        bool(int(var)) for var in sys.stdin.readline().rstrip().split(" ")
    )
    # print(encrypted, shifts, directions)
    decrypted: str = ""
    s_index: int = 0
    d_index: int = 0
    for c in encrypted:
        if c in LA:
            shift = shifts[s_index]
            direction = directions[d_index]
            current_index = ALPHABET[c.upper()]
            if not direction:
                new_index = (current_index + shift) % 26
                decrypted += LA[new_index]
            else:
                new_index = current_index - shift
                decrypted += LA[new_index]
            s_index += 1
            s_index %= len(shifts)
            d_index += 1
            d_index %= len(directions)
        else:
            decrypted += c
    print(decrypted)
