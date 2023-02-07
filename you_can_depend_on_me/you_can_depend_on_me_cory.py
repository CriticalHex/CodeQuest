"""System Module"""
import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for case in range(cases):
    n_dependencies, n_errors = (
        int(val) for val in sys.stdin.readline().rstrip().split(SEPARATOR)
    )

    tree: dict[str, tuple[list[str], int | None]] = {}

    for i in range(n_dependencies):
        parent, child = sys.stdin.readline().rstrip().split(SEPARATOR)
        if tree.get(parent):
            tree[parent][0].append(child)
        else:
            tree[parent] = ([child], None)

    for i in tree.copy():
        for i in tree[i][0]:
            if not tree.get(i):
                tree[i] = ([], None)

    layers_done: bool = False
    while not layers_done:
        layers_done: bool = True
        for _, i in tree.items():
            if i[1] is None:
                should_calc: bool = True
                highest_dependency_level: int = -1

                for _, j in i[0]:
                    if tree[j][1] is None:
                        should_calc: bool = False
                    elif tree[j][1] > highest_dependency_level:
                        highest_dependency_level = tree[j][1]
                if should_calc:
                    i = (i[0], highest_dependency_level + 1)
                    layers_done: bool = False

        for p, c in tree.items():
            print(p, c)
