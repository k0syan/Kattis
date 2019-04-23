if __name__ == "__main__":
    n = int(input())
    while n != 0:

        t, d = [int(i) for i in input().split()]
        needed = d

        needed += (d * (d + 1) / 2)

        print(t, int(needed))
        n -= 1
