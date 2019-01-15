if __name__ == "__main__":
    tmp = input().split()
    n, m = int(tmp[0]), int(tmp[1])
    tasks = [int(i) for i in input().split()]
    i = 0
    total = 0
    for t in tasks:
        total += t
        if total <= m:
            i += 1
        else:
            break
    print(i)
