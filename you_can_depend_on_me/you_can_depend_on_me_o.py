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

    def set_level(self, level: int):
        """aaaaaaa"""
        self.level = level
        for d in self.dependent_on:
            d.set_level(level + 1)

    def print_level(self):
        """aaaaaaa"""
        print(self.name, self.level, list(val.name for val in self.dependent_on))
        for d in self.dependent_on:
            d.print_level()

    def build(self):
        """uh"""
        print(self.name, list(val.name for val in self.dependent_on))
        for d in self.dependent_on:
            self.dependents.append(d.name)
            d.build()
        for d in self.dependent_on:
            print(self.name, list(val for val in self.dependents))
            # self.dependents.extend(d.dependents)

    def pathfind(self, build: list[str]):
        """wow"""
        print(self.name)
        if self.name not in build:
            build.append(self.name)
        for d in self.dependent_on:
            build.append(d.name)
        print(build)
        for d in self.dependent_on:
            d.pathfind(build)
        return build


def depended_on(proc: Program, procs: list[Program]):
    """is a node NOT top level"""
    for p in procs:
        if proc in p.dependent_on:
            return True
    return False


def has_dependents(proc: Program, procs: list[Program]):
    """IS a node bottom level"""
    if len(proc.dependent_on) == 0:
        return True
    return False


def find_proc(proc: Program, name: str) -> Program | None:
    if proc.name == name:
        return proc
    for d in proc.dependent_on:
        if d.name == name:
            return d
        return find_proc(d, name)


# def find_restarts(err: str, procs: list[Program], restarts: list[str]):
#     """recursive solution to finding errors"""
#     if err not in restarts:
#         restarts.append(err)
#     for p in procs:
#         if p.name == err:
#             for d in p.dependent_on:
#                 find_restarts(d.name, procs, restarts)
#     return restarts


def find_restarts(err: str, procs: list[Program], restarts: list[str]):
    """recursive solution to finding errors"""
    if err not in restarts:
        restarts.append(err)
    for p in procs:
        if p.name == err:
            for d in p.dependent_on:
                restarts.append(d.name)
            for d in p.dependent_on:
                find_restarts(d.name, procs, restarts)
    return restarts


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
            if p.name == start:
                p.dependent_on.append(Program(end))
                break
        else:
            programs.append(Program(start))
            programs[-1].dependent_on.append(Program(end))
    for p in programs:
        p.dependent_on.sort(key=lambda x: x.name, reverse=True)
        if not depended_on(p, programs):
            p.level = 0
    for p in programs:
        if p.level == 0:
            for d in p.dependent_on:
                d.set_level(1)
    for i in range(errors):
        error = sys.stdin.readline().rstrip()
        for p in programs:
            if p.name == "a.exe":
                p.print_level()
        print()

        # needs_restart = []
        # for p in programs:
        #     if p.name == error:
        #         needs_restart = p.pathfind([])
        # # needs_restart = find_restarts(error, programs, [])
        # needs_restart.reverse()
        # for e in needs_restart:
        #     print(f"restart {e}")
        # print("exit")
