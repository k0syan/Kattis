if __name__ == "__main__":
    rules = list(input())
    r1c = 0
    r2c = 0
    r3c = 0
    curr = rules[0]
    for i in range(1, len(rules)):
        r = rules[i]

        if curr == "D":
            r1c += 1
        elif curr == "U" and r == "D":
            r1c += 2

        curr = "U"

    curr = rules[0]
    for i in range(1, len(rules)):
        r = rules[i]

        if curr == "U":
            r2c += 1
        elif curr == "D" and r == "U":
            r2c += 2

        curr = "D"

    for i in range(1, len(rules)):
        pr = rules[i - 1]
        r = rules[i]

        if r != pr:
            r3c += 1

    print(r1c)
    print(r2c)
    print(r3c)
