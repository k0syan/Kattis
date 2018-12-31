if __name__ == "__main__":
    n = int(input())
    j = 1
    while 1 == 1:
        if n == 0:
            break
        unordered = [""] * n
        ordered = [""] * n
        for i in range(n):
            unordered[i] = input()

        for i in range(int(n / 2)):
            ordered[i] = unordered[i * 2]
            ordered[n - i - 1] = unordered[2 * i + 1]

        if n % 2 == 1:
            ordered[int(n / 2)] = unordered[n - 1]

        print("SET", j)
        for i in range(n):
            print(ordered[i])

        j += 1
        n = int(input())
