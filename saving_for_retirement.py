if __name__ == "__main__":
    b, br, by, a, ay = [int(i) for i in input().split()]
    x = a + 1
    total = (x - a) * ay
    btotal = (br - b) * by
    while total <= btotal:
        x += 1
        total = (x - a) * ay

    print(x)
