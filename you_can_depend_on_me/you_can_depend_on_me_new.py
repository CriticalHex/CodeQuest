"""System Module"""
import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())


class Node:
    children: list["Node"]
    name: str
    level: int

    def __init__(self, name: str):
        self.name = name
        self.children = []
        self.level = -1  # begins at -1, is set to zero if the node is top level

    def set_child_levels(self, level: int):
        for child in self.children:
            child.set_child_levels(level + 1)
        self.level = level

    def get_child_tree(self) -> list["Node"]:
        result: list["Node"] = []
        for child in self.children:
            result.extend(child.get_child_tree())
        result.extend(self.children)

        return result


for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    n_dependencies, n_failures = (int(val) for val in line.split(SEPARATOR))

    nodes: dict[str, Node] = {}

    for i in range(n_dependencies):
        parent, child = sys.stdin.readline().rstrip().split(SEPARATOR)
        if parent not in nodes:
            nodes[parent] = Node(parent)
            nodes[parent].level = 0
        if child not in nodes:
            nodes[child] = Node(child)
        nodes[parent].children.append(nodes[child])

    for node in nodes.values():
        if node.level == 0:
            node.set_child_levels(0)

    for i in range(n_failures):
        failed = sys.stdin.readline().rstrip()
        to_restart = nodes[failed].get_child_tree()
        to_restart.append(nodes[failed])
        to_restart.sort(key=lambda node: node.name)
        max_level = sorted(to_restart, key=lambda x: x.level, reverse=True)[0].level
        for level in range(max_level, -1, -1):
            for node in to_restart:
                if node.level == level:
                    print("restart " + node.name)

        print("exit")
