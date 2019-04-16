def findWord(arr):

    l = set()
    b = []

    for i in arr:
        v = i.split(' > ')
        l.add(v[0])
        l.add(v[1])
        b.append(v[0] + v[1])

    c = list(l)
    m = []
    word = ''

    le = 2
    while le != len(l):
        for i in range(len(b) - 1):
            for j in range(i + 1, len(b)):
                if b[i][1] == b[j][0]:
                    m.append(b[i][0] + b[j])
                if b[i][0] == b[j][1]:
                    m.append(b[j][0] + b[i])
        le = len(m[0])
        b = m
        m = []

    word = b[0]
    print(word)


if __name__ == "__main__":
    findWord(["U > N", "G > A", "R > Y", "H > U", "N > G", "A > R"])
    findWord(["I > F", "W > I", "S > W", "F > T"])
    findWord(["R > T", "A > L", "P > O", "O > R", "G > A", "T > U", "U > G"])
    findWord(["W > I", "R > L", "T > Z", "Z > E", "S > W", "E > R", "L > A", "A > N", "N > D", "I > T"])
