def solve_1():
    c = 0
    for line in open("inputs.txt").readlines():
        ls = list(
            map(
                lambda y: tuple(map(int, y.split("-"))),
                line.strip().split(","),
            )
        )
        a, b = ls
        if a > b:
            a, b = b, a
        if (a[0] >= b[0] and a[1] <= b[1]) or (a[0] <= b[0] and a[1] >= b[1]):
            c += 1
    print(c)

solve_1()
