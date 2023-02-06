"""System Module"""
import sys
from math import inf

SEPARATOR = " "


class Program:
    """Data Structure"""

    def __init__(self, name: str) -> None:
        self.name = name
        self.dependent_on: list["Program"] = []
        self.dependents: list[str] = []
        self.level = inf

    def restart(self, res: list[str]):
        if self.name not in res:
            res.append(self.name)
        res.extend(val.name for val in self.dependent_on)
        for x in self.dependent_on:
            x.restart(res)
        return res


def find_proc(proc: Program, name: str) -> Program | None:
    """find program of name name"""
    if proc.name == name:
        return proc
    for x in proc.dependent_on:
        if x.name == name:
            return x
    for x in proc.dependent_on:
        return find_proc(x, name)


def get_tree(root: Program, tree: list[Program]):
    if root not in tree:
        tree.append(root)
    tree.extend(val for val in root.dependent_on)
    for x in root.dependent_on:
        get_tree(x, tree)
    return tree


cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    connections, errors = (int(val) for val in line.split(SEPARATOR))
    data: list[str] = []
    for i in range(connections):
        data.append(sys.stdin.readline().rstrip())
    programs: list[Program] = []
    for i in range(connections):
        split = data[i].split(SEPARATOR)
        start = split[0]
        end = split[1]
        for p in programs:
            found = find_proc(p, start)
            if found is not None:
                found.dependent_on.append(Program(end))
                break
        else:
            programs.append(Program(start))
            programs[-1].dependent_on.append(Program(end))
    for p in programs:
        for t in get_tree(p, []):
            t.dependent_on.sort(key=lambda x: x.name, reverse=True)
    for i in range(errors):
        error = sys.stdin.readline().rstrip()
        for p in programs:
            found = find_proc(p, error)
            if found is not None:
                tree = found.restart([])
                tree.reverse()
                for t in tree:
                    print(f"restart {t}")
        print("exit")
