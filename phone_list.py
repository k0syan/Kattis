n = int(input())
while n != 0:
    t = int(input())
    consistent = 1
    while t != 0:
        number = input()
        if number.startswith("911"):
            consistent = 0
        t -= 1
    if consistent == 1:
        print("YES")
    else:
        print("NO")
    n -= 1
