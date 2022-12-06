x = open('inputs.txt').read()

for i in range(1, len(x) - 4):
    y = len(set(x[i:i+4]))
    if y == 4:
        print(i + 4)
        break
