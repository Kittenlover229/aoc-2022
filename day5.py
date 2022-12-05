input = open("inputs.txt").read()

def process_input():
    crates, moves = input.split("\n\n")

    crates = crates.split("\n")[:-1]
    crates = list(map(lambda l: list(l[1::2])[::2], crates))
    crates = list(
        map(list, zip(*reversed(crates)))
    )  # transpose the list matrix

    crates = list(map(lambda x: "".join(x).strip(), crates))

    moves = moves.splitlines()
    return crates, moves

def solve_1():
    crates, moves = process_input()
    for move in moves:
        count, source, target = map(int, move.split(' ')[1::2])
        source -= 1
        target -= 1
        moved = crates[source][-count:]
        crates[source] = crates[source][:-count]
        crates[target] = crates[target] + moved[::-1]
    print("".join(map(lambda x: x[-1], crates)))

solve_1()
