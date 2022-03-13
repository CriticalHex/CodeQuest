'''System Module'''
import decimal
import sys

SEPARATOR = " "

def add(a,b):
    '''Add'''
    return a + b, b + a

def sub(a,b):
    '''Subtract'''
    return a - b, b - a

def mul(a,b):
    '''Multiply'''
    return a * b, b * a

def div(a,b):
    '''Divide'''
    return a / b, b / a

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    val1, ari, val2 = (str(val) for val in line.split(SEPARATOR))
    val1, val2 = float(val1), float(val2)
    if ari == "+":
        val1, val2 = add(val1,val2)
    elif ari == "-":
        val1, val2 = sub(val1,val2)
    elif ari == "*":
        val1, val2 = mul(val1,val2)
    elif ari == "/":
        val1, val2 = div(val1,val2)
    val1 = decimal.Decimal(val1).quantize(decimal.Decimal('1.0'), rounding=decimal.ROUND_HALF_UP)
    val2 = decimal.Decimal(val2).quantize(decimal.Decimal('1.0'), rounding=decimal.ROUND_HALF_UP)
    print(val1, val2)
