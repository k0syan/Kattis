n = int(input())
qaly = 0.0
while n > 0:
    tmp = input().split()
    quality, period = float(tmp[0]), float(tmp[1])
    qaly += quality * period
    n -= 1

print("{:.3f}".format(qaly))
