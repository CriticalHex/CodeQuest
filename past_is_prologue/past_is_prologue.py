"""System Module"""
import sys

SEPARATOR = " "

cases = int(sys.stdin.readline().rstrip())


class Event:
    def __init__(self, name: str, *, day: int = 0, night: int = 0) -> None:
        self.name = name
        self.day: int = day
        self.night: int = night

    def print(self):
        if self.day > 0 or self.night > 0:
            print(self.name, self.day, self.night, sep=",")


def in_events(_events: list[Event], _event: str):
    for _e in _events:
        if _e.name == _event:
            return _e


for caseNum in range(cases):
    n_records = int(sys.stdin.readline().rstrip())
    events: list[Event] = []
    for _ in range(n_records):
        line = sys.stdin.readline().rstrip()
        _, _, time, event, is_team = (val for val in line.split(","))
        if is_team == "true":
            check = in_events(events, event)
            if check:
                if time == "Day":
                    check.day += 1
                if time == "Night":
                    check.night += 1
            else:
                if time == "Day":
                    events.append(Event(event, day=1))
                if time == "Night":
                    events.append(Event(event, night=1))
    events.sort(key=lambda x: x.name)
    for e in events:
        e.print()
