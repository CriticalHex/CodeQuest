def print_list(l: list[list[str]]):
    for row in l:
        print(row)


def main():

    cases = int(input())
    for _ in range(cases):
        xy: list[list[str]] = []
        yx: list[list[str]] = []
        rows, columns = (int(val) for val in input().split(" "))
        for _ in range(rows):
            xy.append(input().split(","))
        for _ in range(columns):
            yx.append([])
        for i in range(columns):
            for j in range(rows):
                yx[i].append(xy[j][i])
        for row in yx:
            print(*row, sep=",")


main()
