'''System module'''
import sys

def spell_check(dictword, misspelt):
    '''Checks for misspelt words'''
    hamming = 0
    #print(dictword,misspelt)
    if len(dictword) != len(misspelt):
        return False, 0
    for l, letter in enumerate(misspelt):
        if dictword[l] != letter:
            hamming += 1
    return True, hamming
SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):

    LINE = sys.stdin.readline().rstrip()
    dictwords, misspelled = (int(val) for val in LINE.split(SEPARATOR))

    dictionary = []

    for word in range(dictwords):
        LINE = sys.stdin.readline().rstrip()
        dictionary.append(str(LINE))
    for word in range(misspelled):
        CORRECTED = False
        autocorrect = {}
        LINE = str(sys.stdin.readline().rstrip())
        for j in dictionary:
            Continue, Hamming = spell_check(j, LINE)
            if Continue:
                autocorrect.update({Hamming : j})
        for i in range(len(LINE) + 1):
            for j in autocorrect:
                if i == j:
                    CORRECTED = True
                    print(autocorrect.get(i))
                    break
            if CORRECTED:
                break
        