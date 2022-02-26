import sys

SEPARATOR = "|"


cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    BadAnagram = True
    line = sys.stdin.readline().rstrip()
    
    word1, word2 = (val for val in line.split(SEPARATOR))

    if word1 != word2 and len(word1) == len(word2):
        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] != word2[j]:
                    BadAnagram = True
                else:
                    word2 = list(word2)
                    word2[j] = "_"
                    word2 = "".join(word2)
                    BadAnagram = False
                    break
            if BadAnagram == True:
                break
    if BadAnagram == True:
        print(line, end = "")
        print(" = NOT AN ANAGRAM")
    else:
        print(line, end = "")
        print(" = ANAGRAM")
        
