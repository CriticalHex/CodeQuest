"""System Module"""
import sys


def answer_to_percent(correct: str, answer: str):
    all = len(correct)
    right: int = 0
    for i in range(all):
        if answer[i] == correct[i]:
            right += 1
    return right / all


def percent_to_letter(percent: float):
    if percent < 0.6:
        return "F"
    if percent < 0.7:
        return "D"
    if percent < 0.8:
        return "C"
    if percent < 0.9:
        return "B"
    return "A"


def better_round(val: float, n_digits: int = 0) -> float:
    """Round Half Up"""
    val *= 10**n_digits
    result = int(val + (0.5 if val >= 0 else -0.5))
    return result / 10**n_digits


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        n_students, correct = sys.stdin.readline().rstrip().split(" ")
        students: dict[str, str] = {}
        for _ in range(int(n_students)):
            line = sys.stdin.readline().rstrip()
            name, answers = line.split(" ")
            students[name] = answers
        for name, answer in students.items():
            percent = answer_to_percent(correct, answer)
            grade = percent_to_letter(percent)
            p_str = f"{better_round(percent * 100, 1)}%"
            print(f"{name} {p_str} {grade}")


main()
