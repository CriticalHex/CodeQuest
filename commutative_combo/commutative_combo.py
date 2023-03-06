"""System Module"""
import sys


def pick(
    values: list[int],
    combos: list[str],
    picked: list[bool],
    build_str: str,
    last_index: int,
    add: int,
    total: int = 0,
):
    if total > add:
        return
    picked[last_index] = True
    if build_str:
        build_str += f"+{values[last_index]}"
    else:
        build_str = str(values[last_index])
    if total == add:
        if build_str not in combos:
            combos.append(build_str)
        return
    for i, v in enumerate(values):
        if not picked[i]:
            pick(values, combos, picked, build_str, i, add, total + v)
            picked[i] = False


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        add = int(line.split("=")[1])
        line = sys.stdin.readline().rstrip()
        values = [int(val) for val in line.split(",")]
        values.sort()
        combos: list[str] = []
        for i, v in enumerate(values):
            pick(values, combos, [False for _ in range(len(values))], "", i, add, v)
        for combo in combos:
            print(combo)


main()
