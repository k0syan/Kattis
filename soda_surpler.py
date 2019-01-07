if __name__ == "__main__":
    tmp = input().split()
    e, f, c = int(tmp[0]), int(tmp[1]), int(tmp[2])
    total = 0
    e += f
    while e != 0:
        curr = int(e / c)
        total += curr
        e = int(e % c)
        e += curr
        if e < c:
            break
    print(total)

