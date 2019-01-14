def sumOfDigits(number):
    if int(number / 10) == 0:
        return int(number % 10)
    else:
        return int(number % 10) + sumOfDigits(int(number / 10))


if __name__ == "__main__":
    n = int(input())
    while 1 == 1:
        if n % sumOfDigits(n) == 0:
            print(n)
            break
        else:
            n += 1
