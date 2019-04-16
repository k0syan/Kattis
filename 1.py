def carr_count(n, m):
    nl = [int(i) for i in list(str(n))]
    ml = [int(i) for i in list(str(m))]

    c = 0
    if len(nl) < len(ml):
        while len(nl) != len(ml):
            nl.insert(0, 0)
    elif len(nl) > len(ml):
        while len(nl) != len(ml):
            ml.insert(0, 0)

    ml.insert(0, 0)
    nl.insert(0, 0)

    for i in range(len(nl)):
        a = nl[len(nl) - i - 1]
        b = ml[len(ml) - i - 1]
        if a + b >= 10:
            c += 1
            k = len(nl) - i - 2
            while k != 0:
                if ml[k] == 9:
                    ml[k] = 0
                else:
                    ml[k] += 1
                    break
                k -= 1
    return c

# carr count

if __name__ == "__main__":
    print(carr_count(9, 23))
