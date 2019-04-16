def domino(s):
    a = s.split(",")
    dominos = []
    for a1 in a:
        dominos.append(a1.split("-"))

    longest = 1
    cur = 1
    for i in range(len(dominos) - 1):
        c = dominos[i]
        n = dominos[i + 1]
        if c[1] == n[0]:
            cur += 1
        else:
            cur = 1

        if cur > longest:
            longest = cur

    return longest


if __name__ == "__main__":
    # print(domino("1-1"))
    # print(domino("1-2,1-2"))
    # print(domino("3-2,2-1,1-4,4-4,5-4,4-2,2-1"))
    # print(domino("5-5,5-5,4-4,5-5,5-5,5-5,5-5,5-5,5-5,5-5"))
