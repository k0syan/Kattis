if __name__ == "__main__":
    p = int(input())
    while p != 0:
        tmp = input().split()
        k, n = int(tmp[0]), int(tmp[1])
        positive = int(n * (n + 1) / 2)
        e1 = 2
        o1 = 1
        en = e1 + (n - 1) * 2
        on = o1 + (n - 1) * 2
        even = int(n * (e1 + en) / 2)
        odd = int(n * (o1 + on) / 2)

        print(k, positive, odd, even)
        p -= 1

