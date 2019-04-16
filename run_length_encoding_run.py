if __name__ == "__main__":
    answer = ""
    tmp = input().split()
    letters = list(tmp[1])
    if tmp[0] == "E":
        i = 0
        while i < len(letters):
            c = 1
            for j in range(i + 1, len(letters)):
                if letters[i] == letters[j]:
                    c += 1
                else:
                    break
            answer += letters[i] + str(c)
            i += c
    else:
        for i in range(1, len(letters)):
            cur = letters[i]
            prev = letters[i - 1]
            if cur.isdigit():
                answer += prev * int(cur)

    print(answer)
