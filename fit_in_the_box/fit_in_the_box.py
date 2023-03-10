def find_last_space(line: str):
    for i in range(len(line) - 1, -1, -1):
        if line[i] == " ":
            return i
    return len(line)


def main():

    cases = int(input())
    for _ in range(cases):
        max_chars, max_lines = (int(val) for val in input().split(" "))
        line = input()
        if len(line) / max_chars > max_lines:
            print("WILL NOT FIT")
        else:
            while len(line) > max_chars:
                section = line[0:max_chars]
                i = find_last_space(section)
                print(line[0:i])
                line = line[i + 1 :]
            print(line)


main()
