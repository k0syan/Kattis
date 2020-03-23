x = [('a', 2), ('b', 22), ('c', 222), ('d', 3), ('e', 33), ('f', 333), ('g', 4), ('h', 44), ('i', 444),
        ('j', 5), ('k', 55), ('l', 555), ('m', 6), ('n', 66), ('o', 666), ('p', 7), ('q', 77), ('r', 777), ('s', 7777),
        ('t', 8), ('u', 88), ('v', 888), ('w', 9), ('x', 99), ('y', 999), ('z', 9999), (' ', 0)]
alph = dict(x)
n = int(input())
i = 1
while i <= n:
    ans = ""
    m = list(input())
    print(m)
    pm = m[0]
    ans += str(alph[pm])
    for i in range(1, len(m)):
        c = m[i]
        if pm == c:
            ans += " "
        ans += str(alph[c])
        pm = c

    print("CASE #" + str(i) + ": " + ans)
    i += 1
