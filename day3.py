def score(d):
    if ord("a") <= d <= ord("z"):
        x = d - ord("a") + 1
    elif ord("A") <= d <= ord("Z"):
        x = d - ord("A") + 26 + 1
    return x

def solve_1():
    s = 0

    for ss in open("inputs.txt").readlines():
        l = len(ss)
        print(ss[:l//2], ss[l//2:])
        a = set(ss[l//2:])
        b = set(ss[:l//2])
        diff = list(a.intersection(b))[0]
        print(diff)
        d = ord(diff)
        s += score(d)
    print(s)

def solve_2():
    k = []
    s = 0
    for ss in open("inputs.txt").readlines():
        k.append(ss.strip())
        if len(k) != 3:
            continue
        a, b, c = map(set, k)
        x = a.intersection(b).intersection(c)
        s += score(ord(list(x)[0]))
        k.clear()
    print(s)

solve_2()
