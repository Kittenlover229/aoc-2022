s = 0
for ss in open("inputs.txt").readlines():
    l = len(ss)
    print(ss[:l//2], ss[l//2:])
    a = set(ss[l//2:])
    b = set(ss[:l//2])
    diff = list(a.intersection(b))[0]
    print(diff)
    diff = ord(diff)
    if ord("a") <= diff <= ord("z"):
        x = diff - ord("a") + 1
    elif ord("A") <= diff <= ord("Z"):
        x = diff - ord("A") + 26 + 1
    s += x

print(s)
