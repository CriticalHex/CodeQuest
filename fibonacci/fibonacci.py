'''System Module'''
import sys

SEPARATOR = " "

# def fibo(current_location):
#     '''returns a given place in the fibonacci sequence'''
#     if current_location == 1:
#         return 0
#     if current_location < 2:
#         return 1
#     return fibo(current_location - 1) + fibo(current_location - 2)

def fibo(number):
    '''returns a given place in the fibonacci sequence'''
    temp = 0
    fib_1 = temp
    fib_2 = 1
    output = 0
    if number <= 2:
        return number - 1
    for _ in range(number - 2):
        output = fib_1 + fib_2
        fib_1 = fib_2
        fib_2 = output
    return output
cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    line = int(sys.stdin.readline().rstrip())
    print(f"{line} = {fibo(line)}")
    