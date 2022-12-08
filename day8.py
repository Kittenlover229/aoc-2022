from pprint import pprint


def solve_1():
    data = open("inputs.txt").read()
    data = [list(map(int, line)) for line in data.splitlines()]
    c = 0

    for i in range(1, len(data) - 1):
        for j in range(1, len(data[i]) - 1):
            left, right = data[i][:j], data[i][j + 1 :]
            up = list(map(lambda x: x[j], data[:i]))
            down = list(map(lambda x: x[j], data[i + 1 :]))

            all_less = lambda l: all((a < data[i][j] for a in l))
            if (
                all_less(left)
                or all_less(right)
                or all_less(up)
                or all_less(down)
            ):
                c += 1
    print(c + 2 * len(data) + 2 * len(data[0]) - 4)


solve_1()
