"""System Module"""
import sys


class Data:
    def __init__(self, name: str, child: "Data" | None = None) -> None:
        self.name = name
        self.children: list[Data] = [child] if child else []


def find_entry(root: Data, entry: str):
    if root.name == entry:
        return root
    for child in root.children:
        if child.name == entry:
            return child
    for child in root.children:
        return find_entry(child, entry)


def main():
    catagories: list[Data] = []
    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        child, parent = line.split(",")
        for d in catagories:
            data = find_entry(d, parent)
            if data is not None:
                data.children.append(Data(child))
                break
        else:
            programs.append(Program(start))
            programs[-1].dependent_on.append(Program(end))


main()
