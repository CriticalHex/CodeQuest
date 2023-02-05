"""System Module"""
import sys
from math import floor

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    y = int(sys.stdin.readline().rstrip())
    a = y % 19
    b = y % 4
    c = y % 7
    k = floor(y / 100)
    p = floor((13 + (8 * k)) / 25)
    q = floor(k / 4)
    m = (15 - p + k - q) % 30
    n = (4 + k - q) % 7
    d = ((19 * a) + m) % 30
    e = ((2 * b) + (4 * c) + (6 * d) + n) % 7
    f = ((11 * m) + 11) % 30

    date = 22 + d + e

    if date <= 31:
        mm: int = 3
    else:
        date -= 31
        mm: int = 4
    if mm == 4 and date == 25 and d == 28 and e == 6 and f < 19:
        date: int = 18
    elif mm == 4 and date == 26 and d == 29 and e == 6:
        date: int = 19

    if date > 9:
        print(f"{y}/0{mm}/{date}")
    else:
        print(f"{y}/0{mm}/0{date}")

# 𝑎 =𝑦 𝑚𝑜𝑑 19
# 𝑏 =𝑦 𝑚𝑜𝑑 4
# 𝑐 =𝑦 𝑚𝑜𝑑 7
# 𝑘 =𝑓𝑙𝑜𝑜𝑟( 𝑦 / 100)
# 𝑝=𝑓𝑙𝑜𝑜𝑟(13+8𝑘 / 25 )
# 𝑞 =𝑓𝑙𝑜𝑜𝑟(𝑘 / 4)
# 𝑚=(15−𝑝+𝑘−𝑞) 𝑚𝑜𝑑 30
# 𝑛= (4+𝑘−𝑞) 𝑚𝑜𝑑 7
# 𝑑 =(19𝑎+𝑚) 𝑚𝑜𝑑 30
# 𝑒 =(2𝑏+4𝑐+6𝑑+𝑛) 𝑚𝑜𝑑 7
# 𝑓 =(11𝑚+11) 𝑚𝑜𝑑 30
