if __name__ == "__main__":
    tmp = input().split()
    r, c = int(tmp[0]), int(tmp[1])
    ta = r * r
    outer = ta - (r - c) * (r - c)
    print((1 - outer / ta) * 100)
