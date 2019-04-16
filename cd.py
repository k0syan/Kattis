if __name__ == "__main__":
    while True:
        n, m = [int(i) for i in input().split()]
        if n == 0 and m == 0:
            break
        jack = set()
        count = 0
        for i in range(n):
            jack.add(input())
        jack = set(jack)
        for j in range(m):
            tmp = input()
            if jack.__contains__(tmp):
                count += 1

        print(count)
