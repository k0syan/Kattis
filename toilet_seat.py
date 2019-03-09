if __name__ == "__main__":
    rules = list(input())
    r1c = 0
    r2c = 0
    r3c = 0
    for i in range(len(rules) - 1):
        r = rules[i]
        nr = rules[i + 1]

        if i == 0:
            if r != "U":
                r1c += 1

            if r != "D":
                r2c += 1

            if r != nr:
                r3c += 1
        else:
            if r != "U":
                r1c += 2

            if r != "D":
                r2c += 2

            if r != nr:
                r3c += 1

    print(r1c)
    print(r2c)
    print(r3c)
