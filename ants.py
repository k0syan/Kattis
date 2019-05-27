t = int(input())
while t != 0:
    l, n = [int(i) for i in input().split()]
    a = 0
    minimum, maximum = 0, 0
    while a < n:
        for ln in input().split():
            ln = int(ln)
            a += 1
            minimum = max(minimum, min(ln, l - ln))
            maximum = max(maximum, max(ln, l - ln))

    print(minimum, maximum)
    t -= 1
