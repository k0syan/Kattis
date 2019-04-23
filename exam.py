if __name__ == "__main__":
    n = int(input())
    m = list(input())
    f = list(input())

    s = 0
    d = 0

    for i in range(len(m)):
        if m[i] == f[i]:
            s += 1
        else:
            d += 1

    print(s, d, n)
    pos = 0

    # if s > n:
    #     pos += n + d
    # else:
    #