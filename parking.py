if __name__ == "__main__":
    n = int(input())
    while n != 0:
        t = int(input())
        tmp = [int(i) for i in input().split()]
        print((max(tmp) - min(tmp)) * 2)
        n -= 1
