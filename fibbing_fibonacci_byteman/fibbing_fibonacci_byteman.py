'''System Module'''
import sys

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

sequence = {}
for i in range(1000):
    sequence.update({i:fibo(i)})

for caseNum in range(cases):
    line = int(sys.stdin.readline().rstrip())
    if line in sequence.values():
        print("TRUE")
    else:
        print("FALSE")
