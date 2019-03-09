n = int(input())
while n != 0:
    t = int(input())
    m = t
    consistent = True
    emergency = 0
    numbers = []
    while t != 0:
        number = input()
        numbers.append(number)
        t -= 1
    numbers.sort()
    for i in range(1, len(numbers)):
        prev = numbers[i - 1]
        cur = numbers[i]
        if cur.startswith(prev):
            consistent = False
            break

    if consistent:
        print("YES")
    else:
        print("NO")
    n -= 1
