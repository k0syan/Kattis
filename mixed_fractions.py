if __name__ == "__main__":
    while 1 == 1:
        tmp = input().split()
        a, b = int(tmp[0]), int(tmp[1])
        if a == 0 and b == 0:
            break
        x = int(a / b)
        a = int(a % b)
        print(x, a, "/", b)

