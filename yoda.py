if __name__ == "__main__":
    a = [int(i) for i in list(input())]
    b = [int(i) for i in list(input())]

    af = []
    bf = []

    yp = 1
    if len(a) > len(b):
        while len(a) != len(b):
            b.insert(0, 0)
    elif len(a) < len(b):
        while len(a) != len(b):
            a.insert(0, 0)

    for i in range(len(a)):
        if a[i] > b[i]:
            af.append(a[i])
        elif a[i] < b[i]:
            bf.append(b[i])
        else:
            af.append(a[i])
            bf.append(b[i])

    ay = 0
    if len(af) == 0:
        ay = 1
    else:
        af = int("".join(map(str, af)))

    by = 0
    if len(bf) == 0:
        by = 1
    else:
        bf = int("".join(map(str, bf)))

    if ay == 1:
        print("YODA")
        print(bf)
    elif by == 1:
        print(af)
        print("YODA")
    else:
        print(af)
        print(bf)
