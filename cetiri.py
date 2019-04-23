if __name__ == "__main__":
    numbers = [int(i) for i in input().split()]
    numbers.sort()
    a, b, c = numbers
    if c - b == b - a:
        print(c + c - b)
    elif c - b > b - a:
        print(b + b - a)
    else:
        print(a + c - b)
