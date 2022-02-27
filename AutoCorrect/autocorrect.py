import sys

def spellCheck(dictword, misspelt):
    hamming = 0
    #print(dictword,misspelt)
    if len(dictword) != len(misspelt):
        return False, 0
    for i in range(len(misspelt)):
                if dictword[i] != misspelt[i]:
                    hamming += 1
    return True, hamming
SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    

    line = sys.stdin.readline().rstrip()
    
    dictwords, misspelled = (int(val) for val in line.split(SEPARATOR))

    dictionary = []

    for word in range(dictwords):
        line = sys.stdin.readline().rstrip()
        dictionary.append(str(line))
    
    #print(dictionary)
    
    for word in range(misspelled):
        Corrected = False
        autocorrect = {}
        line = str(sys.stdin.readline().rstrip())
        
        for j in range(len(dictionary)):
            Continue, Hamming = spellCheck(dictionary[j], line)
            if Continue == True:
                autocorrect.update({Hamming : str(dictionary[j])})
        for i in range(len(line) + 1):
            for j in autocorrect.keys():
                if i == j:
                    Corrected = True
                    print(autocorrect.get(i))
                    break
            if Corrected == True:
                break
        