if __name__ == "__main__":
    n = int(input())
    while n != 0:
        imported = 0
        turtles = [int(i) for i in input().split()]
        for i in range(len(turtles) - 2):
            current = turtles[i]
            after = turtles[i + 1]
            if after > current * 2:
                imported += (after - current * 2)
        print(imported)
        n -= 1
