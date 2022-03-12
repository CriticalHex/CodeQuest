'''System Module'''
import sys

def get_key(val, dictionary):
    '''inverse of getValue'''
    for key, value in dictionary.items():
        if val == value:
            return key
    return False

SEPARATOR = " "
ALPHABET = {"A":2**26, "B":2**25, "C":2**24, "D":2**23,
        "E":2**22, "F":2**21, "G":2**20, "H":2**19,
        "I":2**18, "J":2**17, "K":2**16, "L":2**15,
        "M":2**14, "N":2**13, "O":2**12, "P":2**11,
        "Q":2**10, "R":2**9, "S":2**8, "T":2**7,
        "U":2**6, "V":2**5, "W":2**4, "X":2**3,
        "Y":2**2, "Z":2**1}

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    TEAMS = []
    AGENTS = {}
    line = sys.stdin.readline().rstrip()
    TEMPAGENTS = list(line.split(SEPARATOR))
    for agent in TEMPAGENTS:
        letter, score = (val for val in agent.split("="))
        AGENTS.update({letter:int(score)})
    INDEX = 0
    for i in AGENTS.values():
        TEAMS.append([get_key(i, AGENTS)])
        for j in AGENTS.values():
            if abs(i - j) <= 10:
                TEAMS[INDEX].append(get_key(j, AGENTS))
        INDEX += 1
    for team in TEAMS:
        for p1 in team:
            for p2 in team:
                if abs(AGENTS.get(p1) - AGENTS.get(p2)) > 10:
                    team.remove(p2)
    for team in TEAMS:
        for p1 in team:
            ERR = 0
            for p2 in team:
                if p1 == p2:
                    if ERR >= 1:
                        team.remove(p2)
                    ERR += 1
    FINAL_TEAMS = {}
    for team in TEAMS:
        OUTPUT = 0
        for agent in team:
            OUTPUT += ALPHABET.get(agent)
        FINAL_TEAMS.update({tuple(team):OUTPUT})
    FINAL_VALUES = list(FINAL_TEAMS.values())
    FINAL_VALUES.sort(reverse=1)
    FINAL_TEAM = get_key(FINAL_VALUES[0], FINAL_TEAMS)
    FINAL_OUT = ""
    for agent in FINAL_TEAM:
        FINAL_OUT += agent + " "
    print(FINAL_OUT.strip())
