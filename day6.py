def make_solve(z: int):
    x = open('inputs.txt').read()
    def solve():
        for i in range(1, len(x) - z):
            y = len(set(x[i:i+z]))
            if y == z:
                print(i + z)
                break
    return solve

make_solve(14)()
