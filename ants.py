t = int(input())
while t != 0:
    l, n = [int(i) for i in input().split()]
    ants = []
    while len(ants) < n:
        line = input().split()
        for ln in line:
            ants.append(int(ln))

    minimum, maximum = 0, 0
    for a in ants:
        minimum = max(minimum, min(a, l - a))
        maximum = max(maximum, max(a, l - a))

    print(minimum, maximum)
    t -= 1
