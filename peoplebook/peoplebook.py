"""System Module"""
import sys


class Person:
    def __init__(
        self, name: str, age: str, insta: str, twt: str, phone: str, email: str
    ) -> None:
        self.name = name.lstrip("[[")
        self.age = age
        self.insta = insta
        self.twitter = twt
        self.phone = phone
        self.email = email.rstrip("]]")

    def print(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Instagram: {self.insta}")
        print(f"Twitter: {self.twitter}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")


def info(data: list[str], index: int):
    return (
        data[0].split(",")[index],
        data[1].split(",")[index],
        data[2].split(",")[index],
        data[3].split(",")[index],
        data[4].split(",")[index],
        data[5].split(",")[index],
    )


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        people: list[Person] = []
        n_people = int(sys.stdin.readline().rstrip())
        line = sys.stdin.readline().rstrip()
        data = line.split("],[")
        for i in range(n_people):
            people.append(Person(*info(data, i)))
        for _ in range(n_people):
            get = sys.stdin.readline().rstrip()
            for person in people:
                if person.name == get:
                    person.print()


main()
