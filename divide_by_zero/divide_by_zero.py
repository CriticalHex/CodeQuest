'''System Module'''
import decimal
import sys

def better_round(user_in, degree: str = "1.0"):
    '''Round Half Up'''
    return decimal.Decimal(user_in).quantize(decimal.Decimal(degree),rounding=decimal.ROUND_HALF_UP)

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = sys.stdin.readline().rstrip()
    dividend, divisor = (val for val in line.split(SEPARATOR))
    try:
        dividend = float(dividend)
        try:
            divisor = float(divisor)
            try:
                print(better_round(dividend / divisor))
            except ZeroDivisionError:
                print("Divide By Zero")
        except ValueError:
            print("Invalid Divisor")
    except ValueError:
        print("Invalid Dividend")
    