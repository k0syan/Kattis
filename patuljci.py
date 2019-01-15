if __name__ == "__main__":
    d = []
    for k in range(9):
        d.append(int(input()))

    diff = sum(d) - 100
    for i in d:
        if diff - i == i:
            continue
        elif (diff - i) in d:
            d.remove(i)
            d.remove(diff - i)
            break

    for j in d:
        print(j)
