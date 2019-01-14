def digitsCount(number):
    if int(number / 10) == 0:
        return 1
    else:
        return 1 + digitsCount(int(number / 10))


if __name__ == "__main__":
    n = int(input())
    while n != 0:
        c = int(input())
        print(digitsCount(c))
        n -= 1
