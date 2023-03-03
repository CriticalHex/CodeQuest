'''System module'''
import sys

SEPARATOR = "|"


cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    BAD_ANAGRAM = True
    line = sys.stdin.readline().rstrip()
    word1, word2 = (val for val in line.split(SEPARATOR))

    if word1 != word2 and len(word1) == len(word2):
        for i in word1:
            for j in word2:
                if i != j:
                    BAD_ANAGRAM = True
                else:
                    word2 = list(word2)
                    word2.remove(j)
                    BAD_ANAGRAM = False
                    break
            if BAD_ANAGRAM:
                break
    if BAD_ANAGRAM:
        print(line, end = "")
        print(" = NOT AN ANAGRAM")
    else:
        print(line, end = "")
        print(" = ANAGRAM")
