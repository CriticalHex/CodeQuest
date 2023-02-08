"""System Module"""
import sys
import struct
import decimal

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())


def bin_to_float(b: str):
    """Convert binary string to a float."""
    bf = int.to_bytes(int(b, 2), 4)  # 4 bytes needed for IEEE 754 binary32.
    return struct.unpack(">f", bf)[0]


def bin_to_double(b: str):
    """Convert binary string to a double."""
    bf = int.to_bytes(int(b, 2), 8)  # 8 bytes needed for IEEE 754 binary64.
    return struct.unpack(">d", bf)[0]


def better_round(val: float, n_digits: int = 0) -> float:
    """Round Half Up"""
    val *= 10**n_digits
    result = int(val + (0.5 if val >= 0 else -0.5))
    return result / 10**n_digits


def float_to_scientific(val: float) -> str:
    if val > 99999.99999 or val < 0.00001:
        strval = f"{val:.5e}"
        return strval
    return str(val)


for caseNum in range(cases):
    hex_in = int(sys.stdin.readline().rstrip(), 16)
    binary = list(f"{hex_in:0>b}")
    binary.reverse()
    # print(binary)
    n_measurands = int(sys.stdin.readline().rstrip())
    for _ in range(n_measurands):
        datatype, start, size = sys.stdin.readline().rstrip().split(SEPARATOR)
        start = int(start)
        size = int(size)
        if datatype == "int":
            arr = binary[start : start + size]
            val: int = 0
            for i in range(size):
                if i == size - 1:
                    val -= int(arr[i]) * (2**i)
                else:
                    val += int(arr[i]) * (2**i)
            # print("".join(binary[-start - size : -start]))
            print(val)
        elif datatype == "uint":
            arr = "".join(reversed(binary[start : start + size]))
            print(int(arr, 2))
        elif datatype == "float":
            arr = reversed(binary[start : start + size])
            s = "".join(arr)
            unrounded = bin_to_float(s)
            # rounded = str(better_round(unrounded, "1.00000"))
            # first, second = rounded.split("+")
            print(better_round(unrounded, 5))
        elif datatype == "double":
            arr = reversed(binary[start : start + size])
            s = "".join(arr)
            unrounded = bin_to_double(s)
            # print(f"{unrounded:f}")
            assert isinstance(unrounded, float)
            # print(f"{unrounded:.5e}")
            print(float_to_scientific(better_round(unrounded, 5)))
