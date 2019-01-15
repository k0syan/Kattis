if __name__ == "__main__":
    n = int(input())
    w = input().split()
    g = 1
    for i in range(n):
        if w[i].isdigit() and int(w[i]) != i + 1:
            g = 0
            break
        elif not w[i].isdigit() and w[i] != "mumble":
            g = 0
            break

    if g == 1:
        print("makes sense")
    else:
        print("something is fishy")
