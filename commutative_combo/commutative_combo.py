"""System Module"""
import sys


def ascii_val(s: str):
    return [int(val) for val in s.split("+")]


def pick(
    values: list[int],
    combos: set[str],
    used: list[bool],
    build_str: str,
    last_index: int,
    add: int,
    total: int = 0,
):
    used[last_index] = True
    if total > add:
        return
    if build_str:
        build_str += f"+{values[last_index]}"
    else:
        build_str = str(values[last_index])
    if total == add:
        combos.add(build_str)
        return
    for i, v in enumerate(values):
        if not used[i]:
            pick(values, combos, used, build_str, i, add, total + v)
            for j in range(i + 1, len(values)):
                used[j] = False


def permute(
    values: list[str], used: list[bool], permutations: set[str], build_str: str
):
    for i, v in enumerate(values):
        if not used[i]:
            copy = build_str
            used[i] = True
            if build_str:
                build_str += f"+{v}"
            else:
                build_str = v
            if False in used:
                permute(values, used, permutations, build_str)
            else:
                permutations.add(build_str)
            build_str = copy
            used[i] = False


def generate_perms(combos: set[str]):
    permutations = combos.copy()
    for combo in combos:
        values = combo.split("+")
        permute(values, [False for _ in range(len(values))], permutations, "")
    return permutations


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        add = int(line.split("=")[1])
        line = sys.stdin.readline().rstrip()
        values = [int(val) for val in line.split(",")]
        values.sort(reverse=True)
        used = [False for _ in range(len(values))]
        combos: set[str] = set()
        for i, v in enumerate(values):
            pick(values, combos, used, "", i, add, v)
            for j in range(i + 1, len(used)):
                used[j] = False
        combos = generate_perms(combos)
        all_combos = sorted(list(combos), key=ascii_val)
        for combo in all_combos:
            print(combo)


main()
