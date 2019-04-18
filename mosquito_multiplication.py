if __name__ == "__main__":
    # m, p, l, e, r, s, n = [int(i) for i in input().split()]
    n = int(input())
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            print(i)
            sum += i
    print(sum)