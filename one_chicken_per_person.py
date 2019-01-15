if __name__ == "__main__":
    tmp = input().split()
    p, c = int(tmp[0]), int(tmp[1])
    if c < p:
        if p - c == 1:
            print("Dr. Chaz needs 1 more piece of chicken!")
        else:
            print("Dr. Chaz needs " + str(p - c) + " more pieces of chicken!")
    elif c - p == 1:
        print("Dr. Chaz will have 1 piece of chicken left over!")
    else:
        print("Dr. Chaz will have " + str(c - p) + " pieces of chicken left over!")
