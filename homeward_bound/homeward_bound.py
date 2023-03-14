"""System Module"""
import sys


class Node:
    def __init__(self, value: str, next: "Node" | None = None) -> None:
        self.val = value
        self.next: Node | None = next


def find_node(root: Node, value: str) -> Node | None:
    if root.val == value:
        return root
    if root.next is not None:
        return find_node(root.next, value)
    return None


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        end, start = line.split(" ")
        if x:=find_node()

main()
