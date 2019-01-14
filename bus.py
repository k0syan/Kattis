if __name__ == "__main__":
    n = int(input())
    while n != 0:
        s = int(input())
        total = 0
        for i in range(1, s + 1):
            total = 1 + total * 2
        print(total)
        n -= 1
