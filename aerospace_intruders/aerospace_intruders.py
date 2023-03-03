"""System Module"""
import sys


class Ship:
    def __init__(self, name: str, letter: str, x: int, y: int) -> None:
        self.name = name
        self.letter = letter
        self.x = x
        self.y = y


def subsort(ships: list[Ship]):
    lowest_x = ships[0]
    new_ships: list[Ship] = []
    for ship in ships:
        if ship.x == lowest_x.x:
            new_ships.append(ship)
    new_ships.sort(key=lambda x: x.y, reverse=True)
    return new_ships


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        ships: list[Ship] = []
        subcases = int(sys.stdin.readline().rstrip())
        for _ in range(subcases):
            line = sys.stdin.readline().rstrip()
            name, data = line.split("_")
            letter, loc = data.split(":")
            x, y = (int(val) for val in loc.split(","))
            ships.append(Ship(name, letter, x, y))
        while ships:
            ships.sort(key=lambda x: x.x)
            new_ships = subsort(ships)
            if len(new_ships) > 1:
                ship = new_ships[0]
            else:
                ship = ships[0]
            print(f"Destroyed Ship: {ship.name} xLoc: {ship.x}")
            new_ships.remove(ship)
            ships.remove(ship)
            for ship in ships:
                if ship.letter == "A":
                    ship.x -= 10
                if ship.letter == "B":
                    ship.x -= 20
                elif ship.letter == "C":
                    ship.x -= 30


main()
