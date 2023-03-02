"""System Module"""
import sys


def words_from_string(line: str):
    words: list[str] = []
    start = 0
    stop = 0
    for c in line:
        if c != " ":
            stop += 1
        else:
            words.append(line[start:stop])
            stop += 1
            start = stop
    words.append(line[start:stop])
    return words


def letters_from_morse(line: str):
    lsep = "   "
    wsep = "       "

    def find_end(line: str, start: int):
        for i in range(start, len(line)):
            if wsep in line[i : i + 7]:
                return i, 7
            if lsep in line[i : i + 3]:
                return i, 3
        return len(line), len(line)

    morse: list[str] = []
    start = 0
    while start < len(line):
        end, add = find_end(line, start)
        morse.append(line[start:end])
        if add == 7:
            morse.append(" ")
        start = end + add
    return morse


def main():
    letter_to_morse: dict[str, str] = {}
    morse_to_letter: dict[str, str] = {}
    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        for _ in range(26):
            line = sys.stdin.readline().rstrip()
            letter, morse = line[0], line[2:]
            letter_to_morse[letter] = morse
            morse_to_letter[morse] = letter
        eline = sys.stdin.readline().rstrip()
        ewords = words_from_string(eline)
        encoded = ""
        for word in ewords:
            for letter in word:
                encoded += letter_to_morse[letter]
                encoded += "   "
            encoded += "    "
        encoded = encoded.rstrip()
        print(encoded)

        dline = sys.stdin.readline().rstrip()
        dletters = letters_from_morse(dline)
        decoded = ""
        for letter in dletters:
            if letter != " ":
                decoded += morse_to_letter[letter]
            else:
                decoded += " "
        decoded = decoded.rstrip()
        print(decoded)


main()
