import sys

num_cases = int(sys.stdin.readline().rstrip())

for _ in range(num_cases):
    text = sys.stdin.readline().rstrip()
    text = text.split(", ")

    for i in range(len(text)):
        text[i] = int(text[i])
    
    if text[0] + text[1] <= text[2] or text[0] + text[2] <= text[1] or text[1] + text[2] <= text[0]:
        print("Not a Triangle")
    else:
        if text[2] == text[1] and text[2] == text[0] and text[1] == text[0]:
            print("Equilateral")
        elif text[0] != text[1] and text[0] != text[2] and text[1] != text[2]:
            print("Scalene")
        elif (text[0] == text[1] and text[0] != text[2]) or (text[1] == text[2] and text[1] != text[0]) or (text[2] == text[0] and text[2] != text[1]):
            print("Isosceles")