"""System Module"""
import sys


class Student:
    def __init__(self, name: str, gpa: str, credit_hours: str):
        self.name = name
        self.gpa = gpa
        self.credit_hours = credit_hours


def main():
    values = {"A": 4, "B": 3, "C": 2, "D": 1}

    cases = int(sys.stdin.readline().rstrip())
    for caseNum in range(cases):
        school = sys.stdin.readline().rstrip()
        subCases = int(sys.stdin.readline().rstrip())
        students = []
        for _ in range(subCases):
            line = sys.stdin.readline().rstrip()
            name, classes = (val for val in line.split(" "))
            grades = list(val for val in classes.split(","))
            grade_points: int = 0
            credit_hours: int = 0
            for grade in grades:
                credit_hours += int(grade[1])
                temp = values.get(grade[0]) * int(grade[1])
                grade_points += values.get(grade[0]) * int(grade[1])
            GPA = grade_points / credit_hours
            students.append(Student(name, GPA, credit_hours))
        vale = []
        highest = 0
        for s in students:
            if s.gpa > highest:
                highest = s.gpa
        for s in students:
            if s.gpa == highest:
                vale.append(s)
        highest = 0
        if len(vale) > 1:
            for i, s in enumerate(vale):
                if s.credit_hours > highest:
                    highest = s.credit_hours
            for s in vale:
                if s.credit_hours == highest:
                    winner = s
        else:
            winner = vale[0]
        print(school + " = " + winner.name)


main()
