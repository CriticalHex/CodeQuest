"""System Module"""
import sys
import string


def pick(
    values: list[int],
    combos: list[str],
    used: list[bool],
    add: int,
    sum_str: str = "",
    total: int = 0,
):
    if total == add:
        if sum_str not in combos:
            combos.append(sum_str)
        return
    for i, v in enumerate(values):
        if not used[i]:
            if total + v <= add:
                used[i] = True
                if sum_str == "":
                    sum_str = str(v)
                else:
                    sum_str += f"+{v}"
                pick(values, combos, used, add, sum_str, total + v)
                used[i] = False
            else:
                return


def build_exec(values: list[int], combos: list[str], used: list[bool], add: int):
    loop_len = range(len(values))
    total = 0
    sum_str = ""
    for a in loop_len:
        if not used[a]:
            if total + values[a] < add:
                used[a] = True
                total += values[a]
                if sum_str == "":
                    sum_str = str(values[a])
                else:
                    sum_str += f"+{values[a]}"
                build_exec(values, combos, used, add)
                used[a] = False
                # sum_str.rstrip(f"+{values[a]}")
                # total -= values[a]
            elif total + values[a] == add:
                if sum_str not in combos:
                    combos.append(sum_str)
                break
            else:
                break


def attempt_one(values: list[int], combos: list[str], used: list[bool], add: int):
    loop_len = range(len(values))
    total = 0
    sum_str = ""
    for a in loop_len:
        if not used[a]:
            if total + values[a] < add:
                total += values[a]
                used[a] = True
                if sum_str == "":
                    sum_str = str(values[a])
                else:
                    sum_str += f"+{values[a]}"
                for b in loop_len:
                    if not used[b]:
                        if total + values[b] < add:
                            total += values[b]
                            used[b] = True
                            if sum_str == "":
                                sum_str = str(values[b])
                            else:
                                sum_str += f"+{values[b]}"
                            for c in loop_len:
                                if not used[c]:
                                    if total + values[c] < add:
                                        total += values[c]
                                        used[c] = True
                                        if sum_str == "":
                                            sum_str = str(values[c])
                                        else:
                                            sum_str += f"+{values[c]}"
                                        for d in loop_len:
                                            if not used[d]:
                                                if total + values[d] < add:
                                                    total += values[d]
                                                    used[d] = True
                                                    if sum_str == "":
                                                        sum_str = str(values[d])
                                                    else:
                                                        sum_str += f"+{values[d]}"
                                                    for e in loop_len:
                                                        if not used[e]:
                                                            if total + values[e] < add:
                                                                total += values[e]
                                                                used[e] = True
                                                                if sum_str == "":
                                                                    sum_str = str(
                                                                        values[e]
                                                                    )
                                                                else:
                                                                    sum_str += (
                                                                        f"+{values[e]}"
                                                                    )
                                                                # forloop here
                                                                used[e] = False
                                                                sum_str = (
                                                                    sum_str.rstrip(
                                                                        f"+{values[e]}"
                                                                    )
                                                                )
                                                                total -= values[e]
                                                            elif (
                                                                total + values[e] == add
                                                            ):
                                                                if (
                                                                    sum_str
                                                                    not in combos
                                                                ):
                                                                    combos.append(
                                                                        sum_str
                                                                    )
                                                                break
                                                            else:
                                                                break
                                                    used[d] = False
                                                    sum_str = sum_str.rstrip(
                                                        f"+{values[d]}"
                                                    )
                                                    total -= values[d]
                                                elif total + values[d] == add:
                                                    if sum_str not in combos:
                                                        combos.append(sum_str)
                                                    break
                                                else:
                                                    break
                                        used[c] = False
                                        sum_str = sum_str.rstrip(f"+{values[c]}")
                                        total -= values[c]
                                    elif total + values[c] == add:
                                        if sum_str not in combos:
                                            combos.append(sum_str)
                                        break
                                    else:
                                        break
                            used[b] = False
                            sum_str = sum_str.rstrip(f"+{values[b]}")
                            total -= values[b]
                        elif total + values[b] == add:
                            if sum_str not in combos:
                                combos.append(sum_str)
                            break
                        else:
                            break
                used[a] = False
                sum_str = sum_str.rstrip(f"+{values[a]}")
                total -= values[a]
            elif total + values[a] == add:
                if sum_str not in combos:
                    combos.append(sum_str)
                break
            else:
                break


def attempt_two(
    values: list[int], combos: list[str], used: list[bool], add: int, i: int, total: int
):
    loop_len = range(len(values))
    sum_str: str = ""

    # total += values[i] came in that way
    if total > add:
        return
    used[i] = True
    sum_str = str(values[i])
    if total == add:
        if sum_str not in combos:
            combos.append(sum_str)
        used[i] = False
        return
    for a in loop_len:
        if not used[a]:
            total += values[a]
            if total > add:
                total -= values[a]
                continue
            used[a] = True
            sum_str += f"+{values[a]}"
            if total == add:
                if sum_str not in combos:
                    combos.append(sum_str)
                used[a] = False
                total -= values[a]
                sum_str = sum_str[: len(sum_str) - (1 + len(str(values[a])))]
                continue
            for b in loop_len:
                if not used[b]:
                    total += values[b]
                    if total > add:
                        total -= values[b]
                        continue
                    used[b] = True
                    sum_str += f"+{values[b]}"
                    if total == add:
                        if sum_str not in combos:
                            combos.append(sum_str)
                        used[b] = False
                        total -= values[b]
                        sum_str = sum_str[: len(sum_str) - (1 + len(str(values[b])))]
                        continue
                    for c in loop_len:
                        pass
                    used[b] = False
                    total -= values[b]
                    sum_str = sum_str[: len(sum_str) - (1 + len(str(values[b])))]
            used[a] = False
            total -= values[a]
            sum_str = sum_str[: len(sum_str) - (1 + len(str(values[a])))]
    used[i] = False


def indent(level: int):
    return "".join("    " for _ in range(level))

def remove_r(text: str):
    temp = ""
    for c in text:
        if c != "\r":
            temp += c
    return temp

def attempt_three(values: list[int]):
    exec_lines: list[str] = []
    exec_string = """
    if total > add:
        return
    used[i] = True
    sum_str = str(values[i])
    if total == add:
        if sum_str not in combos:
            combos.append(sum_str)
        used[i] = False
        return
    """
    exec_string = remove_r(exec_string)
    for line in exec_string.split("\n"):
        exec_lines.append(line + "\n")

    above_loop = """
    if not used[a]:
        total += values[a]
        if total > add:
            total -= values[a]
            continue
        used[a] = True
        sum_str += f"+{values[a]}"
        if total == add:
            if sum_str not in combos:
                combos.append(sum_str)
            used[a] = False
            total -= values[a]
            sum_str = sum_str[:len(sum_str) - (1+len(str(values[a])))]
            continue
    """
    below_loop = """
    used[a] = False
    total -= values[a]
    sum_str = sum_str[: len(sum_str) - (1 + len(str(values[a])))]
    """

    for i in values:
        letter = string.ascii_lowercase[i]


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        add = int(line.split("=")[1])
        line = sys.stdin.readline().rstrip()
        values = [int(val) for val in line.split(",")]
        values.sort()
        used = [False for _ in range(len(values))]
        combos: list[str] = []
        for i in range(len(values)):
            attempt_two(values, combos, used, add, i, values[i])
        for combo in combos:
            print(combo)


main()
