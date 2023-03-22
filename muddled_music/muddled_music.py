"""System Module"""
import sys


class Artist:
    def __init__(self, name: str, track: str) -> None:
        self.name = name
        self.tracks: list[str] = [track]


def in_artists(name: str, artists: list[Artist]):
    for artist in artists:
        if artist.name == name:
            return artist


def remove_the(name: str):
    if name[:4].lower() == "the ":
        return name[4:]
    return name


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        artists: list[Artist] = []
        subcases = int(sys.stdin.readline().rstrip())
        for _ in range(subcases):
            line = sys.stdin.readline().rstrip()
            title, artist = line.split(" - ")
            if x := in_artists(artist, artists):
                x.tracks.append(title)
            else:
                artists.append(Artist(artist, title))
        for artist in artists:
            artist.tracks.sort(key=lambda x: x.lower())
        artists.sort(key=lambda x: remove_the(x.name).lower())
        for artist in artists:
            for track in artist.tracks:
                print(f"{track} - {artist.name}")


main()
