"""System Module"""
import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())

for caseNum in range(cases):
    teams: list[list[str]] = []
    agents: dict[str, int] = {}
    line = sys.stdin.readline().rstrip()
    TEMPAGENTS = list(line.split(SEPARATOR))
    for agent in TEMPAGENTS:
        letter, score = (val for val in agent.split("="))
        agents[letter] = int(score)
    for i in range(1, 91, 1):
        teams.append([])
        window = range(i, i + 11)
        for agent, score in agents.items():
            if score in window:
                teams[i - 1].append(agent)
    teams.sort(key=lambda team: len(team))
    scored_teams: dict[str, int] = {}
    team_strings: list[str] = []
    for team in teams:
        if team == [] or len(team) < len(teams[-1]):
            continue
        team.sort()
        team_string: str = ""
        for agent in team:
            team_string += agent + " "
        team_string = team_string.rstrip()
        team_strings.append(team_string)
        # scored_teams[team_string] = min(map(lambda letter: ord(letter), team))
    # final_teams = sorted(scored_teams.items(), key=lambda x: x[1])
    # final_team = final_teams[0]
    team_strings.sort()
    print(team_strings[0])
