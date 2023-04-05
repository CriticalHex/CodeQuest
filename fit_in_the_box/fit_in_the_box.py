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
        new_lines: list[str] = []
        while len(line) > max_chars:
            section = line[:max_chars]
            i = section.rfind(" ")
            new_lines.append(line[:i])
            line = line[i + 1 :]
        new_lines.append(line)
        if len(new_lines) > max_lines:
            print("WILL NOT FIT")
        else:
            for line in new_lines:
                print(line)


main()
