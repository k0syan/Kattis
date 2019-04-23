n = int(input())
digits = [1, 2, 6, 4]
while n != 0:
    d = int(input())
    if d == 0:
        print(1)
    elif d <= 4:
        print(digits[d - 1])
    else:
        print(0)
    n -= 1
