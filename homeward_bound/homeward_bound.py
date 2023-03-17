"""System Module"""
import sys


class Node:
    def __init__(self, value: str, next: "Node | None" = None) -> None:
        self.val = value
        self.next: Node | None = next


def find_node(root: Node, value: str) -> Node | None:
    if root.val == value:
        return root
    if root.next is not None:
        return find_node(root.next, value)
    return None


def insert(append_to: Node, to_append: Node):
    if append_to.next:
        to_append.next = append_to.next
    append_to.next = to_append


def print_list(root: Node):
    print(root.val)
    if root.next:
        print_list(root.next)


def merge_roots(roots: list[Node]):
    while len(roots) > 1:
        merge_root(roots)


def merge_root(roots: list[Node]):
    for root in roots:
        for other in roots:
            if other is not root:
                if x := find_node(other, root.val):
                    if root.next:
                        insert(x, root.next)
                    roots.remove(root)
                    return


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        subcases = int(sys.stdin.readline().rstrip())
        trips: dict[str, str] = {}
        for _ in range(subcases):
            line = sys.stdin.readline().rstrip()
            end, start = line.split(" ")
            trips[start] = end
        roots: list[Node] = []
        for start, end in trips.items():
            for root in roots:
                if x := find_node(root, start):
                    insert(x, Node(end))
                    break
            else:
                roots.append(Node(start, Node(end)))
        # for root in roots:
        #     print_list(root)
        merge_roots(roots)
        for root in roots:
            print_list(root)


main()
