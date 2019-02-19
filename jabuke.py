def cArea(a1, a2, a3, b1, b2, b3):
    return abs(a1 * (b2 - b3) + a2 * (b3 - b1) + a3 * (b1 - b2)) / 2


if __name__ == "__main__":
    x = [int(t) for t in input().split()]
    y = [int(t) for t in input().split()]
    z = [int(t) for t in input().split()]

    xa, ya = x[0], x[1]
    xb, yb = y[0], y[1]
    xc, yc = z[0], z[1]

    area = cArea(xa, xb, xc, ya, yb, yc)

    trees = int(input())
    ti = 0
    for i in range(trees):
        t = input().split()
        tx, ty = int(t[0]), int(t[1])
        ar1 = cArea(tx, xa, xb, ty, ya, yb)
        ar2 = cArea(tx, xb, xc, ty, yb, yc)
        ar3 = cArea(tx, xa, xc, ty, ya, yc)

        if area == ar1 + ar2 + ar3:
            ti += 1

    print("{:.1f}".format(area))
    print(ti)
