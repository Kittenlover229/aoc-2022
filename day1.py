inputs = open("inputs.txt").read()
lines = [line.split() for line in inputs.split("\n\n")]
lines = list(map(lambda x: list(map(int, x)), lines))
lines = list(map(sum, lines))
lines.sort(reverse=True)

print ("Part one:")
print(lines[0])

print ("Part two:")
print(lines[0] + lines[1] + lines[2])
