if __name__ == "__main__":
    n = int(input())
    radiuses = [int(i) for i in input().split()]
    for i in range(1, n):
        r1 = radiuses[0]
        r2 = radiuses[i]
        d = r2
        while 1 == 1:
            if int(r1 % d) == 0 and int(r2 % d) == 0:
                r1, r2 = int(r1 / d), int(r2 / d)
                break
            else:
                d -= 1
        ans = str(r1) + "/" + str(r2)
        print(ans)
