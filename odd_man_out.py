if __name__ == "__main__":
    n = int(input())
    j = 1
    while n != 0:
        c = int(input())
        g = input().split()

        for i in range(len(g)):
            gn = g[i]
            if g.count(gn) == 1:
                print("Case #" + str(j) + ":", gn)
                break

        j += 1
        n -= 1
