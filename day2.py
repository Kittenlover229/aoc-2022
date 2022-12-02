part_1 = [
    # rock paper scissors
    [3, 0, 6], # rock
    [6, 3, 0], # paper
    [0, 6, 3],  # scissors
]

total = 0
for line in open("inputs.txt").readlines():
    def solve(score_matrix: list[list[int]]) -> int:
        a, b = line.strip().split(" ")
        l = ord(a) - ord('A')
        r = ord(b) - ord('X')
        return score_matrix[r][l] + (r + 1)
    total += solve(part_1)
print(total)
