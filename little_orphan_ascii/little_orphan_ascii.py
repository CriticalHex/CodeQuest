"""System Module"""
import sys


class WorkOrder:
    def __init__(self, id: int, title: str, reported: str) -> None:
        self.id = id
        self.title = title
        self.reported = reported


class WorkTask:
    def __init__(
        self, id: int, work_order_id: int, part_id: int, assigned_to: str
    ) -> None:
        self.id = id
        self.work_order_id = work_order_id
        self.part_id = part_id
        self.assigned_to = assigned_to


class Part:
    def __init__(self, id: int, name: str, serial_number: str) -> None:
        self.id = id
        self.name = name
        self.serial_number = serial_number


def main():
    cases = int(sys.stdin.readline().rstrip())
    for _ in range(cases):
        orders: list[WorkOrder] = []
        tasks: list[WorkTask] = []
        parts: list[Part] = []
        line = sys.stdin.readline().rstrip()
        n_orders, n_tasks, n_parts = (int(val) for val in line.split(" "))
        for _ in range(n_orders):
            line = sys.stdin.readline().rstrip()
            id, title, reported = line.split(",")
            id = int(id)
            orders.append(WorkOrder(id, title, reported))
        for _ in range(n_tasks):
            line = sys.stdin.readline().rstrip()
            id, work_order_id, part_id, assigned_to = line.split(",")
            id, work_order_id, part_id = int(id), int(work_order_id), int(part_id)
            tasks.append(WorkTask(id, work_order_id, part_id, assigned_to))
        for _ in range(n_parts):
            line = sys.stdin.readline().rstrip()
            id, name, serial_number = line.split(",")
            id = int(id)
            parts.append(Part(id, name, serial_number))
        tasks.sort(key=lambda x: x.id)
        for task in tasks:
            output: str = f"{task.id} "
            if task.work_order_id not in [order.id for order in orders]:
                output += f"MISSING WORK_ORDER {task.work_order_id} "
            if task.part_id not in [part.id for part in parts]:
                output += f"MISSING PART {task.part_id} "
            if output != f"{task.id} ":
                print(output.rstrip())


main()
