"""System Module"""
import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for case in range(cases):
    n_dependencies, n_errors = (
        int(val) for val in sys.stdin.readline().rstrip().split(SEPARATOR)
    )

    tree: dict[str, tuple[list[str], any]] = {}  # type: ignore

    for data in range(n_dependencies):
        parent, child = sys.stdin.readline().rstrip().split(SEPARATOR)
        if tree.get(parent):
            tree[parent][0].append(child)
        else:
            tree[parent] = ([child], None)

    for data in tree.copy():
        for data in tree[data][0]:
            if not tree.get(data):
                tree[data] = ([], None)

    layers_done: bool = False
    while not layers_done:
        layers_done: bool = True
        for name, data in tree.items():
            if data[1] is None:
                should_calc: bool = True
                highest_dependency_level: int = -1

                for j in data[0]:
                    if tree[j][1] is None:
                        should_calc: bool = False
                    elif tree[j][1] > highest_dependency_level:
                        highest_dependency_level = tree[j][1]

                if should_calc:
                    tree[name] = (data[0], highest_dependency_level + 1)
                    layers_done: bool = False

        # for p, c in tree.items():
        #    print(p, c)

    for i in range(n_errors):
        failed = sys.stdin.readline().rstrip()

        to_reboot: list[str] = [failed]
        max_index: int = 0
        current_index: int = 0

        while max_index >= current_index:
            for i in tree[to_reboot[current_index]][0]:
                if i not in to_reboot:
                    to_reboot.append(i)
                    max_index += 1
            current_index += 1

        reboot_dict: dict[str, tuple[list[str], int]] = {}

        for i in to_reboot:
            reboot_dict[i] = tree[i]

        for i in range(reboot_dict[failed][1] + 1):
            to_print: list[str] = []

            for key, value in reboot_dict.items():
                if value[1] == i:
                    to_print.append(key)

            to_print.sort()
            for i in to_print:
                print(f"restart {i}")
        print("exit")
