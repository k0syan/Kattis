if __name__ == "__main__":
    n = int(input())
    total = 0
    while n != 0:
        abilities = list(input())
        won = 1
        for i in range(len(abilities) - 1):
            previous = abilities[i]
            next = abilities[i + 1]
            if previous == "C" and next == "D":
                won = 0
                break
        total += won
        n -= 1

    print(total)
