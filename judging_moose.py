if __name__ == "__main__":
    tmp = input().split()
    l, r = int(tmp[0]), int(tmp[1])
    if l == r == 0:
        print("Not a moose")
    elif l == r:
        print("Even", 2 * r)
    elif l > r:
        print("Odd", 2 * l)
    else:
        print("Odd", 2 * r)
