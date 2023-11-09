"""Problem Solution"""
import math


class Tri:
    def __init__(
        self, p1: tuple[int, int], p2: tuple[int, int], p3: tuple[int, int]
    ) -> None:
        self.a = math.dist(p1, p2)
        self.b = math.dist(p2, p3)
        self.c = math.dist(p1, p3)
        cosA = self.b**2 + self.c**2 - self.a**2
        cosA /= 2 * self.b * self.c
        self.A = math.acos(cosA)
        cosB = -self.b**2 + self.c**2 + self.a**2
        cosB /= 2 * self.a * self.c
        self.B = math.acos(cosB)
        cosC = self.b**2 - self.c**2 + self.a**2
        cosC /= 2 * self.b * self.a
        self.C = math.acos(cosC)
        self.middle_line = max(self.a, self.b, self.c)
        # print(*map(math.degrees, (self.A, self.B, self.C)))
        if self.c == self.middle_line:
            self.corner_angle = self.C
        elif self.b == self.middle_line:
            self.corner_angle = self.B
        elif self.a == self.middle_line:
            self.corner_angle = self.A


def main():

    cases = int(input())
    for _ in range(cases):
        points: list[tuple[int, int]] = []
        for _ in range(4):
            x, y = (int(val) for val in input().split(" "))
            points.append((x, y))
        tr1 = Tri(points[0], points[1], points[2])
        tr2 = Tri(points[1], points[2], points[3])
        tr3 = Tri(points[2], points[3], points[0])
        c1 = tr1.corner_angle
        c2 = tr2.corner_angle
        c3 = tr3.corner_angle
        c4 = (2 * math.pi) - (c1 + c2 + c3)
        c1, c2, c3, c4 = map(int(map(math.degrees, (c1, c2, c3, c4))))
        # print(*map(math.degrees, (c1, c2, c3, c4)))
        print(c1, c2, c3, c4)
        if c1 == c2 and c2 == c3 and c3 == c4:
            print("Square")


main()
