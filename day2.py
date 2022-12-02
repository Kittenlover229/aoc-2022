total = 0
for line in open("inputs.txt").readlines():

    def solve_1(me, them) -> int:
        # 3 + 0 - 0 = 3 = 0 rock vs rock
        # 3 + 1 - 0 = 4 = 1 paper vs rock
        # 3 + 2 - 0 = 5 = 2 scissors vs rock
        # 3 + 0 - 1 = 2 = 2 rock vs paper
        # 3 + 1 - 1 = 3 = 0 paper vs paper
        # 3 + 2 - 1 = 4 = 1 scissors vs paper
        # 3 + 0 - 2 = 1 = 1 rock vs scissors
        # 3 + 1 - 2 = 2 = 2 paper vs scissors
        # 3 + 2 - 2 = 3 = 0 scissors vs scissors

        # +1 to roll the array
        # 0 is a loss
        # 1 is a draw
        # 2 is a win

        i = (3 + me - them + 1) % 3
        print(x := [0, 3, 6][i], y := me + 1, z := x + y)
        return z

    def solve_2(me, them) -> int:
        i = (them + me - 1) % 3
        print(x := i + 1, y := [0, 3, 6][me], z := x + y)
        return z

    a, b = line.strip().split(" ")
    l = ord(a) - ord("A")
    r = ord(b) - ord("X")
    total += solve_2(r, l)

print(total)
