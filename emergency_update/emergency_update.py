"""System Module"""
import sys


class Emp:
    def __init__(self, name: str, phone: str, address: str) -> None:
        self.name = name
        self.phone = phone
        self.addr = address


def emp_in_list(employee: Emp, emp_list: list[Emp]):
    for emp in emp_list:
        if employee.name == emp.name:
            return emp


def main():

    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        line = sys.stdin.readline().rstrip()
        n_old, n_new = (int(val) for val in line.split(" "))
        old: list[str] = []
        new: list[str] = []
        old_emps: list[Emp] = []
        new_emps: list[Emp] = []
        for _ in range(n_old):
            old.append(sys.stdin.readline().rstrip())
        for _ in range(n_new):
            new.append(sys.stdin.readline().rstrip())
        for entry in old:
            name, phone, address = entry.split(",")
            old_emps.append(Emp(name, phone, address))
        for entry in new:
            name, phone, address = entry.split(",")
            new_emps.append(Emp(name, phone, address))
        outputs: list[str] = []
        for emp in old_emps:
            if x := emp_in_list(emp, new_emps):
                if emp.phone != x.phone and emp.addr != x.addr:
                    outputs.append(f"{emp.name} UPDATED BOTH")
                elif emp.addr != x.addr:
                    outputs.append(f"{emp.name} UPDATED ADDRESS")
                elif x.phone != emp.phone:
                    outputs.append(f"{emp.name} UPDATED PHONE NUMBER")
                new_emps.remove(x)
            else:
                outputs.append(f"{emp.name} DELETED")
        for emp in new_emps:
            outputs.append(f"{emp.name} CREATED")
        outputs.sort()
        for out in outputs:
            print(out)


main()
