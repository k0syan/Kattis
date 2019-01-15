if __name__ == "__main__":
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ_.")
    letters = [letter for letter in enumerate(letters)]
    while 1 == 1:
        tmp = input().split()
        if len(tmp) == 1:
            break
        else:
            c, word = int(tmp[0]), list(tmp[1])
            fword = []
            for w in word:
                i = 0
                for l in letters:
                    if l[1] == w:
                        i = l[0]
                        break
                i += c
                if i >= len(letters):
                    i -= len(letters)
                let = ""
                for l in letters:
                    if l[0] == i:
                        let = l[1]
                        break
                fword.append(let)
            fword.reverse()
            print("".join(fword))
            