def sum_of_digits(t):
    if int(t / 10) == 0:
        return int(t % 10)
    else:
        return int(t % 10) + sum_of_digits(int(t / 10))


if __name__ == "__main__":
    n = int(input())
    while n != 0:
        s = sum_of_digits(n)
        a = 11
        while 1 == 1:
            if sum_of_digits(a * n) == s:
                break
            else:
                a += 1
        print(a)
        n = int(input())
        if n == 0:
            break
