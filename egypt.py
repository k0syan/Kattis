if __name__ == "__main__":
    while 1 == 1:
        tmp = [int(x) for x in input().split()]
        tmp.sort()
        a, b, c = int(tmp[0]), int(tmp[1]), int(tmp[2])
        if a == 0 and b == 0 and c == 0:
            break

        if c * c == b * b + a * a:
            print("right")
        else:
            print("wrong")
