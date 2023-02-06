"""System Module"""
import sys
import string

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    encrypted = sys.stdin.readline().rstrip().lower()
    shifts = list(int(var) for var in sys.stdin.readline().rstrip().split(" "))
    directions = list(
        bool(int(var)) for var in sys.stdin.readline().rstrip().split(" ")
    )
    decrypted: str = ""
    s_index: int = 0
    d_index: int = 0
    for c in encrypted:
        if c in string.ascii_lowercase:
            shift = shifts[s_index]
            direction = directions[d_index]
            current_index = list(string.ascii_lowercase).index(c)
            if not direction:
                new_index = (current_index + shift) % 26
                decrypted += string.ascii_lowercase[new_index]
            else:
                new_index = current_index - shift
                decrypted += string.ascii_lowercase[new_index]
            s_index += 1
            s_index %= len(shifts)
            d_index += 1
            d_index %= len(directions)
        else:
            decrypted += c
    print(decrypted)
