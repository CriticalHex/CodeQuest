"""System Module"""
import sys


class Data:
    def __init__(self, name: str, child: "Data" = None) -> None:  # type: ignore
        self.name = name
        self.children: list["Data"] = [child] if child else []


def find_entry(root: Data, entry: str):  # type: ignore
    if root.name == entry:
        return root
    for child in root.children:
        if child.name == entry:
            return child
    for child in root.children:
        if x := find_entry(child, entry):  # type: ignore
            return x  # type: ignore


def print_catalouge(catalogue: list[Data], level: int = 0):
    dashes = "".join("-" for _ in range(level))
    catalogue.sort(key=lambda x: x.name)
    for d in catalogue:
        print(f"{dashes}{d.name}")
        print_catalouge(d.children, level + 1)


def main():
    catagories: list[Data] = []
    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        child, parent = line.split(",")
        for d in catagories:
            data = find_entry(d, parent)  # type: ignore
            if data is not None:
                data.children.append(Data(child))  # type: ignore
                break
        else:
            if parent != "None":
                catagories.append(Data(parent, Data(child)))
            else:
                catagories.append(Data(child))
    print_catalouge(catagories)


main()
